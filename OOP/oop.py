#OOP Practice

class Student:
    def __init__(self,name,age,course):
        self.name = name 
        self.age = age
        self.course = course
    
    def display_info(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Course:",self.course)

    def greet(self):
        print(f"\nHello,I am {self.name}.")

# Creating Objects
student1 = Student("Nidhi",19,"B.Tech-IT")
student2 = Student("Neha",21,"BCA")

#Calling methods
student1.display_info()
student1.greet()

print()

student2.display_info()
student2.greet()



print("\nBooks: ")

class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def display_book(self):
        print("\nTitle:",self.title)
        print("Author:",self.author)
        print("Price:",self.price)

book1 = Book("Fourth Wing","Rebecca Yarros",499)
book2 = Book("Silent Patient","Alex Michaelides",399)

book1.display_book()
book2.display_book()