m = int(input("Enter the number of rows of A: "))
n = int(input("Enter the number of columns of A: "))
p = int(input("Enter the number of columns of B: "))
matrix1 = []
matrix2 = []
matrix_product = []
for i in range(m):
    row = []
    for j in range(n):
        a = int(input(f"Enter element for matrix1 [{i+1},{j+1}]: "))
        row.append(a)
    matrix1.append(row)
for k in range(n):
    row = []
    for l in range(p):
        b = int(input(f"Enter element for matrix2 [{k+1},{l+1}]: "))
        row.append(b)
    matrix2.append(row)
print(matrix1)
print(matrix2)
for i in range(m):
    row = []
    for j in range(p):
        toplam = 0
        for k in range(n):
            toplam += matrix1[i][k] * matrix2[k][j]
        row.append(toplam)
    matrix_product.append(row)
print(matrix_product)