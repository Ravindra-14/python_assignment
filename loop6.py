s='Pentagon Space'
l=len(s)
s1=""
i=0
while(i<l):
    if (s[i]  not in s1):
        s1=s1+s[i]
    i=i+1
print(s1)
