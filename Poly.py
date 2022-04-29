#  File: Poly.py

#  Description: Adds and multiplies polynomials formatted in linked lists

#  Student Name: Monish Jayakumar

#  Student UT EID: mj27639

#  Partner Name: Talah El-Zein

#  Partner UT EID: the272

#  Course Name: CS 313E

#  Unique Number: 52590

#  Date Created: 11/5

#  Date Last Modified: 11/6

import sys

class Link (object):
  def __init__ (self, coeff = 1, exp = 1, next = None):
    self.coeff = coeff
    self.exp = exp
    self.next = next

  def __str__ (self):
    return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'
  
  # returns formatted str of link
  def format(self):
    return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

class LinkedList (object):
  def __init__ (self):
    self.head = None
    self.numElements = 0
  
  # inserts link in linkedlist
  def insert_last (self, coeff, exp): 
    new_link = Link(coeff, exp)
    self.numElements += 1

    current = self.head
    # if list is empty just add newLink as the head
    if current == None:
      self.head = new_link
      return

    while current.next != None:
      current = current.next

    current.next = new_link

  # finds link in unordered linkedlist
  def find_unordered (self, exp):
    current = self.head
    if current == None:
        return None
    # search through whole list till found
    while current.exp != exp:
        if (current.next == None):
            return None
        else:
            current = current.next
    return current

  # returns copy of list
  def copy_list (self):
    lst = LinkedList()
    current = self.head
    # loop through list and add links
    for i in range(self.numElements):
      newLink = current
      lst.insert_last(newLink.coeff, newLink.exp)
      current = current.next
    return lst

  # keep Links in descending order of exponents
  def insert_in_order (self, coeff, exp):
    self.numElements += 1
    newLink = Link(coeff, exp)
    # if head is null
    if (self.head == None):
        self.head = newLink
        return

    previous = self.head
    current = self.head

    # if exp is already greater than current exp
    if (exp > current.exp):
      newLink.next = self.head
      self.head = newLink
      return

    # while current exp >= data keep searching 
    while (current.exp >= exp):
        if (current.next == None):
            current.next = newLink
            return
        else:
            previous = current
            current = current.next
    
    previous.next = newLink
    newLink.next = current

  # deletes link from linked list
  def delete_link (self, exp):
  
    previous = self.head
    current = self.head

    if current == None:
        return None
    
    
    #while current data is not the data we're looking for, move current pointer forwards
    while (current.exp != exp):
        if (current.next == None):
            return None
        else:
            previous = current
            current = current.next
     
    if (current == self.head):
        self.head = self.head.next
    else:
        previous.next = current.next

    self.numElements -= 1
    return current

  # simplifies linkedlist to remove 0 coefficients and add coeeficients of equal exponents
  def simplify(self):
    result = LinkedList()
    current1 = self.head
    bigExp = current1.exp
    if current1 == None:
      return 
    for i in range(bigExp + 1):
      s = 0
      current1 = self.head
      for j in range(self.numElements):
        if current1.exp == i:
          s += current1.coeff
        current1 = current1.next
      if s != 0:
        result.insert_in_order(s, i)

    return result

  # add polynomial p to this polynomial and return the sum
  def add (self, p):
    result = LinkedList()
    copy1 = self.copy_list()
    copy2 = p.copy_list()
    current1 = copy1.head
    current2 = copy2.head
    # for every element in self, loop through p
    for i in range(self.numElements):
      for j in range(p.numElements):
        # if we get to end of LL, add insert result link
        if current2.next == None:
          result.insert_in_order(current1.coeff, current1.exp)
          break
        # if equal exponent is found, add coefficents and insert link
        if (current1.exp == current2.exp):
          s = current1.coeff + current2.coeff
          result.insert_in_order(s, current1.exp)
          copy2.delete_link(current2.exp)
          break
        current2 = current2.next
      # move outer LL link forward, reset inner LL to beginning 
      current1 = current1.next
      current2 = copy2.head

    current3 = copy2.head
    # loop through links left over in the inner loop LL
    for k in range(copy2.numElements):
      # add to result
      result.insert_in_order(current3.coeff, current3.exp)
      current3 = current3.next
    result = result.simplify()
    return result

  # multiply polynomial p to this polynomial and return the product
  def mult (self, p):
    result = LinkedList()
    current1 = self.head
    current2 = p.head
    # for every element in self, loop through p
    for i in range(self.numElements):
      for j in range(p.numElements):
        exp = current1.exp + current2.exp
        coeff = current1.coeff * current2.coeff
        # check if same exp already exists in result
        link = result.find_unordered(exp)
        # if not, add link
        if (link == None):
          result.insert_in_order(coeff, exp)
        # if it does, add coefficients
        else:
          link.coeff += coeff
        current2 = current2.next
      current1 = current1.next
      current2 = p.head

    result = result.simplify()
    return result

  # create a string representation of the polynomial
  def __str__ (self):
    result = ''
    current = self.head
    for i in range(self.numElements):
      if current.next != None:
        result += current.format() + ' + '
      else:
        result += current.format()
      current = current.next
    return result
def main():
  # read data from file poly.in from stdin
  # create polynomial p
    n = int(sys.stdin.readline())
    coeff = []
    exp = []
    p = LinkedList()
    for i in range(n):
      nums = sys.stdin.readline().strip().split(' ')
      #print(nums)
      p.insert_in_order(int(nums[0]), int(nums[1])) 
    sys.stdin.readline()
    p = p.simplify()
    #print(p)
    m = int(sys.stdin.readline())
    q = LinkedList()
    # create polynomial q
    for i in range(m):
      nums = sys.stdin.readline().strip().split(' ')
      q.insert_in_order(int(nums[0]), int(nums[1])) 
    #print(q)
    q = q.simplify()
    #print(q)

  # get sum of p and q and print sum
    result = p.add(q)
    print(result)
  # get product of p and q and print product
    prod = p.mult(q)
    print(prod)
if __name__ == "__main__":
  main()