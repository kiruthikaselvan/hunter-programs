str1,str2=input(),input()
if str2 in str1 and len(str2)<len(str1):
    print(str1.index(str2))
else:
    print("-1")
