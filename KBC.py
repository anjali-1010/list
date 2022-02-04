print("WELCOME TO KBC")
quetion=[["Q1.How many containaint are there","Q2. What is tha capital of india","Q3. Navgurukul me kon kon se course padhae jate hai"]]
option=[["1.Saven","2.Four","3.Eight","4.Nine"],["1.Jaipur","2.Bhopal","3.Bangluru","4.New delhi"],["1.Software Engineering","2.Counsling","3.Turism","4.Agriculture"]]
Answer=[["2","4","1"]]
i=0
while i<len(quetion):
    print(quetion[i][0])
    j=0
    while j<len(option):
        print(option[i])
        user=input("Enter your answer")
        print(option[i][1])
        if user==Answer[i][j]:
            print("your Answer is........right")
            print(quetion[i][1])
            user2=input("Enter your Answer")
            user==Answer[i]
            print("your answer is.........right")
            print(quetion[i][2])
            user3=input("enter your answer")
            user==Answer[i]
        elif user!=Answer[i][j]:
            print("your Anser is........Wrong")
            break
        print("thanks for play")
        break
    j=j+3
i+=1