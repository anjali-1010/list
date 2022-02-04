list=['1', '2', '3', '4', '5', '6', '7', '8']
i=0
while i<len(list):
    j=0
    a=0
    b=[]
    while j<len(list)-1:
        a=list[j]+list[j+1]
        j=j+1
        b.append(a)
    i=i+1
print(b)