# Password Checker

pwd = "Nidhi@10"

attempts = 1

while attempts <= 3:
    user = input("Enter password: ")
    
    if user == pwd:
        print("Access granted!")
        break
    else :
        if attempts < 3:
            print("Wrong password! try again.\n")
        attempts+=1    
else:
    print("Too many attempts! Access denied.")