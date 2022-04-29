
#  Description: Computes all permutations of valid magic squares

# A magic square is defined as a "square array of numbers consisting of the distinct positive integers 1, 2, ..., 
# arranged such that the sum of the numbers in any horizontal, vertical, or main diagonal line is always the same number

import sys

# checks if a 1-D list if converted to a 2-D list is magic
# a is 1-D list of integers
# returns True if a is magic and False otherwise
def is_magic (a):
  x = int(len(a) ** 0.5)
  magic_sum = x * (x ** 2 + 1) / 2
  tot = 0
  tot2 = 0
  if x == 3:
    tot = a[2] + a[4] + a[6]
    tot2 = a[0] + a[4] + a[8]
  if x == 4:
    tot = a[3] + a[6] + a[9] + a[12]
    tot2 = a[0] + a[5] + a[10] + a[15]

  return tot2 == tot == magic_sum  

# checks row sum
def check(a, idx, x):
 # x = int(len(a) ** 0.5)
  start = idx - x + 1
  end = idx + 1
  expected_sum = int(x * (x ** 2 + 1) / 2)
  return sum(a[start:end]) == expected_sum

# checks if n - 1 elements sum is already too large
def check2(a, idx, x):
  #x = int(len(a) ** 0.5)
  start = idx - x + 2
  end = idx + 1
  expected_sum = int(x * (x ** 2 + 1) / 2)
  s = sum(a[start:end])
  return (expected_sum - s > x**2) or (s >= expected_sum)


# checks if last n number is available to complete magic sum
def check3 (a, idx, x):
  #x = int(len(a) ** .5)
  expected_sum = int(x * (x ** 2 + 1) / 2)
  tot = 0
  ind = idx
  for i in range(x - 1):
    tot += a[ind]
    ind -= x 
  #print(tot, ind)
  num_needed = expected_sum - tot
  return num_needed in a[:idx + 1] or (expected_sum - tot > x**2) or (tot >= expected_sum)

# checks column sum
def check4 (a, idx, x):
  #x = int(len(a) ** .5)
  expected_sum = int(x * (x ** 2 + 1) / 2)
  tot = 0
  ind = idx
  for i in range(x):
    tot += a[ind]
    ind -= x
  return tot != expected_sum
  
  # checks last row element if required number has been used already
def check5(a, idx, x):
  #x = int(len(a) ** 0.5)
  start = idx - x + 2
  end = idx + 1
  expected_sum = int(x * (x ** 2 + 1) / 2)
  s = sum(a[start:end])
  num_needed = expected_sum - s
  return num_needed in a[:idx + 1] or (expected_sum - s > x**2) or (s >= expected_sum)


# checks diagonals
# n = 3: check 2, 4 ,6
# n = 4: check 3, 6, 9, 12
def check6 (a, idx, x):
  x = int(len(a) ** .5)
  expected_sum = int(x * (x ** 2 + 1) / 2)
  tot = 0
  if x == 3:
    tot = a[2] + a[4] + a[6]
  if x == 4:
    tot = a[3] + a[6] + a[9] + a[12]
  #for i in range(x - 1):
   # tot += a[b]
   # b += (x - 1)
  return tot != expected_sum  

 
# python magicsquare.py < magic.in
# this function recursively permutes all magic squares
def permute ( a, idx, all_magic ):
  hi = int(len(a) ** 0.5)
  if (idx + 1 == len(a)) and is_magic(a):
    c = a[:]
    #print(c)
    all_magic.append(c)
  else:
    for i in range (idx, len(a)):
      a[idx], a[i] = a[i], a[idx]

      # checks when at n - 1 elements if there's an available number to complete magic sum
      if (len(a) - (hi * 2)) <= idx < (len(a) - hi) and check3(a, idx, hi):
        a[idx], a[i] = a[i], a[idx]

      # checks column sums on last row
      elif (len(a) - hi) <= idx < (len(a) - 1) and check4(a, idx, hi):
        a[idx], a[i] = a[i], a[idx]

       # checks row sum
      elif (idx + 1) % hi == 0 and not check(a, idx, hi):
        a[idx], a[i] = a[i], a[idx]


      # check2 checks if n - 1 element sum is too large and
      # if there's available row element to complete magic sum
      elif (idx + 2) % hi == 0 and check5 (a,idx, hi): 
        a[idx], a[i] = a[i], a[idx]

      # valid magic square so keep permuting
      else:
        permute (a, idx + 1, all_magic) 
        a[idx], a[i] = a[i], a[idx]

def main():
  # read the dimension of the magic square
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create an empty list for all magic squares
  all_magic = []

  # create the 1-D list that has the numbers 1 through n^2
  lst = [x for x in range(1, n**2 + 1)]

  # generate all magic squares using permutation 
  permute(lst, 0, all_magic)
  # print all magic squares
  for square in all_magic:
    print (square)


if __name__ == "__main__":
  main()
