def erat(n):
    if type(n)!= int:
        print("Wrong input!")
    else:
         x=[1]*(n+1)
         x[0]=x[1]=0
    
         for j in range(2,int(n//2)+1):
            if x[j]==1:
                for i in range(j*j,n+1,j):
                   x[i]=0
    p=[j for j in range(2,n+1) if x[j]==1]
    return p
n=int(input(" "))
j=erat(n)
print(j)