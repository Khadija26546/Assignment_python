# Q1. Print the following student details:
# Student Name, Address, Contact No, Mother Tongue,
# School Name, Year, Panel and Roll No.

print("Student Name: ABC")
print("Address: XYZ")
print("Contact No: 1234567890")
print("Mother Tongue: English")
print("School Name: ABC School")
print("Year: 2026")
print("Panel: B")
print("Roll No: 34")


# Q2. Modify Address, Contact No and Mother Tongue into
# multi-line comments so that they do not appear in output.

print("Student Name: ABC")

"""
Address: XYZ
Contact No: 1234567890
Mother Tongue: English
"""

print("School Name: ABC School")
print("Year: 2026")
print("Panel: B")
print("Roll No: 34")


# Q3. Accept Student Name, Roll Number and marks of 3 subjects.
# Calculate percentage and display highest and lowest marks.

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))

percentage = (m1 + m2 + m3) / 3

print("Student Name:", name)
print("Roll Number:", roll_no)
print("Percentage:", percentage)

marks = [m1, m2, m3]

print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))


# Q4. Check whether a number is positive, negative or zero.

num = float(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# Q5. Check whether a number is even or odd.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Q6. Accept two non-negative values and print True if
# they have the same last digit.

num1 = int(input("Enter first non-negative number: "))
num2 = int(input("Enter second non-negative number: "))

if num1 % 10 == num2 % 10:
    print(True)
else:
    print(False)


# Q7. Print numbers from 1 to 10 in a single row with one tab.

for i in range(1, 11):
    print(i, end="\t")


# Q8. Print even numbers from 23 to 57, each on a separate row.

for i in range(23, 58):
    if i % 2 == 0:
        print(i)


# Q9. Check whether a given number is prime or not.

num = int(input("Enter a number: "))

if num < 2:
    print("Not Prime")
else:
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not Prime")


# Q10. Print all prime numbers from 10 to 99.

for num in range(10, 100):
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)


# Q11. Find the sum of digits of a number.

num = int(input("Enter a number: "))

num = abs(num)
sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits = sum_digits + digit
    num = num // 10

print("Sum of digits:", sum_digits)


# Q12. Reverse a given number.

num = int(input("Enter a number: "))

sign = -1 if num < 0 else 1
num = abs(num)

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reverse:", sign * reverse)


# Q13. Check whether a given number is a palindrome.

num = int(input("Enter a number: "))

original = num
num = abs(num)

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if abs(original) == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


# Q14. Accept 5 numbers and display their cubes.

for i in range(5):
    num = int(input("Enter a number: "))
    print("Cube:", num ** 3)


# Q15. Find the prime factors of a number.

num = int(input("Enter a number: "))

print("Prime factors:")

factor = 2

while num > 1:
    while num % factor == 0:
        print(factor, end=" ")
        num = num // factor

    factor = factor + 1


# Q16. Print the given star pattern.

for i in range(1, 5):
    print("* " * i)


# Q17. Print the given star pattern.

for i in range(1, 5):
    print("* " * i)


# Mini Project 1. Ask the user how far they want to travel in miles.
# Less than 3 miles: bicycle
# More than 3 but less than 300 miles: motorcycle
# 300 miles or more: supercar

distance = float(input("How far do you want to travel (in miles)? "))

if distance < 3:
    print("Ride a bicycle")
elif distance < 300:
    print("Ride a motorcycle")
else:
    print("Drive a supercar")


# Mini Project 2. A hosting provider charges $0.51 per hour
# for one server. Calculate daily, weekly, monthly cost
# and number of days possible with $918.

hourly_cost = 0.51

daily_cost = hourly_cost * 24
weekly_cost = hourly_cost * 24 * 7
monthly_cost = hourly_cost * 24 * 30

days_with_918 = 918 / daily_cost

print("Cost per day: $", round(daily_cost, 2))
print("Cost per week: $", round(weekly_cost, 2))
print("Cost per month: $", round(monthly_cost, 2))
print("Days with $918:", round(days_with_918, 2))


# LIST Q1. Create a list of 5 integers, display the list
# and access individual elements using their index.

my_list = [10, 20, 30, 40, 50]

print("List:", my_list)
print("First element:", my_list[0])
print("Second element:", my_list[1])
print("Third element:", my_list[2])
print("Fourth element:", my_list[3])
print("Fifth element:", my_list[4])


