import dns.resolver
import dns.exception

def get_cname_record(domain):
    """
    Mencoba mendapatkan record CNAME dari sebuah domain.
    Mengembalikan string CNAME jika ditemukan, None jika tidak ada atau terjadi error.
    Dilengkapi dengan timeout untuk mencegah program macet.
    """
    try:
        
        
        answers = dns.resolver.resolve(domain, 'CNAME', lifetime=5.0)
        
        
        cname_target = answers[0].target.to_text().rstrip('.')
        return cname_target
        
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        
        return None
    except (dns.exception.Timeout, dns.resolver.NoNameservers, dns.exception.DNSException):
        
        
        return None
    except Exception:
        
        return None
