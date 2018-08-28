from requests import get

def public_ip(ip):
    pub_ip = get(ip)
    return pub_ip.text

input_ip = raw_input("enter the link to get public ip : ")
print(public_ip(input_ip))
