#Functions Practice

#function without parameter
def greet():
    print("Hello,Nidhi!")

greet()

#function with parameter
def greet(name):
    print("Hello,",name)

greet("Nidhi")

#function that returns a value
def add(a,b):
    return a+b

result = add(10,20)
print("Sum =",result)

#function to find a square
def square(num):
    return num*num

print("Square =",square(5))

#function with multiple parameters
def student(name,age,course):
    print("\nStudent information")
    print("Name:",name)
    print("Age:",age)
    print("Course:",course)

student("Nidhi Pandey",19,"B.Tech-IT")