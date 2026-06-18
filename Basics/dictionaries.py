#Dictionaries Practice

student = {
    "name": "Nidhi Pandey",
    "age": 19,
    "course": "B.Tech IT"
}

print("\nStudent Dictionary:",student)

#Accessing Values
print("Name:",student["name"])
print("Age:",student["age"]
)

#Adding new key value pair
student["city"]="Mumbai"
print("\nAfter adding:",student)

#Updating values
student["age"] = 20
print("\nAfter updating:",student)


#Removing key value pair
student.pop("city")
print("\nAfter removing:",student)