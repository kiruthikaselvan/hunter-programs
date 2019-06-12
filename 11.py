string=input()
r=[]
l=string.split()
#print(l)
for i in l:
    r.append(i[::-1])
#print(r)
print(" ".join(r))
