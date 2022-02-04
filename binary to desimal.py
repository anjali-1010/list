# print("Enter the Binary Number: ")
# bnum = int(input())
binary_number = [1, 0, 0, 1, 1, 0, 1, 1]
dnum = 0
i = 1
s=0
while i<len(binary_number):
    rem = i%10
    dnum = i+ (rem*i)
    s=s+dnum
    i = i*2
    bnum = int(i/10)

print("\nEquivalent Decimal Value = ", s)