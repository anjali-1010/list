colore_list=['Red', 'Maroon', 'Yellow', 'Olive']
i=0
b=[]
c=[]
while i<len(colore_list):
    j=0
    a=list(colore_list[i])
    while j<len(colore_list[i][j]):
        b.append(a)
        j=j+1
    i=i+1
print(b)