# LIST Q2. Append a new item to a list.

my_list = [10, 20, 30, 40, 50]

my_list.append(60)

print(my_list)


# LIST Q3. Reverse a list.

my_list = [10, 20, 30, 40, 50]

my_list.reverse()

print(my_list)


# LIST Q4. Count the occurrences of a specified element.

my_list = [10, 20, 10, 30, 10, 40]

element = int(input("Enter element to count: "))

print("Occurrences:", my_list.count(element))


# LIST Q5. Append list1 to the front of list2.

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list2 = list1 + list2

print(list2)


# LIST Q6. Insert a new item before the second element.

my_list = [10, 20, 30, 40]

item = int(input("Enter new item: "))

my_list.insert(1, item)

print(my_list)


# LIST Q7. Remove an item from a specified index.

my_list = [10, 20, 30, 40, 50]

index = int(input("Enter index to remove: "))

if 0 <= index < len(my_list):
    my_list.pop(index)
    print(my_list)
else:
    print("Invalid index")


# LIST Q8. Remove the first occurrence of a specified element.

my_list = [10, 20, 30, 20, 40]

element = int(input("Enter element to remove: "))

if element in my_list:
    my_list.remove(element)
    print(my_list)
else:
    print("Element not found")


# LIST Q9. Accept 20 values.
# (a) Count similar elements and print their index values.
# (b) Count even and odd elements.
# (c) Count positive and negative elements.

my_list = []

for i in range(20):
    value = int(input("Enter value: "))
    my_list.append(value)

print("List:", my_list)

print("Similar elements and their indexes:")

checked = []

for value in my_list:
    if value not in checked:
        if my_list.count(value) > 1:
            indexes = []

            for i in range(len(my_list)):
                if my_list[i] == value:
                    indexes.append(i)

            print(value, ":", indexes)

        checked.append(value)

even = 0
odd = 0
positive = 0
negative = 0

for value in my_list:

    if value % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

    if value > 0:
        positive = positive + 1
    elif value < 0:
        negative = negative + 1

print("Even values:", even)
print("Odd values:", odd)
print("Positive values:", positive)
print("Negative values:", negative)


# LIST Q10. Accept 10 values.
# (a) Arrange in ascending order using sorted().
# (b) Arrange in descending order using sort().
# (c) Find the length of the list.

my_list = []

for i in range(10):
    value = int(input("Enter value: "))
    my_list.append(value)

print("Ascending order:", sorted(my_list))

my_list.sort(reverse=True)

print("Descending order:", my_list)
print("Length:", len(my_list))


# LIST Q11. Merge two lists using the + operator.

list1 = list(map(int, input(
    "Enter first list values separated by spaces: "
).split()))

list2 = list(map(int, input(
    "Enter second list values separated by spaces: "
).split()))

merged_list = list1 + list2

print("Merged list:", merged_list)


# LIST Q12. Create an acronym from a given phrase in uppercase.

phrase = input("Enter a phrase: ")

words = phrase.split()

acronym = ""

for word in words:
    acronym = acronym + word[0].upper()

print("Acronym:", acronym)


# LIST Q13. Display the abbreviation of a month using its number.

month = int(input("Enter month number (1-12): "))

months = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec"
}

if month in months:
    print("Abbreviation:", months[month])
else:
    print("Invalid month number")


# DICTIONARY Q1. Add a new key-value pair to a dictionary.
# Example: {0:10, 1:20} -> {0:10, 1:20, 2:30}

my_dict = {
    0: 10,
    1: 20
}

my_dict[2] = 30

print(my_dict)


# DICTIONARY Q2. Concatenate three dictionaries.

dict1 = {
    1: 10,
    2: 20
}

dict2 = {
    3: 30,
    4: 40
}

dict3 = {
    5: 50,
    6: 60
}

new_dict = {}

new_dict.update(dict1)
new_dict.update(dict2)
new_dict.update(dict3)

print(new_dict)


# DICTIONARY Q3. Check whether a given key exists in a dictionary.

my_dict = {
    "name": "ABC",
    "rollno": 34,
    "marks": 85
}

key = input("Enter key to search: ")

if key in my_dict:
    print("Key exists")
else:
    print("Key does not exist")


# DICTIONARY Q4. Iterate through a dictionary using a for loop
# to display keys, values, and both keys and values.

my_dict = {
    "name": "ABC",
    "rollno": 34,
    "marks": 85
}

