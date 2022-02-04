list=[1,2,3,4,5,6,7]
i=1
j=0
a=[]
while i<len(list):
    d=list[i]-list[j]
    a.append(d)
    i=i+1
    j=j+1
print(a)


