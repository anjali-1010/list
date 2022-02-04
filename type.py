a=[]
i=0
while i<=4:
    b=int(input("enter a number"))
    if b==type(int):
        a.append(b)
    elif b==type(str):
        a.append(b)
    elif b==type(float):
        a.append(b)
    i=i+1
print(a)
