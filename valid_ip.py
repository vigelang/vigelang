import re
a=raw_input("enter the IP address :")
valid_ip= re.search('(([2][5][0-5]\.)|([2][0-4][0-9]\.)|([0-1]?[0-9]?[0-9]\.)){3}(([2][5][0-5])|([2][0-4][0-9])|([0-1]?[0-9]?[0-9]))$',a)
if valid_ip:
    ip_type = re.match('([\d]+).([\d]+).([\d]+).([\d]+)',a)
    #changing ip_type from string to integer
    last_block = int(ip_type.group(4))
    First_block = int(ip_type.group(1))
    #Finding class and IP type
    if last_block in range(1,255) and First_block in range(1,127):
        print("class-A-Unicast address")
    if last_block in range(1,255) and First_block in range(128,192):
        print("class-B-Unicast address")
    if last_block in range(1,255) and First_block in range(192,224):
        print("class-C-Unicast address")
    if last_block in range(1,255) and First_block in range(224,240):
        print("class-D-Multicast address range")
    if last_block in range(1,255) and First_block in range(240,256):
        print("class-E-Unicast address")
    if last_block == 255:
        print("broadcast IP address")
    if last_block == 0:
        print("Network address")
    if First_block == 127:
        print("Loopback's IP address")
else:
    print("Not a valid IP address")
