import re
a=raw_input("enter the IP address :")
ipv6=[]
valid_ip= re.search('(([2][5][0-5]\.)|([2][0-4][0-9]\.)|([0-1]?[0-9]?[0-9]\.)){3}(([2][5][0-5])|([2][0-4][0-9])|([0-1]?[0-9]?[0-9]))$',a)
if valid_ip:
    ip_type = re.match('([\d]+).([\d]+).([\d]+).([\d]+)',a)
    octet = [int(ip_type.group(1)),int(ip_type.group(2)),int(ip_type.group(3)),int(ip_type.group(4))]
    #converting IP to IPV6
    for i in range(0,4):#(range represents 4 octets)
        reminder=octet[i] % 16
        quotient=int(octet[i] / 16)
        ipv6.append(str(hex(quotient)) + str(hex(reminder)))
        print(hex(quotient))
        print(reminder)
#IPV6 Address format(2002:C0A8:6301::1/64)
print(" IPV6 Address is :" , "2002:"+str(ipv6[0])+str(ipv6[1])+":"+str(ipv6[2])+str(ipv6[3])+"::1/64")

