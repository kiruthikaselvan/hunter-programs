str1,str2=input(),input()
if str2 in str1 and len(str1)<len(str2):
    print(str1.index(str2))
else:
    print("-1")
