a=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
i=0
x=0
f=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if len(a[i])>x:
            x=len(a[i])
        b=a[i]
        j=j+1
    i=i+1
print(b)