# Age Calculator

birth_yr = int(input("Enter your birth year: "))
current_yr = int(input("Enter current year: "))

if birth_yr > 0 and current_yr >= birth_yr:
    age = current_yr - birth_yr
    print(f"You are {age} years old.")
    #Voting Eligibility
    if age >= 18:
        print("You are eligible to vote!")
    else:
        print("You are not eligible for voting!")
else:
    print("Invalid year!!")

