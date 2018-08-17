#b=big
#s=second big
a=[2,4,7,4,22,45,67,88,26,76,89,55]
if a[0]>a[1]:
    b=a[0]
    s=a[1]
else:
    s=a[0]
    b=a[1]
for i in range(2,len(a)):
    if a[i]>b:
        s=b
        b=a[i]
    elif a[i]>s:
        s=a[i]

print(s)
