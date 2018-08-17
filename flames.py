a=raw_input("enter the first string : ")
b=raw_input("enter the second string : ")
dict={'f':'Friends','l':'Loves','a':'Affection','m':'Marriage','e':'Enemy','s':'Sister'}
for i in a:
    if i in b:
        a=a.replace(i,'',1) 
        b=b.replace(i,'',1)     
c=len(a) + len(b)
d="flames"
e=d
for i in range(0,(2*c)): ##Iteration count is unknown since used 2*c iterations  
    if len(d) <= c:
        d=d+d
    if len(d) > c:
        e=e.replace(d[c-1],'')
        d=e
    if len(e)==1:
        break
print(dict[e])