print("Keys:")

for key in my_dict:
    print(key)

print("Values:")

for value in my_dict.values():
    print(value)

print("Keys and values:")

for key, value in my_dict.items():
    print(key, ":", value)


# DICTIONARY Q5. Create a dictionary with keys from 1 to 15
# and values as their squares.

my_dict = {}

for i in range(1, 16):
    my_dict[i] = i ** 2

print(my_dict)


# DICTIONARY Q6. Find the sum of all values in a dictionary.

my_dict = {
    "a": 10,
    "b": 20,
    "c": 30
}

total = sum(my_dict.values())

print("Sum:", total)


# DICTIONARY Q7. Create a dictionary containing 5 student elements.
# Add new information, delete information and display the dictionary.

my_dict = {
    "name": "ABC",
    "rollno": 34,
    "panel": "B",
    "marks": 85,
    "year": 2026
}

print("Original dictionary:", my_dict)

my_dict["address"] = "XYZ"

del my_dict["address"]

print("Student information:", my_dict)


# DICTIONARY Q8. Convert two lists into a dictionary.
# Example: ['name','panel','rollno'] and ['ABC','B',34]

list1 = [
    "name",
    "panel",
    "rollno"
]

list2 = [
    "ABC",
    "B",
    34
]

my_dict = dict(zip(list1, list2))

print(my_dict)


# DICTIONARY Q9. Convert dictionary keys and values into two lists.

my_dict = {
    "name": "ABC",
    "panel": "B",
    "rollno": 34
}

keys_list = list(my_dict.keys())
values_list = list(my_dict.values())

print("Keys list:", keys_list)
print("Values list:", values_list)


# DICTIONARY Q10. Find the mean of all dictionary values.

my_dict = {
    "marks1": 23,
    "marks2": 123,
    "marks3": 43,
    "marks4": 13,
    "marks5": 39
}

mean = sum(my_dict.values()) / len(my_dict)

print("Mean:", mean)


# DICTIONARY Q11. Sort dictionary elements using sorted().

my_dict = {
    "name": "ABC",
    "panel": "B",
    "rollno": 34,
    "marks": [65, 87, 67, 94]
}

print("Sorted keys:", sorted(my_dict))


# TUPLE Q1. Display the fourth element from the first
# and the fourth element from the last.

my_tuple = (
    10,
    20,
    30,
    40,
    50,
    60,
    70
)

print("Fourth element from first:", my_tuple[3])
print("Fourth element from last:", my_tuple[-4])


# TUPLE Q2. Check whether an element exists in a tuple.

my_tuple = (
    10,
    20,
    30,
    40,
    50
)

element = int(input("Enter element to search: "))

if element in my_tuple:
    print("Element exists")
else:
    print("Element does not exist")


# TUPLE Q3. Convert a list into a tuple.

my_list = [
    10,
    20,
    30,
    40,
    50
]

my_tuple = tuple(my_list)

print("Tuple:", my_tuple)


# TUPLE Q4. Find the index of an item in a tuple.

my_tuple = (
    10,
    20,
    30,
    40,
    50
)

element = int(input("Enter element: "))

if element in my_tuple:
    print("Index:", my_tuple.index(element))
else:
    print("Element not found")


# TUPLE Q5. Replace the last value of every tuple in a list with 100.
# Example: [(10,20,40),(40,50,60),(70,80,90)]

my_list = [
    (10, 20, 40),
    (40, 50, 60),
    (70, 80, 90)
]

new_list = []

for item in my_list:
    new_tuple = item[:-1] + (100,)
    new_list.append(new_tuple)

print(new_list)


# SET Q1. Remove a given item from a set.

my_set = {
    10,
    20,
    30,
    40,
    50
}

item = int(input("Enter item to remove: "))

if item in my_set:
    my_set.remove(item)
    print(my_set)
else:
    print("Item not found")


# SET Q2. Find the intersection of two sets.

set1 = {
    1,
    2,
    3,
    4
}

set2 = {
    3,
    4,
    5,
    6
}

print("Intersection:", set1.intersection(set2))


# SET Q3. Find the union of two sets.

set1 = {
    1,
    2,
    3,
    4
}

set2 = {
    3,
    4,
    5,
    6
}

print("Union:", set1.union(set2))


# SET Q4. Find the maximum and minimum values in a set.

my_set = {
    10,
    20,
    5,
    40,
    30
}

