a="thearaphy"
b="weather"
d=list(a)
e=list(b)
i=0
c=[]
while i<len(d):
    if d[i] in e:
        if d[i]not in c:
            c.append(d[i])
    i=i+1
print(c)
