#Multiply matrices 4x4
def multipule(x, y):
    result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    # iterate through rows of X
    for i in range(4):
        # iterate through columns of Y
        for j in range(4):
            # iterate through rows of Y
            for k in range(4):
                result[i][j] += x[i][k] * y[k][j]
    return result

#Multiply matrices 4x1
def multipuleVector(x, y):
    result = [[0], [0], [0], [0]]
    # iterate through rows of X
    for i in range(4):
        # iterate through columns of Y
        for j in range(1):
            # iterate through rows of Y
            for k in range(4):
                result[i][j] += x[i][k] * y[k][j]
    return result

#Elementary matrix
def elementmatrix(matrix, row, column):
    i = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    i[row][column] = -matrix[row][column]/matrix[column][column]
    return i


def lelementmatrix(matrix, row, column):
    i = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    i[row][column] = matrix[row][column]/matrix[column][column]
    return i

#equivalence test to matrix I
def imatrix(matrix):
    i = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    for k in range(4):
        for j in range(4):
            if i[k][j] != matrix[k][j]:
                return False
    return True


#copy matrix
def changematrix(mat1, mat2, r, c):
    for i in range(r):
        for j in range(c):
            mat1[i][j] = mat2[i][j]
    return mat1


#connecting matrix
def addmatrix(mat1, mat2, r, c):
    mat3 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(r):
        for j in range(c):
            mat3[i][j] = mat1[i][j] + mat2[i][j]
    return mat3


#change sign matrix
def signmatrix(mat1, r, c):
    mat2 = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    mat2[r][c] = -1 * mat1[r][c]
    return mat2


#up triple matrix rating
def uptriangle(matrix):
    for i in range(4):
        for j in range(4):
            if i < j:
                if matrix[j][i] != 0:
                    mat1 = elementmatrix(matrix, j, i)
                    matrix = multipule(mat1, matrix)

    return matrix


#matrix l
def lmatrix(matrix):
    mat3 = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    for i in range(4):
        for j in range(4):
            if i < j:
                if matrix[j][i] != 0:
                    mat1 = elementmatrix(matrix, j, i)
                    mat2 = signmatrix(mat1, j, i)
                    mat3 = multipule(mat3, mat2)
                    matrix = multipule(mat1, matrix)

    return mat3

#reverse function without diagonal
def ratingmatrix(matrix):
    matrixi = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    for i in range(4):
        for j in range(4):
            if i < j:
                if matrix[j][i] != 0:
                    mat1 = elementmatrix(matrix, j, i)
                    matrix = multipule(mat1, matrix)
                    matrixi = multipule(mat1, matrixi)

    for i in range(4):
        for j in range(4):
            if i > j:
                if matrix[j][i] != 0:
                    mat1 = elementmatrix(matrix, j, i)
                    matrix = multipule(mat1, matrix)
                    matrixi = multipule(mat1, matrixi)
    return matrixi

#original function only with the diagonal
def ratingmatrixslant(matrix):
    matrixi = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    for i in range(4):
        for j in range(4):
            if i < j:
                if matrix[j][i] != 0:
                    mat1 = elementmatrix(matrix, j, i)
                    matrix = multipule(mat1, matrix)
                    matrixi = multipule(mat1, matrixi)

    for i in range(4):
        for j in range(4):
            if i > j:
                if matrix[j][i] != 0:
                    mat1 = elementmatrix(matrix, j, i)
                    matrix = multipule(mat1, matrix)
                    matrixi = multipule(mat1, matrixi)
    return matrix

def lowtriangle(matrix):
    for i in range(4):
        for j in range(4):
            if i > j:
                if matrix[j][i] != 0:
                    mat1 = elementmatrix(matrix, j, i)
                    matrix = multipule(mat1, matrix)
    return matrix

#check that the determinant is non-zero
def determinant(matrix, r, c):
    mat1 = uptriangle(matrix)
    dete = 1
    for i in range(r):
        for j in range(c):
            if i == j:
                dete = dete*mat1[j][i]
    return dete

#last level in matrix rating
def slant(mat1, mat2, r, c):
    mat3 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(r):
        for j in range(c):
            mat3[i][j] = mat2[i][j]/mat1[i][i]

    return mat3

#max pivot
def switch(matrix):
    newmatrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    maxindex = 0
    for i in range(4):
        maxindex = i
        for j in range(4):
            if i < j:
                if matrix[maxindex][i] < matrix[j][i]:
                    maxindex = j
        for k in range(4):
            newmatrix[i][k] = matrix[maxindex][k]
            matrix[maxindex][k] = matrix[i][k]
            matrix[i][k] = newmatrix[i][k]
    return newmatrix



#Defining Matrix A and finding its inverse matrix
originalmatrix = [[2, 4, 6, -8], [6, -9, 7, 2], [5, 3, 3, -4], [8, -2, 1, -3]]
print("matrix A:")
print(""
      "")
for o in originalmatrix:
    print(o)
print(""
      "")
if determinant(originalmatrix, 4, 4) != 0:
    originalmatrix = switch(originalmatrix)
    # for o in originalmatrix:
    #    print(o)
    # print(""
    #       "")
    reversematrix = ratingmatrix(originalmatrix)
    originalmatrix = ratingmatrixslant(originalmatrix)
    reversematrix = slant(originalmatrix, reversematrix, 4, 4)
    print("the inverse matrix of A:")
    print(""
          "")
    for o in reversematrix:
        print(o)
    print(""
          "")
vectorb = [[2], [4], [6], [-8]]
matrix = [[2, 5, 1, 0], [-1, 3, 8, 6], [1, 4, 5, -3], [4, 1, 1, 7]]
matrix = switch(matrix)
for o in matrix:
    print(o)
print(""
      "")

u = uptriangle(matrix)
u1 = ratingmatrix(u)
u2 = ratingmatrixslant(u)
u = slant(u2, u1, 4, 4)
print("matrix U:")
print(""
      "")
for o in u:
    print(o)
print(""
      "")

l = lmatrix(matrix)
l1 = ratingmatrix(l)
l2 = ratingmatrixslant(l)
l = slant(l2, l1, 4, 4)
print("matrix L:")
print(""
      "")
for o in l:
    print(o)
print(""
      "")

result = multipule(l, u)
result = multipuleVector(result, vectorb)
print("vector X:")
print(""
      "")
for o in result:
    print(o)
print(""
      "")
# matrixtry = [[2, 0, 0, 0], [0, 3, 0, 0], [0, 0, 5, 0], [0, 0, 0, 4]]
# for o in matrixtry:
#     print(o)
# originalmatrix = switch(originalmatrix)
# if determinant(originalmatrix, 4, 4) != 0:
#     # originalmatrix = switch(originalmatrix)
#     reversematrix = ratingmatrix(originalmatrix)
#     originalmatrix = lowtriangle(originalmatrix)
#     # for e in originalmatrix:
#     #     print(e)
#     originalmatrix = uptriangle(originalmatrix)
#     reversematrix = slant(originalmatrix, reversematrix, 3, 3)
#     for e in reversematrix:
#         print(e)
# else:
#     print("error")
# print(""
#       "")
# u = uptriangle(originalmatrix)
# for o in u:
#     print(o)
# print(""
#       "")
# l = lmatrix(originalmatrix)
# for o in l:
#     print(o)
# print(""
#       "")
# a = multipule(l, u)
# for o in a:
#     print(o)
# print(""
#       "")
# lminos = ratingmatrix(l)
# for o in lminos:
#     print(o)