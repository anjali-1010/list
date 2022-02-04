a=[1, 1, 2, 3, 4, 4, 5, 1]
i=0
b=[]
while i<len(a):
    c=0
    j=0
    d=[]
    while j<len(a):
        if a[j]==a[i]:
            c+=1
            d.append(c)
            d.append(a[i])
        
        j+=1
    print(d)
    i=i+1
# print()



# from itertools import groupby
# def modified_encode(alist):
#         def ctr_ele(el):
#             if len(el)>1: return [len(el), el[0]]
#             else: return el[0]
#         return [ctr_ele(list(group)) for key, group in groupby(alist)]

# n_list = [1,1,2,3,4,4,5, 1]
# print("Original list:") 
# print(n_list)
# print("\nList reflecting the modified run-length encoding from the said list:")
# print(modified_encode(n_list))

# n_list = 'aabcddddadnss'
# print("\nOriginal String:") 
# print(n_list)
# print("\nList reflecting the modified run-length encoding from the said string:")
# print(modified_encode(n_list))

