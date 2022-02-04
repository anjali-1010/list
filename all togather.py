from locale import ABMON_10


elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
a=0
even=0
b=0
odd=0
s=0
count=0
i=0
while i<len(elements):
    count=count+1
    s=s+1
    avr_total=s//count
    if elements[i]%2==0:
        even=even+elements[i]
        a=a+1
        avr_even=even//a
    else:
        odd=odd+elements[i]
        b=b+1
        avr_odd=odd/b
    i=i+1
print("even ka count",a)
print("odd ka count",b)
print("saare number ka count",count)
print("even ka sum",a)
print("odd ka sum",b)
print("saare number a sum",s)
print("even ka avrage",avr_even)
print("odd ka avrage",avr_odd)
print("saare ka avrage",avr_total)

