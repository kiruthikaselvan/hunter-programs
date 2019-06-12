n=int(input())
li=list(map(int,input().split()))
for i in range(len(li)-1,-1,-1):
    if i!=0:
        print(li[i],end="->")
    else:
        print(li[i])
