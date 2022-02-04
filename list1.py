list1=[1,2,3,[4,5],6,7,[8,9],10]
i=0
s=0
a=[]
while i<len(list1):
    if type(list1[i])==list:
        j=0
        while j <len(list1[i]):
            s=s+list1[i][j]
        
            a.append(s)
        j+=1
    i+=1
print(a)

    # else:
    #     s=s+list1[i]
        


    # # while j<=(list1[i]):
    #     k=0
    #     while k<len(list1[i][j]):
    #         s+=list1[i][j]
    #         a.append(s)
    #         k=k+1
#     #     j=j+1
#     i=i+1
# print(a)
        
