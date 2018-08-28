from requests import get

def show_json(ip):
    json_format = get('http://ip-api.com/json/'+str(ip))
    return json_format.text

ip=raw_input("enter the ip address : ")
print(show_json(ip))
