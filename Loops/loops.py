#Loops Practice

#for loop
print("Numbers from 1 to 5:")
for i in range(1,6):
    print(i)

#while loop
print("\nwhile loop:")
count = 1
while count<=5:
    print(count)
    count+=1

#Sum of numbers
total = 0

for num in range(1,6):
    total+=num

print("\nSum = ",total)

#Multiplication table

num = 5
print("\nMultiplication table of",num)

for i in range(1,11):
    table = num*i
    print(f"{num} * {i} = {table}")
