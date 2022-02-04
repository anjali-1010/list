list1 = [2, -7, 5, -64, -14]
i=0
count1=0
count2=0
while i<len(list1):
    if list1[i]>0:
        count1=count1+1
    elif list1[i]<0:
        count2=count2+1
    i=i+1
print("posetive",count1)
print("negative",count2)
