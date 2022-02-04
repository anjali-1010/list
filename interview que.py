list=[1,2,3,3,4,5,6,7,8,9,10]
i=0
while i<len(list):
    j=0
    b=[]
    a=0
    while j<len(list)-1:
        a=[list[i],list[j+1]]
        j=j+1
        b.append(a)
        j=j+1
    i=i+1
print(b)