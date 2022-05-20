import os
import sys
def shodan():
    ip = "8.8.8.8"
    x = os.system(f'curl -X GET "https://api.shodan.io/shodan/host/8.8.8.8?key=b2kVKUUFHe0bjBcrB1mhr1S8YLz0myx8"')
    print(ip)
    print(x)