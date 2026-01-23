m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))
matrix1 = []
matrix2 = []
for i in range(m):
    row = []
    for j in range(n):
        a = int(input(f"Enter element for matrix1 [{i+1},{j+1}]: "))
        row.append(a)
    matrix1.append(row)
for k in range(m):
    row = []
    for l in range(n):
        b = int(input(f"Enter element for matrix2 [{k+1},{l+1}]: "))
        row.append(b)
    matrix2.append(row)
toplam = []
for p in range(m):
    row_toplam = []
    for q in range(n):
        row_toplam.append(matrix1[p][q] + matrix2[p][q])
    toplam.append(row_toplam)
print(toplam)