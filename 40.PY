n,sum=int(input()),0
for i in str(n):
    sum=sum+int(i)
#print(sum)
a=str(sum)
if str(sum)==a[::-1]:
    print("YES")
else:
    print("NO")
    
