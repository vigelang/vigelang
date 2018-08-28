Number_of_lines=input("enter the number of lines: ")
if Number_of_lines == 0 or Number_of_lines == 1:
    print("Cant print the Hourglass from the given number of lines")
else:
    a=Number_of_lines
    for i in range((-a+1),0):
        print ((a+i)*' '+((-i)*'*')+(((-i)+1)*'*'))
    for i in range(0,a):
        print ((a-i)*' '+((i)*'*')+((i+1)*'*'))

