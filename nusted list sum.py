# t=[1,2,3,4,[5,6,[7,8,[9,[10,[11,[35,36,37,38,39,40,41,42]]]]]]]
# x=t[4][2][2][1][1][1]
# print(x)
# i=0
# even=[]
# odd=[]
# while i<len(x):
#     if x[i]%2==0:
#         even.append(x[i])
#     else:
#         odd.append(x[i])
#     i=i+1
# print("even number =",even)
# print("odd number=",odd)


t=[1,2,3,4,[5,6,[7,8,[9,[10,[11,[35,36,37,38,39,40,41,42]]]]]]]
x=t[4][2][2][1][1][1]
i=0
even=[]
odd=[]
s1=0
s2=0
total_sum=0
while i<len(x):
    total_sum=total_sum+x[i]
    if x[i]%2==0:
        even.append(x[i])
        s1=s1+x[i]
    else:
        odd.append(x[i])
        s2=s2+x[i]
    i=i+1

# print("sum of numted_list=",s3)
print("even number =",even)
print("odd number =",odd)
print("total_sum =",total_sum)
print("sum of even number =",s1)
print("sum of odd number =",s2)

