import dns.resolver
import dns.exception

def get_cname_record(domain):
    try:
        answers = dns.resolver.resolve(domain, 'CNAME')
        cname_target = answers[0].target.to_text().rstrip('.')
        return cname_target
    except dns.resolver.NoAnswer:
        return None
    except dns.resolver.NXDOMAIN:
        return None
    except (dns.exception.Timeout, dns.resolver.NoNameservers):
        return None
    except Exception:
        return None