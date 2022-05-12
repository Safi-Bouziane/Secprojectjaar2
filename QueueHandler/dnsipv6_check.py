import dns.resolver
def ipv6(url):
    my_resolver = dns.resolver.Resolver()
    domain = url
    if domain.startswith(('http://')):
            domain = domain[7:]
    elif domain.startswith(('https://')):
            domain = domain[8:]
    else:
        domain = domain
    try:
        result = my_resolver.resolve(domain, "AAAA")
        return result[0]
    except dns.resolver.NoAnswer:
        return "No AAAA records"
    except dns.resolver.NXDOMAIN:
        return"No such domain"
