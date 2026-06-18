#input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operator (Add/Sub/Mul/Div): ")

#operation & printing result
if operation == "Add":
    print("Result = ",num1+num2)
elif operation == "Sub":
    print("Result = ",num1-num2)
elif operation == "Mul":
    print("Result = ",num1*num2)
elif operation == "Div":
    if num2 != 0:
        print("Result = ",num1/num2)
    else:
        print("Division by zero error")
else:
    print("Invalid operator!")
