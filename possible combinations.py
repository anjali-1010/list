list=[1, 2, 3]
i=0
while i< len(list):
    j=0
    while j<len(list):
        k=0
        while k<len(list):
            if i!=j and j!=k and i!=k:
                print(list[i],list[j],list[k])
            k=k+1
        j=j+1
    i=i+1