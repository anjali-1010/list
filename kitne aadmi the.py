elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
l=[]
k=[]
while i<len(elements):
    if elements[i]%2==0:
        l.append(elements[i])

    else:
        k.append(elements[i])
    i=i+1
print("even number=",l)
print("odd number=",k)
