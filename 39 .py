list=[[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
a=[]
i=0
while i<len(list):
    j=0
    sum=0
    count=0
    while j<len(list[i]):
        sum+=list[i][j]
        count+=1
        avg=sum/count
        a.append(avg)
        j=j+1
    i=i+1
print(a)

