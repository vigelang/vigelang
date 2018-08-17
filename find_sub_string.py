import re
a=raw_input("enter the string : ")
b=raw_input("String to be found : ")
c=re.findall(b,a)
print(len(c))

________________________

a=raw_input("enter the string : ")
b=raw_input("String to be found : ")
c=0
for i in range(len(a)):
    if b in a:
        a=a.replace(b,'',1)
        c+=1
    if b not in a:
        print("b not in a")
print(c) 
