#  File: Hull.py

#  Description: This program determines the convex hull vertices and area of a set of points.

#  Student Name: Monish Jayakumar

#  Student UT EID: mj27639

#  Partner Name: Talah El-Zein

#  Partner UT EID: the272

#  Course Name: CS 313E

#  Unique Number: 52590

#  Date Created: 9/24

#  Date Last Modified: 9/26

import sys

import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)

# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det (p, q, r):
  x1 = int(p.x)
  x2 = int(q.x)
  x3 = int(r.x)
  y1 = int(p.y)
  y2 = int(q.y)
  y3 = int(r.y)
  # calculates determinant
  det = (x2 * y3 - y2 * x3) - (x1 * y3 - y1 * x3) + (x1 * y2 - y1 * x2)
  return det

# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull (sorted_points):
  upper_hull = []
  upper_hull.append(sorted_points[0])
  upper_hull.append(sorted_points[1])
  for i in range(2,len(sorted_points)):
    upper_hull.append(sorted_points[i])
    # while upper hull has 3 or more points and their determinant is positive
    while (len(upper_hull) >= 3 and det(upper_hull[-3],upper_hull[-2],upper_hull[-1]) > 0):
      upper_hull.pop(-2)

   

  lower_hull = []
  # adds last 2 elements of sorted points to lower hull
  lower_hull.append(sorted_points[-1])
  lower_hull.append(sorted_points[-2])
  for i in range(len(sorted_points) - 3,-1,-1):
    lower_hull.append(sorted_points[i])
    # while lower hull has 3 or more points and their determinant is positive
    while (len(lower_hull) >= 3 and det(lower_hull[-3],lower_hull[-2],lower_hull[-1]) > 0):
      lower_hull.pop(-2)

  # pops first and last value to avoid duplicate values
  lower_hull.pop(0)
  lower_hull.pop(-1)

  # appends lower hull to upper hull
  for i in lower_hull:
    upper_hull.append(i)

 
  return upper_hull

# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly (convex_poly):
  length = len(convex_poly)
  # intializes with edge determinant calculations
  det = convex_poly[-1].x * convex_poly[0].y - convex_poly[-1].y * convex_poly[0].x

  # calculates determinants according to formula of xn * yn+1 and yn * xn+1
  for i in range(length - 1):
    det += (convex_poly[i].x * convex_poly[i + 1].y )
  
  for i in range(length - 1):
    det -= (convex_poly[i].y * convex_poly[i + 1].x )

  return .5 * abs(det)

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  assert det(Point(2, 2), Point(3, 3), Point(4, 4)) == 0
  assert det(Point(0, 0), Point(5, 8), Point(3, -1)) == -29
  assert det(Point(-7, -8), Point(3, 20), Point(34, 87)) == -198
  assert convex_hull([Point(0, 6), Point(1, 3), Point(2, 5), Point(3, 7), Point(4, 4)]) == [(0, 6), (1, 3), (3, 7), (4, 4)]
  assert convex_hull([Point(-3, 1), Point(0, 5), Point(5, 0)]) == [(-3, 1), (5, 0), (0, 5)]
  assert convex_hull([Point(0, 0), Point(0, 2), Point(2, 0), Point(2, 2)]) == [(0, 0), (2, 0), (2, 2), (2, 0)]
  assert area_poly([Point(-3, 1), Point(5, 0), Point(0, 5)]) == 5
  assert area_poly([Point(0, 0), Point(2, 0), Point(2, 2), Point(2, 0)]) == 4
  assert area_poly([Point(1, 1), Point(1, 4), Point(4, 4), Point(4, 1)]) == 9
  print("all test cases passed")

def main():
  # create an empty list of Point objects
  points_list = []

  # read number of points
  line = sys.stdin.readline()
  line = line.strip()
  num_points = int (line)

  # read data from standard input
  for i in range (num_points):
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    x = int (line[0])
    y = int (line[1])
    points_list.append (Point (x, y))

  # sort the list according to x-coordinates
  sorted_points = sorted (points_list)
  
  # print the sorted list of Point objects
  # for p in sorted_points:
    # print(str(p))


  # get the convex hull
  hull = convex_hull(sorted_points)
  
  # run your test cases
  # test_cases()
  
  # print your results to standard output
  # print the convex hull
  print("Convex Hull")
  for i in range(len(hull)):
    print(str(hull[i]))
  print()
  # get the area of the convex hull
  area = area_poly(hull)
  # print the area of the convex hull
  print("Area of Convex Hull =", area)

if __name__ == "__main__":
  main()
