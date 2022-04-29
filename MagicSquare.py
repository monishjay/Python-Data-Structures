#  File: MagicSquare.py

#  Description: Creates a odd magic square of n * n dimensions where each row, column, and diagonal sum to the same value. Also determines sum of all adjacent numbers to a certain value.

#  Student's Name: Monish Jayakumar

#  Student's UT EID: mj27639
 
#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E 

#  Unique Number: 52590

#  Date Created: 9/3

#  Date Last Modified: 9/6

import sys

# Populate a 2-D list with numbers from 1 to n2
# This function must take as input an integer. You may assume that
# n >= 1 and n is odd. This function must return a 2-D list (a list of
# lists of integers) representing the square.
# Example 1: make_square(1) should return [[1]]
# Example 2: make_square(3) should return [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
def make_square ( n ):
    square = [[0 for _ in range(n)] for _ in range(n)]
    square[n - 1][n // 2] = 1
    x = n - 1
    y = n // 2
    x, y = updateXY(x,y)
    for i in range(2, n ** 2 + 1):
        x, y = fillSquare(square, x, y, n, i)
        x, y = updateXY(x,y)
    return square

# increments x and y coordinates
def updateXY(x,y):
    x += 1
    y += 1
    return x, y

# fills square with elements and adjusts coordinates if goes outside dimensions of grid
def fillSquare(square, x, y, n, i):  
    if x >= n and y >= n:
        x = x - 2
        y = y - 1
        if not checkOpen(square, x, y):
            x -= 2
            y -= 1
    elif x >= n:
        x = 0
        if not checkOpen(square, x, y):
            x -= 2
            y -= 1
    elif y >= n:
        y = 0
        if not checkOpen(square, x, y):
            x -= 2
            y -= 1
    elif not checkOpen(square, x, y):
            x -= 2
            y -= 1
    square[x][y] = i
    return x,y

# checks if specific slot in square is already filled or doesn't equal default value of 0
def checkOpen(square,x,y):
    return square[x][y] == 0

# Print the magic square in a neat format where the numbers
# are right justified. This is a helper function.
# This function must take as input a 2-D list of integers
# This function does not return any value
# Example: Calling print_square (make_square(3)) should print the output
# 4 9 2
# 3 5 7
# 8 1 6
def print_square ( magic_square ):
    for i in magic_square:
        for j in i:
            print(j, end = " ")
        print()

# Check that the 2-D list generated is indeed a magic square
# This function must take as input a 2-D list, and return a boolean
# This is a helper function.
# Example 1: check_square([[1, 2], [3, 4]]) should return False
# Example 2: check_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]) should return True
def check_square ( magic_square ):
    n = len(magic_square)
    correctSum = n * ((n ** 2) + 1) / 2 
    for i in magic_square:
        rowSum = sum(i)
        if (rowSum != correctSum):
            return False
    return True

# Input: square is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the magic square
#         if n is outside the range return 0
def sum_adjacent_numbers (square, n):
    if n < 1 or n > len(square) ** 2:
        return 0
    numSum = 0
    x, y = findCoords(square, n)
    numSum += checkIfValid(square, x + 1, y + 1)
    numSum += checkIfValid(square, x + 1, y)
    numSum += checkIfValid(square, x + 1, y - 1)
    numSum += checkIfValid(square, x, y + 1)
    numSum += checkIfValid(square, x, y - 1)
    numSum += checkIfValid(square, x - 1, y)
    numSum += checkIfValid(square, x - 1, y - 1)
    numSum += checkIfValid(square, x - 1, y + 1)
    return numSum

# finds coordinates on magic square of inputted number
def findCoords(square, n):
    for i in range(len(square)):
        for j in range(len(square)):
            if square[i][j] == n:
                return i, j
    return

# checks if adjacent number of inputted number is within the dimensions of the magic square
def checkIfValid(square, x, y):
    n = len(square)
    if x >= 0 and y >= 0 and x < n and y < n:
        return square[x][y]
    else:
        return 0
        
def main():
  # read the input file from stdin
    n = int(sys.stdin.readline().strip())
    nums = sys.stdin.read().splitlines()
    lst = [int(i) for i in nums]
  # create the magic square
    square = make_square(n)
    # print_square(square)
    # check_square(square))
  # print the sum of the adjacent numbers 
    for num in lst:
        print(sum_adjacent_numbers(square, num))
# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()