a=[2,4,10,2,5,10,4,11]
n=[]
i=0
while i<len(a):
    if a[i] not in n:
        n.append(a[i])
    i=i+1
print(n)