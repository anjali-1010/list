list=[12,67,98,34]
i=0
b=[]
while i<len(list):
    j=1
    a=0
    s=0
    while list[i]>0:
        a=list[i]%10
        s=s+a
        list[i]=list[i]//10
    b.append(s)
    j=j+1
    i=i+1
print(b)