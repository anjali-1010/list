list1=['0', '1', '2', '3', '4']
list2=['red', 'green', 'black', 'blue', 'white']
list3=['100', '200', '300', '400', '500']
i=0
j=0
k=0
b=[]
while i<len(list1):
    while j<len(list2):
        while k<len(list3):
            s=list1[i]+list2[j]+list3[k]
            b.append(s)
            i=i+1
            j=j+1
            k=k+1
print(b)




# second method
# second method
# second method
# second method




# list1=['0', '1', '2', '3', '4']
# list2=['red', 'green', 'black', 'blue', 'white']
# list3=['100', '200', '300', '400', '500']
# i=0
# b=[]
# while i<len(list1):
#     while i<len(list2):
#         while i<len(list3):
#             sum=list1[i]+list2[i]+list3[i]
#             b.append(sum)
#             i=i+1
# print(b)