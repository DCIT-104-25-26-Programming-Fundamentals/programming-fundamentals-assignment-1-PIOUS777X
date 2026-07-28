# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# ==========================================================
# Programming Fundamentals - Assignment 4
# Topic: Matrix Operations
# ==========================================================

# ==========================================================
# Programming Fundamentals - Assignment 4
# Topic: Matrix Operations
# ==========================================================

# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# Task: Matrix Operations
# =============================================================================

# -------------------------------
# Function to read a matrix
# -------------------------------
def read_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        while True:
            row = list(map(int, input(f"Enter row {i + 1}: ").split()))
            if len(row) == cols:
                matrix.append(row)
                break
            else:
                print(f"Please enter exactly {cols} values.")
    return matrix


# -------------------------------
# Function to display a matrix
# -------------------------------
def display_matrix(matrix):
    for row in matrix:
        for value in row:
            print(f"{value:6}", end="")
        print()


# -------------------------------
# Part A - Transpose a Matrix
# -------------------------------
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transpose = []

    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transpose.append(new_row)

    return transpose


# -------------------------------
# Part B - Add Two Matrices
# -------------------------------
def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])

    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result


# -------------------------------
# Part C - Multiply Two Matrices
# -------------------------------
def multiply_matrices(matrixA, matrixB):
    rowsA = len(matrixA)
    colsA = len(matrixA[0])
    colsB = len(matrixB[0])

    result = []

    for i in range(rowsA):
        row = []
        for j in range(colsB):
            total = 0
            for k in range(colsA):
                total += matrixA[i][k] * matrixB[k][j]
            row.append(total)
        result.append(row)

    return result


# =============================================================================
# MAIN PROGRAM
# =============================================================================

while True:
    print("\n========== MATRIX OPERATIONS ==========")
    print("1. Transpose a Matrix")
    print("2. Add Two Matrices")
    print("3. Multiply Two Matrices")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # ---------------------------------------------------
    # Part A - Transpose
    # ---------------------------------------------------
    if choice == "1":
        print("\n--- Transpose a Matrix ---")

        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))

        matrix = read_matrix(rows, cols)

        print("\nOriginal Matrix:")
        display_matrix(matrix)

        transposed = transpose_matrix(matrix)

        print("\nTransposed Matrix:")
        display_matrix(transposed)

    # ---------------------------------------------------
    # Part B - Addition
    # ---------------------------------------------------
    elif choice == "2":
        print("\n--- Add Two Matrices ---")

        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))

        print("\nEnter Matrix 1")
        matrix1 = read_matrix(rows, cols)

        print("\nEnter Matrix 2")
        matrix2 = read_matrix(rows, cols)

        result = add_matrices(matrix1, matrix2)

        print("\nMatrix 1:")
        display_matrix(matrix1)

        print("\nMatrix 2:")
        display_matrix(matrix2)

        print("\nSum of Matrices:")
        display_matrix(result)

    # ---------------------------------------------------
    # Part C - Multiplication
    # ---------------------------------------------------
    elif choice == "3":
        print("\n--- Multiply Two Matrices ---")

        rowsA = int(input("Enter rows of Matrix A: "))
        colsA = int(input("Enter columns of Matrix A: "))

        print("\nEnter Matrix A")
        matrixA = read_matrix(rowsA, colsA)

        rowsB = int(input("\nEnter rows of Matrix B: "))
        colsB = int(input("Enter columns of Matrix B: "))

        if colsA != rowsB:
            print("\nMatrix multiplication is not possible.")
            print("The number of columns in Matrix A must equal the number of rows in Matrix B.")
        else:
            print("\nEnter Matrix B")
            matrixB = read_matrix(rowsB, colsB)

            result = multiply_matrices(matrixA, matrixB)

            print("\nMatrix A:")
            display_matrix(matrixA)

            print("\nMatrix B:")
            display_matrix(matrixB)

            print("\nProduct (A × B):")
            display_matrix(result)

    # ---------------------------------------------------
    # Exit
    # ---------------------------------------------------
    elif choice == "4":
        print("\nProgram terminated.")
        break

    else:
        print("\nInvalid choice. Please select between 1 and 4.")
