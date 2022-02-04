n=int(input("enter a number"))
a=str(n)
i=10**(len(a)-1)
b=""
while i>0:
    if (n//i)* i!=0:
        b=b+str((n//i)*i)+"+"
        n=n%i
    i//=10
print(b[0:len(b)-1])