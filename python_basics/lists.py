# Python Lists

fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Fruits:", fruits)

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

fruits.append("Grapes")
print("After adding a fruit:", fruits)

fruits.remove("Banana")
print("After removing a fruit:", fruits)

print("All fruits:")
for fruit in fruits:
    print(fruit)
