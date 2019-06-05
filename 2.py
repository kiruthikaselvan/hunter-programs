lim=int(input())
t=[]
l=list(map(int,input().split()))
l.sort(reverse=True)
if l[0]!=0:
    x=[t.append(str(i)) for i in l]
    print("".join(t))
else:
    print("0")
