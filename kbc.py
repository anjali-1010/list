print("WELCOME TO KBC")
# name=(input("ENTER YOUR NAME "))
# print("WELCOME TO KBC",name)
ans=input("Are you ready to play(yes/no)")
quetion=[["Q1.How many containaint are there","Q2. What is tha capital of india","Q3. Navgurukul me kon kon se course padhae jate hai"]]
option=[["1.Saven","2.Four","3.Eight","4.Nine"],["1.Jaipur","2.Bhopal","3.Bangluru","4.New delhi"],["1.Software Engineering","2.Counsling","3.Turism","4.Agriculture"]]
Answer=["1","4","1"]
print(Answer[0])
if ans=="yes":
    i=0
    while i<len(quetion):
        j=0
        while j<len(option):
            print(quetion[i][0])
            print(option[0])
            user=input("Enter your answer")
            if user==Answer[0]:
                print("your Answer is........right")
                print(quetion[i][1])
                print(option[1])
                user2=input("Enter your Answer")
                if user2==Answer[1]:
                    print("your answer is.........right")
                    print(quetion[i][2])
                    print(option[2])
                    user3=input("enter your answer")
                    if user3==Answer[2]:
                        print("your answer is.........right")
                        print("congradulations you win")
                        break
                    else:
                        print("your Anser is........Wrong")
                        break
                else:
                    print("your Anser is........Wrong")
                    break
            else: 
                print("your Anser is........Wrong")
                print("thanks for play")
                break
            j=j+1
        i+=1
else:
    print("DON'T MIND ,TAKE YOUR TIME")