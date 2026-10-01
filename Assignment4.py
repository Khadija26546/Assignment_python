# Accept matrix elements from the user

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter elements of first matrix:")
A = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"Enter element [{i}][{j}]: ")))
    A.append(row)

print("Enter elements of second matrix:")
B = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"Enter element [{i}][{j}]: ")))
    B.append(row)

# Matrix Addition
C = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("Addition of matrices:")
for row in C:
    print(row)