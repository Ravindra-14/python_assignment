age_list=[12,9,6,31,22,40,78,88,76]
g=[]
g1=[]
g2=[]

for i in age_list:
    if i<18:
        g.append(i)
    elif(i>18 and i<60):
        g1.append(i)
    else:
        g2.append(i)
print(g)
print(g1)
print(g2)
