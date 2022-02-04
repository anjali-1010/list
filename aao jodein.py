elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
s1=0
s2=0
l=[]
k=[]
while i<len(elements):
    if elements[i]%2==0:
        l.append(elements[i])
        s1=s1+elements[i]
    else:
        k.append(elements[i])
        s2=s2+elements[i]
    i=i+1
print("sum of even number=",l)
print("sum of odd number=",k)
print("even sum=",s1)
print("odd sum=",s2)
