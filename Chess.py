
#  File: Chess.py

#  Description: This program outputs the number of solutions for placing n queens on an n-dimensional board 

#  Student Name: Talah El-Zein

#  Student UT EID: the272

#  Partner Name: Monish Jayakumar

#  Partner UT EID: mj27639

#  Course Name: CS 313E

#  Unique Number: 52590

#  Date Created: 10/16/2021

#  Date Last Modified: 10/16/2021

import sys

class Queens (object):
  def __init__ (self, n = 8):
    self.board = []
    self.n = n
    for i in range (self.n):
      row = []
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)

  # print the board
  def print_board (self):
    for i in range (self.n):
      for j in range (self.n):
        print (self.board[i][j], end = ' ')
      print ()
    print ()

  # check if a position on the board is valid
  def is_valid (self, row, col):
    for i in range (self.n):
      if (self.board[row][i] == 'Q') or (self.board[i][col] == 'Q'):
        return False
    for i in range (self.n):
      for j in range (self.n):
        row_diff = abs (row - i)
        col_diff = abs (col - j)
        if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
          return False
    return True
    
  # do the recursive backtracking
  def recursive_solve (self, col, sol):
      
    if (col == self.n):
      # increment sol when solution is found
      # deleted return True to look for all possible solutions
      sol[0] += 1
      
    else:
      for i in range (self.n):
        if (self.is_valid (i, col)):
          self.board[i][col] = 'Q'
          # recursively checks if all columns are valid
          self.recursive_solve(col + 1, sol)
          # if sol not found, replace 'Q' with '*'
          # if sol found, resets board back to all '*'
          self.board[i][col] = '*'
          
      # if no solution found
      return False

  # if the problem has a solution print the board
  def solve (self):
    # initializes solution num to 0
    sol = [0]
    self.recursive_solve(0, sol)
    print(sol[0])

def main():
  #read the size of the board
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create a chess board
  game = Queens (n)

  # place the queens on the board and count the solutions
  # print the number of solutions
  game.solve()

  
if __name__ == "__main__":
  main()
