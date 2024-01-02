a=[]
for i in range(4):
    a.append(int(input(" ")))
b=a[0]*a[1]
c=a[2]*a[3]
if b%c==0:
    print(b//c)
else:
    print(b//c +1)

