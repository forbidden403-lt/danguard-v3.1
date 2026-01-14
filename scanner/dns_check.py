import dns.resolver
import dns.exception
import multiprocessing
import time

def _resolve_cname_in_process(domain):
    """
    Fungsi ini akan dijalankan di proses terpisah.
    Fungsi ini hanya berfokus pada satu tugas: resolve DNS.
    """
    try:
        answers = dns.resolver.resolve(domain, 'CNAME', lifetime=5.0)
        cname_target = answers[0].target.to_text().rstrip('.')
        return cname_target
    except Exception:
        return None

def get_cname_record(domain):
    """
    Mencoba mendapatkan record CNAME dengan timeout yang sangat ketat.
    Menggunakan multiprocessing untuk memastikan program tidak akan macet.
    """
    process = multiprocessing.Process(target=_resolve_cname_in_process, args=(domain,))
    process.start()
    
    process.join(timeout=7.0)
    
    if process.is_alive():
        process.terminate()
        process.join() 
        print(f"    - DNS query untuk {domain} timeout. Dilewati.")
        return None

    
    try:
        answers = dns.resolver.resolve(domain, 'CNAME', lifetime=2.0) 
        cname_target = answers[0].target.to_text().rstrip('.')
        return cname_target
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout, dns.resolver.NoNameservers, dns.exception.DNSException):
        return None
    except Exception:
        return None
