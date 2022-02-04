magic_squre=[[8,3,4],[1,5,9],[6,7,2]]
i=0
r1=0
r2=0
r3=0
c1=0
c2=0
c3=0
d1=0
d2=0
while i<len(magic_squre):
    r1=r1+magic_squre[0][i]
    r2=r2+magic_squre[1][i]
    r3=r3+magic_squre[2][i]
    c1=c1+magic_squre[0][i]
    c2=c2+magic_squre[1][i]
    c3=c3+magic_squre[2][i]
    d1=d1+magic_squre[0][i]
    d2=d2+magic_squre[2][i]
    i=i+1
if r1==r2==r3==c1==c2==c3==d1==d2:
    print("magic_squre")
else:
    print("not magic_squre")
# i=0
# while i<len(magic_squre):
#     j=0
#     r=0
#     c=0
#     d=0
#     while j<len(magic_squre[i]):
#         r+magic_squre[i][j]
#         c+magic_squre[j][i]
#         # d+magic_squre[i][j]
#         j=j+1
#     i=i+1
#     print(r)
#     print(c)
# # print(d)