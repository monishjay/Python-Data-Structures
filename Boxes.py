
#  Description: This program  computes the maximum number of nesting boxes and outputs the maximum and the number of subsets.

import sys

# Input: 2-D list of boxes. Each box of three dimensions is sorted
#        box_list is sorted
# Output: function returns two numbers, the maximum number of boxes
#         that fit inside each other and the number of such nesting
#         sets of boxes
def nesting_boxes (box_list):
    
  memo = []

  # goes through all the boxes
  for i in range(len(box_list)):
      
    # initializes local max and memo entry for each box
    local_max = 0
    subsets = 1
  
    # goes through the smaller boxes in descending order
    for j in range(i - 1, -1, -1):
      if does_fit(box_list[j], box_list[i]):
        
        # checks if local max of smaller box is greater than current local max
        if memo[j][0] > local_max:
          # resets local max to the local max of the smaller box and resets subsets to the subsets of the smaller box
          local_max = memo[j][0]
          subsets = memo[j][1]
          
        # if local max is the same, increment amount of subsets
        elif memo[j][0] == local_max:
          subsets += memo[j][1]
          
    # increments local_max to take into consideration the current box we are at
    local_max += 1
    
    memo.append([local_max, subsets])
    
  global_max = find_global_max(memo)
  
  num_sets = num_of_sets(memo, global_max)

  return global_max, num_sets

# counts how many sets have global_max boxes
def num_of_sets(memo, global_max):
    sub_count = 0
    for i in range(len(memo)):
      if memo[i][0] == global_max:
        # increment num of subsets from each box with global max
        sub_count += memo[i][1]

    return sub_count

# finds global_max
def find_global_max(memo):

    # creates a list of the local maxes of all the boxes
    global_list = [x[0] for x in memo]
    global_max = max(global_list)

    return global_max
    

# returns True if box1 fits inside box2
def does_fit (box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
  # read the number of boxes 
  line = sys.stdin.readline()
  line = line.strip()
  num_boxes = int (line)

  # create an empty list for the boxes
  box_list = []

  # read the boxes from the file
  for i in range (num_boxes):
    line = sys.stdin.readline()
    line = line.strip()
    box = line.split()
    for j in range (len(box)):
      box[j] = int (box[j])
    box.sort()
    box_list.append (box)

  # print to make sure that the input was read in correctly
  #print (box_list)
  #print()

  # sort the box list
  box_list.sort()

  # print the box_list to see if it has been sorted.
  #print (box_list)
  #print()

  # get the maximum number of nesting boxes and the
  # number of sets that have that maximum number of boxes
  max_boxes, num_sets = nesting_boxes (box_list)
 
  # print the largest number of boxes that fit
  print (max_boxes)

  # print the number of sets of such boxes
  print (num_sets)

if __name__ == "__main__":
  main()

