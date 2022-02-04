numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
m=0
while i<len(numbers):
    if m<numbers[i]:
        m=numbers[i]
    i=i+1
print(m)
