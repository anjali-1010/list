# num1=input("enter a number")
# num=str(num1)
# str=' '
# for i in num1:
# 	if i=='1':
# 		str=str+'one'	
# 	if i=='2':
# 		str=str+'two'
# 	if i=='3':
# 		str=str+'three'
# 	if i=='4':
# 		str=str+'four'
# if i=='5':
#     str=str+'five'
#     if i=='6':
#         str=str+'six'
#     if i=='7':
#         str=str+'sevan'
#     if i=='8':
#         str=str+'Eight'
#     if i=='9':
#         str=str+'nine'
#     if i=='0':
#         str=str+'zero'
#         str+=' '
# print(str)

num1=input("enter a number")
num=str(num1)
i=0
a=[]
while i<len(num):
    j=0
    while j<len(num[i]):
        if num[i]=="1":
            w="one"	
        if num[i]=="2":
            w="two"
        if num[i]=="3":
            w="three"
        if num[i]=="4":
            w="four"
        if num[i]=="5":
            w="five"
        if num[i]=="6":
            w="six"
        if num[i]=="7":
            w="sevan"
        if num[i]=="8":
            w="Eight"
        if num[i]=="9":
            w="nine"
        if num[i]=="0":
            w="zero"
        j=j+1
    a.append(w)
    i=i+1
print(a)