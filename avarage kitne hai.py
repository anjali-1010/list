elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
s1=0
s2=0
c=0
l=[]
k=[]
while i<len(elements):
    if elements[i]%2==0:
        s1=s1+elements[i]
        c=c+1
        avg=s1/c
    else:
        k.append(elements[i])
        s2=s2+elements[i]
        c=c+1
        avg2=s2/c
    i=i+1
print("avrage of even =",avg)
print("avrage of odd =",avg2)
