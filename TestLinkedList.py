#  File: TestLinkedList.py

#  Description: set of linkedlist functions including insert, delete, find, merge, sort

#  Student Name: Monish Jayakumar

#  Student UT EID: mj27639

#  Partner Name: Talah El-Zein

#  Partner UT EID: the272

#  Course Name: CS 313E

#  Unique Number: 52590

#  Date Created: 10/29

#  Date Last Modified: 10/31

from typing import NewType


class Link (object):
  def __init__(self, data, next = None):
      self.data = data
      self.next = None
  
  def __str__ (self):
    return str(self.data)
  
  def __le__ (self, other):
    return self.data <= other.data
  
  
class LinkedList (object):
  # create a linked list
  # you may add other attributes
  def __init__ (self):
    self.head = None
    self.tail = None
    self.numElements = 0

  # get number of links 
  def get_num_links (self):
    return self.numElements
    
  # add an item at the beginning of the list
  def insert_first (self, data): 
    new_Link = Link(data)
    # newLink points to head
    new_Link.next = self.head
    # head is now newLink
    self.head = new_Link
    self.numElements += 1
    

  # add an item at the end of a list
  def insert_last (self, data): 
    new_link = Link(data)
    self.numElements += 1

    current = self.head
    # if list is empty just add newLink as the head
    if current == None:
      self.head = new_link
      return

    while current.next != None:
      current = current.next

    current.next = new_link

  # searches for specific link in data
  def find_link(self, data):
    current = self.head
    # is list is empty return none
    if current == None:
        return None
    # while current link is not the one we're searching for
    while current.data != data:
        if (current.next == None):
            return None
        else:
            current = current.next
    return current

  # add an item in an ordered list in ascending order
  # assume that the list is already sorted
  def insert_in_order (self, data): 
    newLink = Link(data)
    self.numElements += 1
    # if head is null
    if (self.head == None):
        self.head = newLink
        return

    previous = self.head
    current = self.head

    # if data is already less than current data
    if (data < current.data):
      newLink.next = self.head
      self.head = newLink
      return

    # while current Link <= data keep searching 
    while (current.data <= data):
        if (current.next == None):
            current.next = newLink
            return
        else:
            previous = current
            current = current.next
    
    previous.next = newLink
    newLink.next = current
    
  # search in an unordered list, return None if not found
  def find_unordered (self, data):
    current = self.head
    if current == None:
        return None
    # search through whole list till found
    while current.data != data:
        if (current.next == None):
            return None
        else:
            current = current.next
    return current 
  # Search in an ordered list, return None if not found
  def find_ordered (self, data):
    current = self.head
    if current == None:
        return None
    # search through whole list while current data <= data
    while current.data <= data:
        if (current.data == data):
            return current
        if (current.next == None):
            return None
        else:
            current = current.next
  # Delete and return the first occurrence of a Link containing data
  # from an unordered list or None if not found
  def delete_link (self, data):
    previous = self.head
    current = self.head

    if current == None:
        return None
    
    #while current data is not the data we're looking for, move current pointer forwards
    while (current.data != data):
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

  # String representation of data 10 items to a line, 2 spaces between data
  def __str__ (self):
    count = 1
    current = self.head
    string = ''
    while (current != None):
        # for every 10th link add a newline character
        if count % 10 == 0 and count != 1:
          string += str(current.data) + '  '
          string += '\n'
        else:
          # add link and 2 spaces
          string += str(current.data) + '  '
        current = current.next
        count += 1
    return string
  
  # Copy the contents of a list and return new list
  # do not change the original list
  def copy_list (self):
    lst = LinkedList()
    current = self.head
    # loop through list and add links
    for i in range(self.numElements):
      newLink = current
      lst.insert_last(newLink.data)
      current = current.next
    return lst

  # Reverse the contents of a list and return new list
  # do not change the original list
  def reverse_list (self): 
    lst = LinkedList()
    current = self.head
    # loop through list and insert_first for each element 
    for i in range(self.numElements):
      newLink = current
      lst.insert_first(newLink.data)
      current = current.next
    return lst
  # Sort the contents of a list in ascending order and return new list
  # do not change the original list
  def sort_list (self): 
    lst = LinkedList()
    current = self.head
    # using new list use insert_in_order to insert sorted
    for i in range(self.numElements):
      newLink = current
      lst.insert_in_order(newLink.data)
      #print(lst)
      current = current.next
    return lst

  # Return True if a list is sorted in ascending order or False otherwise
  def is_sorted (self):
    # create new sorted version of list
    lst = self.sort_list()
    # check if sorted version = original version
    return self.is_equal(lst)

  # Return True if a list is empty or False otherwise
  def is_empty (self): 
    return self.numElements == 0

  # Merge two sorted lists and return new list in ascending order
  # do not change the original lists
  def merge_list (self, other): 
    lst = LinkedList()
    current = self.head
    current2 = other.head
    length = min(self.numElements, other.numElements)

    # loop through both Lists till the length of smallest list
    while (current != None and current2 != None):
    #for i in range(length):
      if (current.data > current2.data):
        lst.insert_last(current2.data)
        current2 = current2.next
      else:
        lst.insert_last(current.data)
        current = current.next
    
    # add in remaining links
    while (current != None):
      lst.insert_last(current.data)
      current = current.next
        
    # add in remaining links
    while (current2 != None):
      lst.insert_last(current2.data)
      current2 = current2.next

    return lst
  # Test if two lists are equal, item by item and return True
  def is_equal (self, other):
    if (self.numElements != other.numElements):
      return False
    current = self.head
    current2 = other.head
    # loop through list and check if each link = the other link
    for i in range(self.numElements):
      if (current.data != current2.data):
        return False
      else:
        current = current.next
        current2 = current2.next
    return True
  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  # do not change the original list
  def remove_duplicates (self):
    lst = self.copy_list()
    memo = []
    current = lst.head
    previous = lst.head
    # use memo to keep track of data we've seen
    while (current != None):
      # if element is not dup
      if current.data not in memo:       
        memo.append(current.data)
        previous = current
      # if element is dup which means its in the memo, delete it
      else:
        previous.next = current.next
      current = current.next
    return lst
  
  
