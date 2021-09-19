s='Pentagon Space'
l=len(s)
s1=''
s2=''
i=0
while(i<l):
    if(i<5):
        s1=s[i]+s1
    else:
        s2=s2+s[i] 
    i=i+1
print(s1+s2)
