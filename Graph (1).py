#  File: Graph.py

#  Description: creates graph object with adjacency matrix with given input

#  Student Name: Monish Jayakumar

#  Student UT EID: mj27639

#  Partner Name: Talah El-Zein

#  Partner UT EID: the272

#  Course Name: CS 313E

#  Unique Number: 52590

#  Date Created: 11/19

#  Date Last Modified: 11/21

import sys

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append (item)

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check the item on the top of the stack
  def peek (self):
    return self.stack[-1]

  # check is the stack is empty
  def is_empty (self):
    return (len(self.stack) == 0)
  
  # check the number of elements in the stack
  def size (self):
    return (len (self.stack))


class Queue (object):
  def __init__ (self):
    self.queue = []

  def __str__(self):
    result = ''
    for i in self.queue:
      result += str(i) + ' '
    return result
  
  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # returns item at front of queue
  def peek (self):
    return self.queue[0]
  
  # remove an item from the beginning of the queue
  def dequeue (self):
    return self.queue.pop(0)

  # check if the queue is empty
  def is_empty (self):
    return (len (self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len (self.queue))

class Vertex (object):
    def __init__ (self, label):
        self.label = label
        self.visited = False
    
    # determine if vertex was visited
    def was_visited(self):
        return self.visited
    
    # return label of vertex
    def get_label(self):
        return self.label
    
    # string representation of vertex
    def __str__ (self):
        return str(self.label)

class Graph(object):
    def __init__ (self):
        self.Vertices = []
        # adjacency Matrix substitutes for edge class
        self.adjMat = []
    
    # check if vertex label is already in graph
    def has_vertex (self, label):
        nVert = len (self.Vertices)
        for i in range(nVert):
            if label == self.Vertices[i].get_label():
                return True
        return False
    
    def get_index (self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (label == self.Vertices[i].get_label()):
                return i
        return -1
    
    # adds vertex of given label to graph
    def add_vertex (self, label):
        if (self.has_vertex(label)):
            return
        
        # add vertex to list of vertices
        self.Vertices.append(Vertex(label))
        
        # adds new column to adjacency matrix
        nvert = len(self.Vertices)
        for i in range(nvert - 1):
            self.adjMat[i].append(0)
        
        # adds new row for new vertex at bottom
        new_row = []
        for i in range(nvert):
            new_row.append(0)
        self.adjMat.append(new_row)
    
    # add weighted directed edge to graph
    def add_directed_edge (self, start, finish, weight = 1):
        self.adjMat[start][finish] = weight
    
     # add weighted undirected edge to graph
    def add_undirected_edge (self, start, finish, weight = 1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight
    
    # return an unvisited vertex adjacent to vertex v (index)
    def getAdjUnvisitedVertex(self, v):
      #print(v)
      nVert = len(self.Vertices)
      for i in range(nVert):
        # no edge means 0 in adjacency matrix, so > 0 means there's an edge connecting vertex v to vertex i
        if (self.adjMat[v][i] > 0) and not(self.Vertices[i].was_visited()):
          return i
      return -1
      
    # Depth First Search (DFS) thru graph
    def dfs (self, v):
        # create stack
        stack = Stack()
        
        # mark vertex v as visited and push to stack
        (self.Vertices[v]).visited = True
        print(self.Vertices[v])
        stack.push(v)
        
        # visit the other vertices 
        while (not stack.is_empty()):
          # get adjacent unvisited vertex
          u = self.getAdjUnvisitedVertex(stack.peek())
          #print('u',u)
          if (u == -1):
            u = stack.pop()
          else:
            (self.Vertices[u]).visited = True
            #print('lol')
            print(self.Vertices[u])
            stack.push(u)
        
        # the stack is empty, let us reset the 
        nVert = len(self.Vertices)
        for i in range(nVert):
          (self.Vertices[i]).visited = False
        
    # do breadth first search (BFS)
    def bfs(self, v):
      
      # checks if v has no adj unvisited vertex
      if self.getAdjUnvisitedVertex(v) == -1:
        return 
      
      # create queue
      queue = Queue()
      
      # mark starting vertex
      (self.Vertices[v]).visited = True
      print(self.Vertices[v])
      queue.enqueue(v)

      # visit adj unvisited vertex
      #a = self.getAdjUnvisitedVertex(v)
     # print(self.Vertices[a])
      #(self.Vertices[a]).visited = True
     # queue.enqueue(a)
        
      while (not queue.is_empty()):
         # get adjacent unvisited vertex
          u = self.getAdjUnvisitedVertex(queue.peek())
          # if current vertex has no adjacent unvisited vertex, dequeue to find new current vertex
          if (u == -1):
            u = queue.dequeue()
          # if current vertex has available vertex, mark as visited and enqueue
          else:
            (self.Vertices[u]).visited = True
            print(self.Vertices[u])
            queue.enqueue(u)
        
      # the queue is empty, reset visited to False 
      nVert = len(self.Vertices)
      for i in range(nVert):
        (self.Vertices[i]).visited = False
      
    
    # delete an edge from the adjacency matrix
    # delete a single edge if the graph is directed
    # delete two edges if the graph is undirected
    def delete_edge (self, fromVertexLabel, toVertexLabel):
      # convert labels to indexes
      fromVertex = self.get_index(fromVertexLabel)
      toVertex = self.get_index(toVertexLabel)
      
      # if edge is undirected, delete both edges
      if self.adjMat[fromVertex][toVertex] == self.adjMat[toVertex][fromVertex]:
        #print('lol')
        self.adjMat[fromVertex][toVertex] = 0
        self.adjMat[toVertex][fromVertex] = 0
      
      # if edge is directed, delete on edge
      else:
        self.adjMat[fromVertex][toVertex] = 0
                    
    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def delete_vertex (self, vertexLabel):
      # checks if given vertex is in vertex list
      if not self.has_vertex(vertexLabel):
        return 
      
      vertexIndex = self.get_index(vertexLabel)
      nVert = len(self.Vertices)
      
      # removes edges from adjacency matrix
      for i in range(nVert):
        self.adjMat[vertexIndex][i] = 0
        self.adjMat[i][vertexIndex] = 0
      
      # removes vertex from list
      self.Vertices.pop(vertexIndex)
      self.adjMat.pop(vertexIndex)
      for i in self.adjMat:
        i.pop(vertexIndex)
    
    def printAdjMat(self):
      for i in range(len(self.adjMat)):
        for j in range(len(self.adjMat[0])):
          if j == len(self.adjMat[0]) - 1:
            print(self.adjMat[i][j], end = '')
          else:
            print(self.adjMat[i][j], end = ' ')
        print()
      
def main():
  # create Graph Object
  cities = Graph()
  
  # read number of vertices
  nVert = int(sys.stdin.readline().strip())
  
  # read vertices into the list of Vertices
  for i in range(nVert):
    city = sys.stdin.readline().strip()
    cities.add_vertex(city) 
    #print(city)
  
  # read number of edges
  numEdges = int(sys.stdin.readline().strip())
  #print(numEdges)
  
  # read each edge and place in adjacency matrix
  for i in range (numEdges):
    edge = sys.stdin.readline().strip().split()
    start = int(edge[0])
    finish = int(edge[1])
    weight = int(edge[2])
    
    cities.add_directed_edge(start, finish, weight)
    #print(cities.adjMat)
  # read starting vertex for dfs and bfs
  startVertex = sys.stdin.readline().strip()
  
  # get index of starting vertex
  startIndex = cities.get_index (startVertex)
  
  # test DFS
  print("Depth First Search")
  cities.dfs(startIndex)
  print()
  
  # test breadth first search
  print("Breadth First Search")
  cities.bfs(startIndex)
  print()
  
  # test deletion of an edge
  print("Deletion of an edge")
  z = sys.stdin.readline().strip().split()
  cities.delete_edge(z[0], z[1])
  print()
  print("Adjacency Matrix")
  cities.printAdjMat()
  
  # test deletion of a vertex
  city = sys.stdin.readline().strip()
  cities.delete_vertex(city)
  print()
  print('Deletion of a vertex')
  print()
  print("List of Vertices")
  for i in range(len(cities.Vertices)):
    print(cities.Vertices[i].get_label())
  print()
  print("Adjacency Matrix")
  cities.printAdjMat()
  print()
  
if __name__ == "__main__":
  main()