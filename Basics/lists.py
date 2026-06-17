#Lists Practice

cricketers = ["Virat Kohli","Rohit Sharma","K.L.Rahul","M.S.Dhoni"]
print("Indian cricketers: ",cricketers)

print("First cricketer:",cricketers[0]) #accessing elements

cricketers.append("Jasprit Bumrah") #adding an element
print("After append: ",cricketers)

cricketers.remove("M.S.Dhoni") #removing an element
print("After removing: ",cricketers)

#loop through list
print("\nCricketers:")
for n in cricketers:
    print(n)