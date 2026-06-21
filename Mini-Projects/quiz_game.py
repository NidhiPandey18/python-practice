#Python Quiz Game

print("\n-----Welcome to Python Quiz!-----\n")

score = 0

ans1 = input(("Q1) What is capital of India? "))

if ans1.lower() == "delhi":
    print("Correct!!\n")
    score+=1
else:
    print("Wrong :(\n") 


ans2 = int(input(("Q2) What is 2+2 ? ")))

if ans2 == 4:
    print("Correct!!\n")
    score+=1
else:
    print("Wrong :( \n")


ans3 = int(input(("Q3) How many days are there in a leap year? ")))

if ans3 == 366:
    print("Correct!!\n")
    score+=1
else:
    print("Wrong :( \n")

print("FINAL SCORE : ",score,"/ 3")