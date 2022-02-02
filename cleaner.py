#!/bin/python3
# R7_API_Cleaner
# By Doug Leidgen - 12/2021
#
# This script is used to delete old machines out of Rapid7 IVM Console

import requests
import sys

# The following will suppress error messages.  DO NOT USE WITHOUT SUPERVISION
class DevNull:
    def write(self, msg):
        pass

sys.stderr = DevNull()


url1 = 'https://server:3780/api/3/asset_groups/67/assets'
url2 = 'https:/server:3780/api/3/asset_groups/68/assets'
url3 = 'https://server:3780/api/3/asset_groups/30/assets'
heads = {'Authorization': 'Basic BadStuff5goHere'}
itch = 1
scratch = 0
opv = ' '

while itch < 4:
    if itch == 1:
        opv = url1
    elif itch == 2:
        opv = url2
    elif itch == 3:
        opv = url3
    else:
        opv = ' '
        break

    #print(opv)  #debug
    
    r = requests.get(opv, verify=False, headers=heads)
    machines = r.json()["resources"]

    for i in machines:
        #print(i)    #debug
        si = str(i)
        lurl = 'https://server:3780/api/3/assets/' + si
        #print(lurl) #debug
        mr = requests.delete(lurl, verify=False, headers=heads)
        print(si + ' has been deleted') # Comment out for automation

    itch += 1
    scratch += 1

    try:
        del machines
    except:
        print('Deleting machines failed')   # Comment out for automation
        pass

    try:
        del mr
    except:
        print('Deleting mr failed') # Comment out for automation
        pass

try:
    del heads
except:
    print('Deleting heads failed') # Comment out for automation
    pass

print(scratch + ' machines deleted')    #debug
sys.exit()
