#!/usr/bin/env python3
import ipaddress

#ipchk= '192.168.0.1'
ipchk= input('Apply an IP address: ')

try:
    ipaddress.ip_address(ipchk)

    if ipchk == '192.168.20.1':
        print('looks like the IP address of the gateway was set: '+ipchk +'this is not recommended')
    else:
        print('looks like the IP address was set: '+ipchk)
#    else:
#        print('You did not provide input.')

except:
    print("That doesnt appear to be a valid IP address")

