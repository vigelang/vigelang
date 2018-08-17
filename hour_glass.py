a=input("enter the number: ")
for i in range((-a+1),0):
    print ((a+i)*' '+((-i)*'*')+(((-i)+1)*'*'))
for i in range(0,a):
    print ((a-i)*' '+((i)*'*')+((i+1)*'*'))

