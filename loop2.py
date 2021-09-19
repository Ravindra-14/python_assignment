s='Pentagon Space'
l=len(s)
s1=""
s2=""
for i in range(l):
    if(i<5):
        s1=s[i]+s1
    else:
        s2=s2+s[i]
s1=s1+s2
print(s1)