def main():
  # Test methods insert_first() and __str__() by adding more than
  # 10 items to a list and printing it.
  lst = LinkedList()
  for i in range(15,0,-1):
    lst.insert_first(i)
  #print(lst)
  # Test method insert_last()
  #lst.insert_last(16)
  #print(lst)

  # Test method insert_in_order()
  #lst.insert_in_order(0)
  #print(lst)

  # Test method get_num_links()
  # print(lst.get_num_links())

  # Test method find_unordered() 
  # Consider two cases - data is there, data is not there 
  lst2 = LinkedList()
  lst2.insert_first(1)
  lst2.insert_first(27)
  lst2.insert_first(13)
  lst2.insert_first(17)
  lst2.insert_first(-9)
  #print(lst2.find_unordered(27))
  #print(lst2.find_unordered(6))

   # Test method find_ordered() 
  # Consider two cases - data is there, data is not there 
  #print(lst.find_ordered(5))
  #print(lst.find_ordered(91))

  # Test method delete_link()
  # Consider two cases - data is there, data is not there 
  #print(lst.delete_link(6))
  #print(lst.delete_link(91))

  # Test method copy_list()
  lst.copy_list()
  #print(lst3)

  # Test method reverse_list()
  lst4 = lst.reverse_list()
  #print(lst4)

  # Test method sort_list()
  lst5 = lst2.sort_list()
  #print(lst5)
  
  # Test method is_sorted()
  # Consider two cases - list is sorted, list is not sorted

  #print(lst5.is_sorted())
  #print(lst2.is_sorted())

  # Test method is_empty()
  lst6 = LinkedList()
  #print(lst2.is_empty())
  #print(lst6.is_empty())

  # Test method merge_list()
  #print(lst5)
  #print()
  #lst7 = lst5.merge_list(lst5)
 # print(lst7)
  #print(lst)
  #print()
  #print(lst5)
  #print()
  lst8 = lst.merge_list(lst5)
  #print(lst7)
  #print(lst8)

  # Test method is_equal()
  # Consider two cases - lists are equal, lists are not equal
  lst9 = lst8.copy_list()
  #print(lst9.is_equal(lst8))
  #print(lst.is_equal(lst9))

  # Test remove_duplicates()
  lst.insert_in_order(6)
  lst.insert_first(15)
  lst.insert_last(1)
  lst.insert_last(7)
  lst = lst.sort_list()
  #print(lst)
  #print()
  lst = lst.remove_duplicates()
  #print(lst)

if __name__ == "__main__":
  main()