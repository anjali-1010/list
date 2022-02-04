i=0
a=[]
while i<=4:
    b=input("enter a method")
    if b=="append":
        c=int(input("enter a number"))
        a.append(int(c))
    elif b=="insert":
        index=int(input("enter a index number"))
        n=int(input("inter a number"))
        a.insert(index,n)
    elif b=="reverse":
        a.reverse()
    elif b=="pop":
        a.pop()
    elif b=="sort":
        a.sort()
    print(a)
    i=i+1