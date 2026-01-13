import requests
from config import Config

def send_success_notification(chat_id, domain_info):
    if not chat_id or not Config.TELEGRAM_BOT_TOKEN:
        print("[!] Chat ID atau Bot Token tidak dikonfigurasi. Notifikasi tidak dikirim.")
        return
    message = f"🎉 **BERHASIL CLAIM DOMAIN!** 🎉\n\n"
    message += f"🌐 Domain: `{domain_info['original_domain']}`\n"
    message += f"⚙️ Layanan: {domain_info['service']}\n"
    message += f"🎯 Target: `{domain_info['target']}`"
    url = f"https://api.telegram.org/bot{Config.TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {'chat_id': chat_id, 'text': message, 'parse_mode': 'Markdown'}
    try:
        requests.post(url, json=payload)
        print(f"[*] Notifikasi Telegram terkirim ke {chat_id}")
    except Exception as e:
        print(f"[!] Gagal mengirim notifikasi Telegram: {e}")