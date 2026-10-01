a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Check for the largest side and apply Pythagoras theorem
if a >= b and a >= c:
    largest = a
    x = b
    y = c
elif b >= a and b >= c:
    largest = b
    x = a
    y = c
else:
    largest = c
    x = a
    y = b

if x**2 + y**2 == largest**2:
    print("The triangle is a right-angled triangle.")
else:
    print("The triangle is not a right-angled triangle.")