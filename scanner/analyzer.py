import requests
from .dns_check import get_cname_record
from .vendor_fingerprint import FINGERPRINTS

def check_dangling_vulnerability(cname_target, fingerprint):
    try:
        response = requests.get(f"http://{cname_target}", timeout=10, allow_redirects=False)
        if response.status_code in fingerprint.get("status_codes", []):
            content_match = True
            for content_string in fingerprint.get("content_strings", []):
                if content_string not in response.text:
                    content_match = False
                    break
            if content_match or not fingerprint.get("content_strings"):
                return True
    except requests.exceptions.RequestException:
        pass
    return False

def scan_domains(file_path):
    dangling_domains = []
    try:
        with open(file_path, 'r') as f:
            domains = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"[!] Error: File '{file_path}' tidak ditemukan.")
        return []

    print(f"[*] Memulai pemindaian untuk {len(domains)} domain...")

    for domain in domains:
        print(f"[*] Memeriksa: {domain}")
        cname_target = get_cname_record(domain)
        if not cname_target:
            print(f"    - Tidak ada record CNAME. Dilewati.")
            continue
        print(f"    - CNAME ditemukan -> {cname_target}")

        identified_service = None
        for key, fingerprint in FINGERPRINTS.items():
            if key in cname_target:
                identified_service = fingerprint
                break
        
        if not identified_service:
            print(f"    - Layanan tidak dikenali. Dilewati.")
            continue
        print(f"    - Layanan teridentifikasi: {identified_service['service_name']}")

        is_vulnerable = check_dangling_vulnerability(cname_target, identified_service)
        if is_vulnerable:
            print(f"    [!!!] VULNERABLE: Domain ini bisa di-takeover!")
            target_name = cname_target.split('.')[0]
            result = {
                'original_domain': domain,
                'target': target_name,
                'service': identified_service['service_name'].lower().replace(" ", "_")
            }
            if identified_service['service_name'] == 'Azure App Service':
                result['resource_group'] = None
            dangling_domains.append(result)
        else:
            print(f"    - Aman atau tidak terdeteksi.")
    
    print(f"\n[*] Pemindaian selesai. Ditemukan {len(dangling_domains)} domain yang rentan.")
    return dangling_domains