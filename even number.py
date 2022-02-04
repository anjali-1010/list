a=[2,3,4,5,6,7,3,5,8,8]
even=[]
odd=[]
i=0
while i<len(a):
    if a[i]%2==0:
        even.append(a[i])
    else:
        odd.append(a[i])
    i=i+1
print("even number=",even)
print("odd number=",odd)