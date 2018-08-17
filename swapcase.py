a=raw_input("enter the string : ")
b=""
for i in a:
    if i.isalpha():
        if i.isupper():
            i=i.lower()
         
        else:
            i=i.upper()
        b=b+i
    else:
        b=b+i
print(b)
