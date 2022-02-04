list1=[[10, 20], [30, 40], [50, 60], [30, 20, 80]]
list2=[[61], [12, 14, 15], [12, 13, 19, 20], [12]]
i=0
a=[]
while i<len(list1):
    a.append(list1[i]+list2[i])
    i=i+1
print(a)