number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
i=0
l=[]
while i<len(n):
    j=0
    while j<len(n):
        if n[i]+n[j]==number:
            b=n[i],n[j]
            l.append(b)
        j=j+1
    i=i+1
print(l)