import re
a=raw_input("enter the link :")
#a="https://www.google.com/search"
protocol=re.match('(http|https)://([\S]+)/([\S]+)',a)
print("protocol:",protocol.group(1))
print("path:",protocol.group(3))
c=re.search('([0-9]+){4}',protocol.group(2))
if c:
  print('Port :' , c.group())
  print('ip:',re.search('([\d]+.){3}[\d]+',protocol.group(2)).group())
else : 
  print("IP:",protocol.group(2))
