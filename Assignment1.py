# Dictionary, Tuple and List Data Structures
# and different operations on them

# Dictionary
print("DICTIONARY OPERATIONS")

student = {"Name": "Khadija", "Age": 18, "Course": "CSE"}

print("Original Dictionary:", student)

# Adding an item
student["City"] = "Nagpur"
print("After Adding:", student)

# Updating an item
student["Age"] = 19
print("After Updating:", student)

# Deleting an item
del student["City"]
print("After Deleting:", student)

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())


# Tuple
print("\nTUPLE OPERATIONS")

numbers = (10, 20, 30, 40, 50)

print("Original Tuple:", numbers)
print("Length:", len(numbers))
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])
print("Count of 20:", numbers.count(20))
print("Index of 30:", numbers.index(30))


# List
print("\nLIST OPERATIONS")

fruits = ["Apple", "Banana", "Mango"]

print("Original List:", fruits)

# Adding an item
fruits.append("Orange")
print("After Append:", fruits)

# Inserting an item
fruits.insert(1, "Grapes")
print("After Insert:", fruits)

# Removing an item
fruits.remove("Banana")
print("After Remove:", fruits)

# Sorting the list
fruits.sort()
print("After Sorting:", fruits)

# Reversing the list
fruits.reverse()
print("After Reversing:", fruits)