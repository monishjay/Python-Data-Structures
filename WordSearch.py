
#  Description: Searches through grid of letters to find coordinates of specified word

import sys

numColRow = int(sys.stdin.readline().strip())
grid = [["x" for _ in range(numColRow)] for _ in range(numColRow)]
wordList = []


# Input: None
# Output: function returns a 2-D list that is the grid of letters and
#         1-D list of words to search
def read_input ( ):
  sys.stdin.readline() # moves past blank line
  rowIndex = 0
  for i in range(numColRow):
    line = sys.stdin.readline().strip()
    chArr = line.split(" ")
    makeGrid(grid, chArr, rowIndex)
    rowIndex += 1
  sys.stdin.readline() # blank line
  numWords = int(sys.stdin.readline().strip())
  makeWordList(wordList, numWords)
  # print(wordList)
  # print(grid)
  return grid, wordList

# helper method to populate 2d grid of letters
def makeGrid(grid, line, rowIndex):
  for i in range(numColRow):
      grid[rowIndex][i] = line[i] 

# helper method to populate list of words
def makeWordList(wordList, numWords):
  for i in range(numWords):
    word = sys.stdin.readline().strip()
    wordList.append(word)

# Input: a 2-D list representing the grid of letters and a single
#        string representing the word to search
# Output: returns a tuple (i, j) containing the row number and the
#         column number of the word that you are searching 
#         or (0, 0) if the word does not exist in the grid

def find_word (grid, word):
  coord = (0,0)
  firstLetter = word[0]
  length = len(word)
  # searches each letter in grid until first letter of word is found
  for i in range(numColRow):
    for j in range(numColRow):
      if grid[i][j] == firstLetter:
        coord = searchGrid(grid,i,j,word,length)
        if (checkCoord(coord)):
          return coord
  return (0,0)

  # searches through grid to find matching word by calling each search method
  # if any method finds valid coordinates which != (0,0), returns coordinates immedietly
def searchGrid(grid,i,j,word,length):
  coord = (0, 0)
  coord = searchRight(grid,i,j,word,length)
  if (checkCoord(coord)):
    return coord
  coord = searchLeft(grid,i,j,word,length)
  if (checkCoord(coord)):
    return coord
  coord = searchUp(grid,i,j,word,length)
  if (checkCoord(coord)):
    return coord
  coord = searchDown(grid,i,j,word,length)
  if (checkCoord(coord)):
    return coord
  coord = searchBotRDiagonal(grid,i,j,word,length)
  if (checkCoord(coord)):
    return coord
  coord = searchBotLDiagonal(grid,i,j,word,length)
  if (checkCoord(coord)):
    return coord
  coord = searchTopRDiagonal(grid,i,j,word,length)
  if (checkCoord(coord)):
    return coord
  coord = searchTopLDiagonal(grid,i,j,word,length)
  if (checkCoord(coord)):
    return coord
  return coord

# checks if no coordinate was found for word
def checkCoord(coord):
  return coord != (0,0) and coord != None

# searches grid bottom right diagonally
def searchBotRDiagonal(grid,i,j,word,length):
  coord = (i + 1, j + 1)
  wordIndex = 0
  while (j < numColRow and j >= 0 and i >= 0 and i < numColRow and grid[i][j] == word[wordIndex]):
    # print (grid[i][j], i, j, wordIndex)
    #print(length)
    wordIndex += 1
    # print(wordIndex, (i, j))
    # print(i,j)
    j += 1
    i += 1
    if (wordIndex == length):
      # print(coord)
      return coord
  return (0,0)

# searches grid bottom left diagonally
def searchBotLDiagonal(grid,i,j,word,length):
  coord = (i + 1, j + 1)
  wordIndex = 0
  while (j < numColRow and j >= 0 and i >= 0 and i < numColRow and grid[i][j] == word[wordIndex]):
    # print (grid[i][j], i, j, wordIndex)
    #print(length)
    wordIndex += 1
    # print(wordIndex, (i, j))
    # print(i,j)
    j -= 1
    i += 1
    if (wordIndex == length):
      # print(coord)
      return coord
  return (0,0)

# searches grid top right diagonally
def searchTopRDiagonal(grid,i,j,word,length):
  coord = (i + 1, j + 1)
  wordIndex = 0
  while (j < numColRow and j >= 0 and i >= 0 and i < numColRow and grid[i][j] == word[wordIndex]):
    # print (grid[i][j], i, j, wordIndex)
    #print(length)
    wordIndex += 1
    # print(wordIndex, (i, j))
    # print(i,j)
    j += 1
    i -= 1
    if (wordIndex == length):
      # print(coord)
      return coord
  return (0,0)

# searches grid top left diagonally
def searchTopLDiagonal(grid,i,j,word,length):
  coord = (i + 1, j + 1)
  wordIndex = 0
  while (j < numColRow and j >= 0 and i >= 0 and i < numColRow and grid[i][j] == word[wordIndex]):
    # print (grid[i][j], i, j, wordIndex)
    #print(length)
    wordIndex += 1
    # print(wordIndex, (i, j))
    # print(i,j)
    j -= 1
    i -= 1
    if (wordIndex == length):
      # print(coord)
      return coord
  return (0,0)

# searches grid rightwards
def searchRight(grid, i, j, word, length):
  coord = (i + 1, j + 1)
  wordIndex = 0
  while (j < numColRow and grid[i][j] == word[wordIndex]):
    # print (grid[i][j], i, j, wordIndex)
    #print(length)
    wordIndex += 1
    # print(wordIndex)
    j += 1
    if (wordIndex == length):
      # print(coord)
      return coord
  return (0,0)

# searches grid leftwards  
def searchLeft(grid, i, j, word, length):
  coord = (i + 1, j + 1)
  wordIndex = 0
  while (j >= 0 and grid[i][j] == word[wordIndex]):
    # print (grid[i][j], i, j, wordIndex)
    #print(length)
    wordIndex += 1
    j -= 1
    if (wordIndex  == length):
      # print(coord)
      return coord

# searches grid upwards
def searchUp(grid, i, j, word, length):
  coord = (i + 1, j + 1)
  wordIndex = 0
  while (i >= 0 and grid[i][j] == word[wordIndex]):
    # print (grid[i][j], i, j, wordIndex)
    #print(length)
    wordIndex += 1
    i -= 1
    if (wordIndex  == length):
      # print(coord)
      return coord

# searches grid downwords
def searchDown(grid, i, j, word, length):
  coord = (i + 1, j + 1)
  wordIndex = 0
  while (i < numColRow and grid[i][j] == word[wordIndex]):
    # print (grid[i][j], i, j)
    #print(length)
    wordIndex += 1
    i += 1
    if (wordIndex  == length):
      # print(coord)
      return coord

# main driver function for output
def main():
  # read the input file from stdin
  grid, wordList = read_input()
  # find each word and print its location
  for word in wordList:
    location = find_word (grid, word)
    print(word + ": " + str(location))

if __name__ == "__main__":
  main()

