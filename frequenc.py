# test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
# k=3
# i=0
# b=[]
# while i<len(test_list):
#     freq=test_list.count(i)
#     if freq > k and i not in b:
#         b.append(i)
#     i=i+1
# print(b)


test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
# print("The original list : " + str(test_list))
K = 2
res = [] 
for i in test_list:
    freq = test_list.count(i) 
    if freq > K and i not in res: 
        res.append(i)
print("The required elements : ",res)