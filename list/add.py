a=[1,2,3,4,5,6,7]
b=[1,2,3,4,5]
z=[]
k=zip(a,b)
print(k)
for i,j in k:
    z.append(i+j)
print(z)     