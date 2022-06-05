import os
import sys
def shodan():
    ip = sys.argv[1]
    x = os.system(f'curl -X GET "https://api.shodan.io/shodan/host/{ip}?key=b2kVKUUFHe0bjBcrB1mhr1S8YLz0myx8"')


#/***************************************************************
#*
#* Copyright (Wouter Weemaes, Safi Bouziane, Kamil Grielens, Robbe Willeme) - All rights reserved. 
#*
#* Unauthorized use, copy, modify, merge, publish, distribute, sublicense, 
#* and/or sell any parts of the software/source code is strictly prohibited.
#* Proprietary and confidential
#* License: No license. 
#* Written by: (Wouter Weemaes) (wouterweemaes@outlook.com), (06/2022)
#*
#****************************************************************/
