import os
import sys
def shodan():
    ip = sys.argv[1]
    x = os.system(f'curl -X GET "https://api.shodan.io/shodan/host/{ip}?key=b2kVKUUFHe0bjBcrB1mhr1S8YLz0myx8"')