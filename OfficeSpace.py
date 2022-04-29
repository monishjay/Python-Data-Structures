#  File: OfficeSpace.py

#  Description: This program uses inputted coordinates of cubicle spaces and returns the office's area distribution.

#  Student Name: Talah El-Zein

#  Student UT EID: the272

#  Partner Name: Monish Jayakumar

#  Partner UT EID: mj27639

#  Course Name: CS 313E

#  Unique Number: 52590

#  Date Created: 09/23/2021 at 2:00 PM

#  Date Last Modified: 09/24/2021 at 12:21 PM

import sys

# returns the area of rect
def area (rect):
    area = (rect[2] - rect[0]) * (rect[3] - rect[1])
    return area

# returns a tuple of 4 integers denoting the overlapping rectangle.
def overlap (rect1, rect2):
    area = max(min(rect1[2], rect2[2]) - max(rect1[0], rect2[0]), 0) * max(min(rect1[3], rect2[3]) - max(rect1[1], rect2[1]), 0)

    # if no overlap
    if area <= 0:
        return (0,0,0,0)
    
    # if rect1 is in rect2
    elif rect2[0] <= rect1[0] <= rect2[2] and rect2[0] <= rect1[3] <= rect2[2]:
        if rect2[1] <= rect1[1] <= rect2[3] and rect2[1] <= rect1[3] <= rect2[3]:
            return rect1

    # if rect2 is in rect1
    elif rect1[0] <= rect2[0] <= rect1[2] and rect1[0] <= rect2[3] <= rect1[2]:
        if rect1[1] <= rect2[1] <= rect1[3] and rect1[1] <= rect2[3] <= rect1[3]:
            return rect2
        
    # checks which rectangle is on top of the other
    elif rect2[2] >= rect1[2] and rect2[3] >= rect1[3]:
        return (rect2[0], rect2[1], rect1[2], rect1[3])
    else:
        return (rect1[0], rect1[1], rect2[2], rect2[3]) 

# returns the area of unallocated space in the office
def unallocated_space (bldg):
    count = 0
    
    for row in bldg:
        for colm in row:
            if colm == 0:
                count += 1

    return count

# returns the area of contested space in the office
def contested_space (bldg):
    count = 0
    
    for row in bldg:
        for colm in row:
            if colm > 1:
                count += 1
                
    return count

# returns the area of uncontested space the employee gets
def uncontested_space (bldg, rect):
    count = 0
    
    x1 = int(rect[0])
    y1 = int(rect[1])
    x2 = int(rect[2])
    y2 = int(rect[3])
    for j in range(y1, y2):
        for k in range(x1, x2):
            if bldg[j][k] == 1:
                count += 1
                
    return count      

# returns a 2-D list of integers representing the office building and showing how many employees want each cell in the 2-D list
def request_space (office, cubicles):
    
    bldg = [[0 for i in range(office[2])] for i in range(office[3])]

    for i in range(len(cubicles)):
        x1 = cubicles[i][0]
        y1 = cubicles[i][1]
        x2 = cubicles[i][2]
        y2 = cubicles[i][3]
        for j in range(y1, y2):
            for k in range(x1, x2):
                bldg[j][k] += 1

    return bldg

# test cases for a few functions
def test_cases ():
    assert area ((0, 0, 2, 2)) == 2
    assert overlap ((0, 0, 3, 3,), (1, 1, 2, 2)) == (1, 1, 2, 2)

    return "all test cases passed"

def main():
    # reads office grid dimensions
    grid_dim = sys.stdin.readline().strip().split()
    grid_x2 = int(grid_dim[0])
    grid_y2 = int(grid_dim[1])
    grid_area = grid_x2 * grid_y2

    num_ppl = int(sys.stdin.readline().strip())
    
    ppl_info = []
    ppl_names = []

    # appends each person's info to ppl_info
    for i in range(num_ppl):
        person = sys.stdin.readline().strip().split()
        ppl_names.append(person[0])
        ppl_info.append(person)

    # creates office rect
    office = (0, 0, grid_x2, grid_y2)
    
    cubicles = []

    # appends tuple info for each person to cubicles
    for i in range(num_ppl):
        coord = (int(ppl_info[i][1]), int(ppl_info[i][2]), int(ppl_info[i][3]), int(ppl_info[i][4]))
        cubicles.append(coord)

    # creates populated bldg
    bldg = request_space(office, cubicles)

    # run your test cases
    '''
    print (test_cases())
    '''

    # print the following results after computation

    # compute the total office space
    print("Total", grid_area)

    # compute the total unallocated space
    print("Unallocated", unallocated_space(bldg))

    # compute the total contested space
    print("Contested", contested_space(bldg))
    
    # compute the uncontested space that each employee gets
    for i in range(len(ppl_names)):
        print(ppl_names[i], uncontested_space(bldg, cubicles[i]))

if __name__ == "__main__":
  main()
