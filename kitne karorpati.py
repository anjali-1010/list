kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
a=0
b=0
c=0
while i<len(kitna_paisa_hai):
    if kitna_paisa_hai[i]>=10000000:
        a=a+1
    elif kitna_paisa_hai[i]<10000000 and kitna_paisa_hai[i]>=100000:
        b=b+1
    else:
        c=c+1
    i=i+1
print("carorpati",a)
print("lakhpati",b)
print("dilwale",c)
