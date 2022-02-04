# list=[56,34,67,23,45,6,7,33,70,25,55,45]
# first_max=0
# second_max=0
# third_max=0
# i=0
# while i<len(list):
#     if first_max<list[i]:
#         first_max=list[i]
        
#     elif  second_max<list[i]:
#         second_max=list[i]

#     elif third_max<list[i]:
#         third_max=second_max
#     i=i+1
# print(first_max,second_max,third_max)


list=[56,34,67,23,45,6,7,33,70,25,55,45,100,45,89]
first_max=0
second_max=0
third_max=0
i=0
while i<len(list):
    if first_max<list[i]:
        first_max=list[i]
    i=i+1
    j=0
    while j<len(list):
        if list[j]<first_max and second_max<list[j]:
            second_max=list[j]
        j=j+1
        k=0
        while k<len(list):
            if list[k]<second_max and third_max<list[k]:
                third_max=list[k]
            k=k+1
print(first_max,second_max,third_max)