print("Maximum:", max(my_set))
print("Minimum:", min(my_set))


# STRING Q1. Count uppercase and lowercase characters in a string.

text = input("Enter a string: ")

upper = 0
lower = 0

for ch in text:

    if ch.isupper():
        upper = upper + 1

    elif ch.islower():
        lower = lower + 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)


# STRING Q2. Check whether a string is a palindrome.

text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# STRING Q3. Create a new string with n copies of the first
# two characters, where n is the length of the string.
# Example: Wipro -> Wiwiwiwiwi

text = input("Enter a string: ")

n = len(text)

result = text[:2] * n

print(result)


# STRING Q4. If the first or last character is 'x',
# remove those x characters.
# Example: xHix -> Hi

text = input("Enter a string: ")

if text.startswith("x"):
    text = text[1:]

if text.endswith("x"):
    text = text[:-1]

print(text)


# STRING Q5. Given a string and integer n, print n repetitions
# of the last n characters.
# Example: Wipro, 3 -> propropro

text = input("Enter a string: ")

n = int(input("Enter n: "))

if n > 0:
    result = text[-n:] * n
else:
    result = ""

print(result)


# REGEX Q1(a). Write a regular expression to recognize
# bat, bit, but, hat, hit and hut.

import re

text = input("Enter a string: ")

pattern = r"^[bh][aiu]t$"

if re.fullmatch(pattern, text):
    print("Match")
else:
    print("No match")


# REGEX Q1(b). Write a regular expression to match a pair
# of words separated by a single space, such as first and last name.

import re

text = input("Enter two words separated by one space: ")

pattern = r"^[A-Za-z]+ [A-Za-z]+$"

if re.fullmatch(pattern, text):
    print("Match")
else:
    print("No match")


# REGEX Q1(c). Write a regular expression to match a word
# and a single letter separated by a comma and single space.
# Example: Last name, first initial.

import re

text = input("Enter in the form Lastname, F: ")

pattern = r"^[A-Za-z]+, [A-Za-z]$"

if re.fullmatch(pattern, text):
    print("Match")
else:
    print("No match")


# NUMPY Q1. Create a 3 x 3 NumPy array with all True values.

import numpy as np

array = np.ones((3, 3), dtype=bool)

print(array)


# NUMPY Q2. Create a 1-D NumPy array containing
# 10 evenly spaced values from 5 to 50.

import numpy as np

array = np.linspace(5, 50, 10)

print(array)


# NUMPY Q3. Convert a Python list into a NumPy array.

import numpy as np

my_list = [
    10,
    20,
    30,
    40,
    50
]

array = np.array(my_list)

print(array)


# NUMPY Q4. Reverse a 1-D NumPy array.

import numpy as np

array = np.array([
    10,
    20,
    30,
    40,
    50
])

print(array[::-1])


# NUMPY Q5. Create a 3 x 3 identity matrix.

import numpy as np

matrix = np.eye(3)

print(matrix)


# NUMPY Q6. Create a 4 x 4 array and extract
# the first row and last column.

import numpy as np

array = np.arange(1, 17).reshape(4, 4)

print("Array:")
print(array)

print("First row:", array[0, :])
print("Last column:", array[:, -1])


# NUMPY Q7. Create a 4 x 4 array and extract
# the first 2 rows and first 2 columns.

import numpy as np

array = np.arange(1, 17).reshape(4, 4)

result = array[:2, :2]

print(result)


# NUMPY Q8. Perform arithmetic operations on two NumPy arrays
# element by element.

import numpy as np

array1 = np.array([
    1,
    2,
    3,
    4
])

array2 = np.array([
    5,
    6,
    7,
    8
])

print("Addition:", array1 + array2)
print("Subtraction:", array1 - array2)
print("Multiplication:", array1 * array2)
print("Division:", array1 / array2)


# NUMPY Q9. Find the dot product of two NumPy arrays.

import numpy as np

array1 = np.array([
    1,
    2,
    3
])

array2 = np.array([
    4,
    5,
    6
])

dot_product = np.dot(array1, array2)

print("Dot product:", dot_product)


# NUMPY Q10. Find the mean, median and standard deviation
# of a NumPy array.

import numpy as np

array = np.array([
    10,
    20,
    30,
    40,
    50
])

print("Mean:", np.mean(array))
print("Median:", np.median(array))
print("Standard deviation:", np.std(array))