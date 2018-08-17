import re
a=raw_input("enter the Mac address :")
#a='A0:11:22:33:45:66'
valid_mac = re.search('(([0-9a-fA-F])+(:|-)){5}([0-9a-fA-F])+',a)
if valid_mac:
    unicast = re.match('([0-9a-fA-F]+):',a)
    binary_format = bin(int(unicast.group(1),16))
    multicast = re.search('([0]$)',binary_format)
    if multicast:
        print("Unicast address")
    else:
        print("Multicast address")
else:
    print("Not a valid MAC address")
