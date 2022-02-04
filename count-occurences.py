char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
b=[]
c=0
while i<len(char_list):
    if char_list[i] not in b:
        b.append(char_list[i])
        j=0
        count=0
        while j<len(char_list):
            if b[c]==char_list[j]:
                count=count+1
            j=j+1
        print(char_list[i],count,"time")
        c=c+1
    i=i+1