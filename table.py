n=int(input("enter a number"))
i=1
b=[]
while i<=n:
    j=1
    d=[]
    while j<=10:
        x=i*j
        d.append(x)
        j=j+1
    b.append(i)
    b.append(d)
    i=i+1
print(b)