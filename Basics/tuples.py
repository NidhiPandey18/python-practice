#Tuples Practice

empyrean_series = ("Fourth Wing","Iron Flame","Onyx Storm")
print("First book in series:",empyrean_series[0])
print("Total books in series:",len(empyrean_series))

#Loop through tuples
print("\nNames:")
for book in empyrean_series:
    print(book)

# Tuple unpacking
a, b, c = empyrean_series

print("\nTuple Unpacking:")
print("a =", a)
print("b =", b)
print("c =", c)    