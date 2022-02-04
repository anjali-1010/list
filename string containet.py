santance="https://www.w3resource.com/python-exercises/list/"
list=["com","edu","tv"]
i=0
while i<len(list):
    if list[i] in santance:
        print("True")
    else:
        print("False")
    i=i+1