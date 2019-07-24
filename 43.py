import re
str,ns=input(),""
res1 =re.findall("[a-zA-Z]+",str)
res2 =re.findall("[0-9]+",str)
for i in range(len(res2)):
    if int(res2[i])%2==0:
        ns=ns+res1[i]*int(res2[i])
    else:
        ns=ns+res1[i]+res2[i]
print(ns)
        
