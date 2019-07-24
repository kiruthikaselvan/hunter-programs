n,count=int(input()),0
l=list(map(int,input().split()))
for i in range(n):
    if n*i in l:
        count=count+1
print(count)
