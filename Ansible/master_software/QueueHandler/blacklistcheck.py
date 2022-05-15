#https://github.com/jgamblin/isthisipbad/blob/master/isthisipbad.py
import os
import sys
import urllib3
import argparse
import re
import mysql.connector
import socket
import dns
import warnings
from dns import resolver 
from requests import get

def blacklist(Url):
    warnings.filterwarnings("ignore", category=DeprecationWarning)


    def color(text, color_code):
        if sys.platform == "win32" and os.getenv("TERM") != "xterm":
            return text

        return '\x1b[%dm%s\x1b[0m' % (color_code, text)


    def red(text):
        return color(text, 31)


    def blink(text):
        return color(text, 5)


    def green(text):
        return color(text, 32)


    def blue(text):
        return color(text, 34)


    def content_test(url, badip):
        try:
            request = urllib3.Request(url)
            opened_request = urllib3.build_opener().open(request)
            html_content = opened_request.read()
            retcode = opened_request.code

            matches = retcode == 200
            matches = matches and re.findall(badip, html_content)

            return len(matches) == 0
        except:
            return False

    bls = ["b.barracudacentral.org", "bl.spamcop.net",
        "blacklist.woody.ch", "cbl.abuseat.org", 
        "combined.abuse.ch", "combined.rbl.msrbl.net", 
        "db.wpbl.info", "dnsbl.cyberlogic.net",
        "dnsbl.sorbs.net", "drone.abuse.ch", "drone.abuse.ch",
        "duinv.aupads.org", "dul.dnsbl.sorbs.net", "dul.ru",
        "dynip.rothen.com",
        "http.dnsbl.sorbs.net", "images.rbl.msrbl.net",
        "ips.backscatterer.org", "ix.dnsbl.manitu.net",
        "korea.services.net", "misc.dnsbl.sorbs.net",
        "noptr.spamrats.com", "ohps.dnsbl.net.au", "omrs.dnsbl.net.au",
        "osps.dnsbl.net.au", "osrs.dnsbl.net.au",
        "owfs.dnsbl.net.au", "pbl.spamhaus.org", "phishing.rbl.msrbl.net",
        "probes.dnsbl.net.au", "proxy.bl.gweep.ca", "rbl.interserver.net",
        "rdts.dnsbl.net.au", "relays.bl.gweep.ca", "relays.nether.net",
        "residential.block.transip.nl", "ricn.dnsbl.net.au",
        "rmst.dnsbl.net.au", "smtp.dnsbl.sorbs.net",
        "socks.dnsbl.sorbs.net", "spam.abuse.ch", "spam.dnsbl.sorbs.net",
        "spam.rbl.msrbl.net", "spam.spamrats.com", "spamrbl.imp.ch",
        "t3direct.dnsbl.net.au", "tor.dnsbl.sectoor.de",
        "torserver.tor.dnsbl.sectoor.de", "ubl.lashback.com",
        "ubl.unsubscore.com", "virus.rbl.jp", "virus.rbl.msrbl.net",
        "web.dnsbl.sorbs.net", "wormrbl.imp.ch", "xbl.spamhaus.org",
        "zen.spamhaus.org", "zombie.dnsbl.sorbs.net"]

    URLS = [
        #TOR
        ('http://torstatus.blutmagie.de/ip_list_exit.php/Tor_ip_list_EXIT.csv',
        'is not a TOR Exit Node',
        'is a TOR Exit Node',
        False),

        #EmergingThreats
        ('http://rules.emergingthreats.net/blockrules/compromised-ips.txt',
        'is not listed on EmergingThreats',
        'is listed on EmergingThreats',
        True),

        #AlienVault
        ('http://reputation.alienvault.com/reputation.data',
        'is not listed on AlienVault',
        'is listed on AlienVault',
        True),

        #BlocklistDE
        ('http://www.blocklist.de/lists/bruteforcelogin.txt',
        'is not listed on BlocklistDE',
        'is listed on BlocklistDE',
        True),

        #Dragon Research Group - SSH
        ('http://dragonresearchgroup.org/insight/sshpwauth.txt',
        'is not listed on Dragon Research Group - SSH',
        'is listed on Dragon Research Group - SSH',
        True),

        #Dragon Research Group - VNC
        ('http://dragonresearchgroup.org/insight/vncprobe.txt',
        'is not listed on Dragon Research Group - VNC',
        'is listed on Dragon Research Group - VNC',
        True),

        #NoThinkMalware
        ('http://www.nothink.org/blacklist/blacklist_malware_http.txt',
        'is not listed on NoThink Malware',
        'is listed on NoThink Malware',
        True),

        #NoThinkSSH
        ('http://www.nothink.org/blacklist/blacklist_ssh_all.txt',
        'is not listed on NoThink SSH',
        'is listed on NoThink SSH',
        True),

        #Feodo
        ('http://rules.emergingthreats.net/blockrules/compromised-ips.txt',
        'is not listed on Feodo',
        'is listed on Feodo',
        True),

        #antispam.imp.ch
        ('http://antispam.imp.ch/spamlist',
        'is not listed on antispam.imp.ch',
        'is listed on antispam.imp.ch',
        True),

        #dshield
        ('http://www.dshield.org/ipsascii.html?limit=10000',
        'is not listed on dshield',
        'is listed on dshield',
        True),

        #malc0de
        ('http://malc0de.com/bl/IP_Blacklist.txt',
        'is not listed on malc0de',
        'is listed on malc0de',
        True),

        #MalWareBytes
        ('http://hosts-file.net/rss.asp',
        'is not listed on MalWareBytes',
        'is listed on MalWareBytes',
        True)]



    parser = argparse.ArgumentParser(description='Is This IP Bad?')
    parser.add_argument('-i', '--ip', help='IP address to check')
    parser.add_argument('--success', help='Also display GOOD', required=False, action="store_true")
    args, unknown = parser.parse_known_args()

    if args is not None and args.ip is not None and len(args.ip) > 0:
        badip = args.ip
    else:
        # Get IP To Check
        website = str(Url)# you can put any website
        if website.startswith(('http://')):
            website = website[7:]
        elif website.startswith(('https://')):
            website = website[8:]
        else:
            website = website
        try:
          ip = socket.gethostbyname(website)
        except:
            return 'check failed'
        badip = ip
        if badip is None or badip == "":
            sys.exit("No IP address to check.")
    BAD = 0
    GOOD = 0

    for url, succ, fail, mal in URLS:
        if content_test(url, badip):
            if args.success:
                (green('{0} {1}'.format(badip, succ)))
                GOOD = GOOD + 1
            else:
                (red('{0} {1}'.format(badip, fail)))
                BAD = BAD + 1

    BAD = BAD
    GOOD = GOOD

    for bl in bls:
        try:
                my_resolver = dns.resolver.Resolver()
                query = '.'.join(reversed(str(badip).split("."))) + "." + bl
                my_resolver.timeout = 5
                my_resolver.lifetime = 5
                answers = my_resolver.query(query, "A")
                answer_txt = my_resolver.query(query, "TXT")
                BAD = BAD + 1

        except dns.resolver.NXDOMAIN:
            GOOD = GOOD + 1

        except dns.resolver.Timeout:
            blink('WARNING: Timeout querying ' + bl)

        except dns.resolver.NoNameservers:
            blink('WARNING: No nameservers for ' + bl)

        except dns.resolver.NoAnswer:
            blink('WARNING: No answer for ' + bl)

    return str('{0} is on {1}/{2} blacklists.'.format(badip, BAD, (GOOD+BAD)))

result = blacklist(sys.argv[1])
rowid = sys.argv[2]

if 1:
        mydb = mysql.connector.connect(
        host="securityprojecthowsami.mysql.database.azure.com",
        user="safidesafi@securityprojecthowsami.mysql.database.azure.com",
        password="DeltaGroepPassword#",
        database="securityproject")
        mycursor = mydb.cursor()
        sql = f"UPDATE Result SET TEST3 = %s WHERE ID = %s"
        val = (result,rowid)
        mycursor.execute(sql, val)
        mydb.commit()