n=int(input("enter a numbr"))
# a=str(n)
i=0
while i<(n):
    x=n%10
    n=n//10
    m=x**2
    i=i+1
    print(m,end="")
