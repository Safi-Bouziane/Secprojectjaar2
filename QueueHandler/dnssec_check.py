import urllib.request
def dnscheck(Url):
    # Check that the program was called with command-line arguments and if so, check the domains
        if len(Url) > 1:
            for domain in Url[1:]:
                results = urllib.request.urlopen('http://portfolio.sidnlabs.nl/check/%s' % domain).read()

                newResults = results.decode('utf-8').split()
                finalResult = newResults[0].replace(domain, '').replace(',', '')
                return domain + " is " + finalResult + " with DNSSEC."
        else:
            return "No domain was given."