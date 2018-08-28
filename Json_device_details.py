##1

import re
import time
import datetime
import pexpect
import sys
device_details={}
class ConnectionRefuse(Exception):
    """
    Exceptions for not connecting to device.
    """
    pass

def device_class(x,y):
    tel = 'telnet'+' '+x+' '+y
    try:
        device = pexpect.spawn(tel)
        device.logfile = sys.stdout
    except ConnectionRefuse as e:
        print(e.message)
    device.sendline('C_LOGON "xena"')
    result = device.expect("<OK>")
    device.sendline('C_INFO ?')
    result = device.expect('C_TKSVCSTATE')
    c=device.before
    mac=(re.search('C_MACADDRESS +([\S]+)',c)).group(1)
    model=(re.search('C_MODEL +([\S]+)',c)).group(1)
    serial=(re.search('C_SERIALNO +([\d\s]+)',c)).group(1)
    version_1=(re.search('C_VERSIONNO +([\d\s]+)',c)).group(1)
    version_minor=(re.search('C_VERSIONNO_MINOR +([\s\d]+[\d])',c)).group(1)
    version=(version_1+version_minor).replace(' ','.')
    reserved_by=(re.search('C_RESERVEDBY +([\S]+)',c)).group(1)
    if reserved_by.isalpha():
        reserved_by = reserved_by
    else:
        reserved_by = 'none'
    day = str(datetime.datetime.now().strftime("%A"))
    month = str(datetime.datetime.now().strftime("%B"))
    date = str(datetime.datetime.now().day)
    year = str(datetime.datetime.now().year)
    date_1 = day+','+ month +' '+date+','+year
    port_list=[]
    for i in range(0,6):
        port = '0/'+str(i)
        port_cli = '0/'+str(i)+' P_INFO ?'
        device.sendline(port_cli)
        device.expect("P_LPSUPPORT")
        c = device.before
        rsvd_by = (re.search(port+'  P_RESERVEDBY +([\S]+)',c)).group(1)
        if rsvd_by.isalpha():
            rsvd_by = reserved_by
        else:
            rsvd_by = 'none'
        interface = (re.search(port+'  P_INTERFACE +("+[\s\S]+")',c)).group(1)
        speed = (re.search(port+'  P_SPEED +([\S]+)',c)).group(1)
        speed = str(int(speed)/1000)+' Gbps'
        status = (re.search(port+'  P_STATUS +([\S]+)',c)).group(1)
        if status == '1':
            status = "up"
        if status == '-1':
            status = "down"
        capture = (re.search(port+'  P_CAPTURE +([\S]+)',c)).group(1)
        traffic = (re.search(port+'  P_TRAFFIC +([\S]+)',c)).group(1)
        port_list.append({"name": port,"reserved_by": rsvd_by,"interface" : interface,"speed" : speed,"status" : status,"capture" : capture,"traffic" : traffic})

##json_format
    device_details={"ip" : ip_1,"mac" : mac,"model" : model,"serial" : serial,"version" : version,"reserved_by": reserved_by,"date" : date_1,"ports":port_list}
    device.write('C_LOGOFF\n')
    return device_details

ip_1='192.168.10.28'
port_id='22611'
tel = 'telnet'+' '+ip_1+' '+port_id
a=device_class(ip_1,port_id)
print(a)


