
#  Description: check if binary trees are similar, height function, gets all nodes at specific level and number of total nodes

import sys

class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return self.queue.pop(0)

  # check if the queue is empty
  def is_empty (self):
    return (len (self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len (self.queue))

class Node (object):
   def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lchild = lChild
        self.rchild = rChild
        self.lev = 0
    
   def __str__(self):
       return str(self.data)


class Tree (object):
  def __init__ (self):
      self.root = None

# insert data into the tree
  def insert (self, data):
    new_node = Node (data)
    if (self.root == None):
      self.root = new_node
      return
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (data < current.data):
          current = current.lchild
        else:
          current = current.rchild

      if (data < parent.data):
        parent.lchild = new_node
      else:
        parent.rchild = new_node

  # Returns true if two binary trees are similar
  def is_similar (self,pNode):
      pNode = pNode.root
      queue = Queue()
      memo = breadth_first(self.root, queue)
      memo2 = breadth_first(pNode, queue)
      return memo == memo2

  def get_level (self, level):
    if self.root == None:
        return []
    self.root.lev = 0
    #print(self.root.data)
    nodes = []
    queue = Queue()
    queue.enqueue(self.root)
    # loop till queue is empty
    while not queue.is_empty():
        # pop current node from queue
        current_node = queue.dequeue()

        # if current node is at level param, append to list
        if current_node.lev == level:
            nodes.append(current_node)

        # if node has right child, queue right child and increment right child's level
        if current_node.rchild != None: #   and current_node.lchild == None:
            queue.enqueue(current_node.rchild)
            current_node.rchild.lev = current_node.lev + 1

        # if node has left child, queue left child and increment left child's level
        if current_node.lchild != None: # and current_node.rchild == None:
            queue.enqueue(current_node.lchild)
            current_node.lchild.lev = current_node.lev + 1

    nodes = reversed(nodes)
    return nodes

  # Returns the height of the tree
  def get_height (self): 
      if self.root == None:
          return -1
      return self.heightHelper(self.root)

  def heightHelper(self, node):
       # use get_level until its None

       # if at leaf node, return 0
      if node.lchild == None and node.rchild == None:
          return 0
      # if theres left and right child, return max of both paths + 1
      elif node.lchild != None and node.rchild != None:
          return 1 + max(self.heightHelper(node.lchild), self.heightHelper(node.rchild))
      # if theres only right child, advance node and add 1
      elif node.rchild != None and node.lchild == None:
          return 1 + self.heightHelper(node.rchild)
      # if theres only left child, advance node and add 1
      elif node.lchild != None and node.rchild == None:
          return 1 + self.heightHelper(node.lchild)

  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree and the root
  def num_nodes (self):
      memo = [0]
      # traverses tree with a counter
      post_order2(self.root, memo)
      return memo[0]

def getLevels (node, queue, level):
    memo = []
    queue.enqueue(node)
    for i in range(level):
      memo = []
      for i in range(level):
        current_node = queue.dequeue()
        memo.append(current_node.data)
        if current_node.lchild != None:
            queue.enqueue(current_node.lchild)
        if current_node.rchild != None:
            queue.enqueue(current_node.rchild)
      print(memo)

    return memo

# returns breadth first search of binary tree
def breadth_first (node, queue):
    memo = []
    if node == None:
        return None
    queue.enqueue(node)
    # loop till queue is empty
    while not (queue.is_empty()):
        # current node is popped from queue
        current = queue.dequeue() 
        memo.append(current.data)
        if current.lchild != None:
            queue.enqueue(current.lchild)
        if current.rchild != None:
            queue.enqueue(current.rchild)

    return memo

def post_order2 (aNode, memo):
    if (aNode != None):
      post_order2 (aNode.lchild, memo)
      post_order2 (aNode.rchild, memo)
      # increment counter when at center node
      memo[0] += 1


def main():
    # Create three trees - two are the same and the third is different
    tree1 = Tree()
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list (map (int, line)) 	# converts elements into ints
    #print('input1', tree1_input)
    for num in tree1_input:
       tree1.insert(num)

    tree2 = Tree()
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list (map (int, line)) 	# converts elements into ints
    for num in tree2_input:
       tree2.insert(num)

    tree3 = Tree()
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list (map (int, line)) 	# converts elements into ints
    #print('input3', tree3_input)
    for num in tree3_input:
        tree3.insert(num)
    #print('root', tree3.root.data)

    # Test your method is_similar()
    #print(tree1.is_similar(tree2.root))
    
    # Print the various levels of two of the trees that are different
    tree3.get_level(1)

    # Get the height of the two trees that are different

    #print(tree3.get_height())

    # Get the total number of nodes a binary search tree
    #print(tree1.num_nodes())

if __name__ == "__main__":
  main()
