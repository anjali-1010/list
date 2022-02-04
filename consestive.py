list=[4, 5, 5, 5, 3, 8]
k=3
i=0
a=[]
while i<len(list):
    j=0
    c=0
    while j<len(list):
        if list[j]==list[i]:
            c=c+1
        j=j+1
    if c==k:
        if list[i] not in a:
            a.append(list[i])
    i=i+1
print(a)
