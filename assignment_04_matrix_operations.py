# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# ==========================================================
# Programming Fundamentals - Assignment 4
# Topic: Matrix Operations
# ==========================================================

# Function to enter a matrix
def input_matrix(rows, cols):
    matrix = []

    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        matrix.append(row)

    return matrix


# Function to print a matrix
def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end="\t")
        print()


# Function to transpose a matrix
def transpose(matrix):
    result = []

    for j in range(len(matrix[0])):
        new_row = []

        for i in range(len(matrix)):
            new_row.append(matrix[i][j])

        result.append(new_row)

    return result


# Function to add two matrices
def add(matrix1, matrix2):
    result = []

    for i in range(len(matrix1)):
        row = []

        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])

        result.append(row)

    return result


# Function to multiply two matrices
def multiply(matrix1, matrix2):
    result = []

    for i in range(len(matrix1)):
        row = []

        for j in range(len(matrix2[0])):
            total = 0

            for k in range(len(matrix2)):
                total = total + matrix1[i][k] * matrix2[k][j]

            row.append(total)

        result.append(row)

    return result


# ==========================
# Main Program
# ==========================

print("MATRIX OPERATIONS")

print("\nPart A - Transpose a Matrix")
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = input_matrix(rows, cols)

print("\nOriginal Matrix")
print_matrix(matrix)

t = transpose(matrix)

print("\nTranspose")
print_matrix(t)


print("\n----------------------------")
print("Part B - Add Two Matrices")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("\nEnter Matrix 1")
matrix1 = input_matrix(rows, cols)

print("\nEnter Matrix 2")
matrix2 = input_matrix(rows, cols)

answer = add(matrix1, matrix2)

print("\nResult")
print_matrix(answer)


print("\n----------------------------")
print("Part C - Multiply Two Matrices")

rows1 = int(input("Enter rows of Matrix A: "))
cols1 = int(input("Enter columns of Matrix A: "))

print("\nEnter Matrix A")
matrixA = input_matrix(rows1, cols1)

rows2 = int(input("\nEnter rows of Matrix B: "))
cols2 = int(input("Enter columns of Matrix B: "))

if cols1 != rows2:
    print("\nMatrix multiplication cannot be done.")
else:
    print("\nEnter Matrix B")
    matrixB = input_matrix(rows2, cols2)

    product = multiply(matrixA, matrixB)

    print("\nProduct Matrix")
    print_matrix(product)
