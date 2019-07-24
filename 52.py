a,b,n=0,1,int(input())
for i in range(n):
    c=a+b
    a,b=b,c
print(c)
