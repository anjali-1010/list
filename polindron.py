name=[ 'n', 'i', 't', 'i', 'n' ]
i=-1
b=[]
while i>=(-len(name)):
    b.append(name[i])
    i=i-1
if b==name:
    print("han palindrom hai")
else:
    print("nahi,polindrom nahi hai")