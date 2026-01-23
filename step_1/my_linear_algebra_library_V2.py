def augmented_matrix(A, B):
    M = [row[:] for row in A]
    for i in range(len(M)):
        M[i].append(B[i])
    return M

def back_substitution(A,B):
    M = augmented_matrix(A, B)
    M = echelon_form(M)
    n = len(M)
    x = [0.0] * n
    for i in range(n-1,-1,-1):
        sum = 0
        for j in range(i+1,n):
            sum += M[i][j] * x[j]
        x[i] = (M[i][n] - sum)/M[i][i]
    return x      

def echelon_form(M):
    rows = len(M)
    columns = len(M[0])
    for j in range(columns):
        for i in range(j+1,rows):
            if M[j][j] == 0:
                for k in range(j+1,rows):
                    if M[k][j] != 0:
                        row_swap(M, j, k)
                        break
            c = -M[i][j] / M[j][j]
            row_addition(M, i, j, c)
    return M

def matrix_show(M):
    for i in M:
        print(i)

def row_swap(M, r1, r2):
    M[r1], M[r2] = M[r2], M[r1]
    return M

def row_multiplier(M, r, c):
    for i in range(len(M[r])):
        M[r-1][i] *= c
    return M

def row_addition(M, main_row, added_row, coefficient):
    for i in range(len(M[main_row])):
        M[main_row][i] += coefficient * M[added_row][i]
    return M

def matrix_multiplier(matrix1, matrix2):
    matrix_product = []
    m = len(matrix1)
    p = len(matrix2[0])
    n= len(matrix1[0])
    for i in range(m):
        row = []
        for j in range(p):
            sum = 0
            for k in range(n):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        matrix_product.append(row)
    return matrix_product

def list_to_matrix(items_g, m, n):
    length = len(items_g)
    if length > m*n:
        print("Number of elements are bigger than dimensions of matrix.")
        return None
    while length < m*n:
        items_g.append(0)
        length = length + 1
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(items_g[i*n+j])
        matrix.append(row)
    return matrix

def dot_product(y1, y2):
    r = len(y1)
    product = 0
    for i in range(r):
        product += int(y1[i]*y2[i])
    return product