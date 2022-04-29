
#  Description: This program sorts a list of strings using queues.

import sys

class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue if empty
  def is_empty (self):
    return (len(self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len(self.queue))

# returns a sorted list of strings
def radix_sort (a):
  
  # finds the max length of the strings
  lst = [len(word) for word in a]
  max_len = max(lst)

  # format given list to add spaces
  format(a, max_len)

  # creates two lists to keep track of order after every enqueue and dequeue
  original_words = a[:]
  new_words = []
  # intialize list of queues
  queue_list = make_queue_list()

  # loop max_len times through 1 letter of each word at a time, starting at the end of the string
  for i in range(max_len - 1, -1, -1):
    # loops through each string and enqueues
    for word in original_words:
      ch = word[i]
      index = get_queue_index(ch)
      queue_list[index].enqueue(word)

    # loop through queue_list to add back to original
    for j in range(len(queue_list)):
      # loop until each 1d queue has no elements
      while queue_list[j].size() != 0:
        w = queue_list[j].dequeue()
        new_words.append(w)

    original_words = new_words[:]
    new_words = []

  # after the list is sorted, strip each string of the added spaces
  for i in range(len(original_words)):
    original_words[i] = original_words[i].strip()

  return original_words

def format(a, max_len):
  # adds max - len(word) spaces to end of each word
  for word in range(len(a)):
    while len(a[word]) < max_len:
      a[word] += ' '
    
# converts each string or num to specified queue and returns queue index
def get_queue_index(ch):
  
  # if char is a number
  if ch.isdigit():
    x = ord(ch)
    return x - 47
  
  # if char is a space
  elif ord(ch) == 32:
    return 0
  
  # if char is a lowercase letter
  else:
    x = ord(ch)
    return x - 86

def make_queue_list():
  queue_list = []
  
  # 37 lists to encompass the space, 10 numbers, and 26 letters
  for i in range(37):
    q = Queue()
    queue_list.append(q)
  
  return queue_list

def main():
  # read the number of words in file
  line = sys.stdin.readline()
  line = line.strip()
  num_words = int (line)

  # create a word list
  word_list = []
  for i in range (num_words):
    line = sys.stdin.readline()
    word = line.strip()
    word_list.append (word)

  # use radix sort to sort the word_list
  sorted_list = radix_sort (word_list)
  
  # print the sorted_list
  print(sorted_list)

if __name__ == "__main__":
  main()

    
