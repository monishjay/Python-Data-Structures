
#  Description: Utilizes topological sort to sort a directed graph

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

  # check if the stack if empty
  def is_empty (self):
    return (len (self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len (self.stack))


class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

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
    self.inDeg = 0

  # determine if a vertex was visited
  def was_visited (self):
    return self.visited

  # determine the label of the vertex
  def get_label (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)


class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []

  # check if a vertex is already in the graph
  def has_vertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return True
    return False

  # given the label get the index of a vertex
  def get_index (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def add_vertex (self, label):
    if (self.has_vertex (label)):
      return

    # add vertex to the list of vertices
    self.Vertices.append (Vertex (label))

    # add a new column in the adjacency matrix
    nVert = len (self.Vertices)
    for i in range (nVert - 1):
      (self.adjMat[i]).append (0)

    # add a new row for the new vertex
    new_row = []
    for i in range (nVert):
      new_row.append (0)
    self.adjMat.append (new_row)

  # add weighted directed edge to graph
  def add_directed_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def add_undirected_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # return vertexes adjacent to vertex v (index)
  def get_neighbors(self, v):
    nVert = len (self.Vertices)
    lst = []
    for i in range (nVert):
      # checks if there is a connecting edge
      if (self.adjMat[v][i] > 0):
        lst.append(i)
    return lst
  
  # return an unvisited vertex adjacent to vertex v (index)
  def get_adj_unvisited_vertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
        return i
    return -1

  # determine if a directed graph has a cycle
  # this function should return a boolean and not print the result
  def has_cycle (self):
    count = 0
    for i in range(len(self.Vertices)):
      if self.dfs_check(i):
        #print('lol')
        return True
    return False
      
  # do a depth first search in a graph
  def dfs_check (self, v):
    # create the Stack
    theStack = Stack ()

    # mark the vertex v as visited and push it on the Stack
    (self.Vertices[v]).visited = True
    #print (self.Vertices[v])
    theStack.push (v)
    neighbors = []
    # visit all the other vertices according to depth
    while (not theStack.is_empty()):
      # get an adjacent unvisited vertex
      vertices = theStack.peek()
      #print(v)
      neighbors = self.get_neighbors(vertices)
      #print(self.Vertices[vertices], neighbors)
      #print(self.Vertices[v], neighbors)
      if v in neighbors:
        return True
      u = self.get_adj_unvisited_vertex (theStack.peek())
      #print(self.Vertices[u])
      if (u == -1):
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        #print (self.Vertices[u])
        theStack.push (u)
    for i in range(len(self.Vertices)):
      self.Vertices[i].visited = False
  # do a depth first search in a graph
  def dfs (self, v):
  
    # create the Stack
    theStack = Stack ()

    # mark the vertex v as visited and push it on the Stack
    (self.Vertices[v]).visited = True
    #print (self.Vertices[v])
    theStack.push (v)

    # visit all the other vertices according to depth
    while (not theStack.is_empty()):
      # get an adjacent unvisited vertex
      u = self.get_adj_unvisited_vertex (theStack.peek())
      if (u == -1):
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        #print (self.Vertices[u])
        theStack.push (u)

    # the stack is empty, let us rest the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

 # return a list of vertices after a topological sort
  # this function should not print the list
  def toposort (self):
    queue = Queue()
    # determines inDegree for all vertices
    for i in range(len(self.Vertices)):
        label = self.Vertices[i].label
        inDegree = self.getInDegree(label)
        #print(inDegree)
        self.Vertices[i].inDeg = inDegree
        #print(self.Vertices[i].label, self.Vertices[i].inDeg)
    count = 0
    # loop till list of vertices is empty
    while (len(self.Vertices) != 0):
      lst = []
      for i in range(len(self.Vertices)):
        vertex = self.Vertices[i]
        #print(self.Vertices[i].label, self.Vertices[i].inDeg)
        if vertex.inDeg == 0:
          lst.append(vertex.label)
          #print('lst',lst)
      for vertex in lst:
        self.delete_vertex(vertex)
      #print(queue.queue)
      
      lst = sorted(lst)
      for i in lst:
        queue.enqueue(i)
      if count == 10:
        break
      count += 1
      # updates inDegree for all vertices after deletion
      for i in range(len(self.Vertices)):
        inDegree = self.getInDegree(self.Vertices[i].label)
        self.Vertices[i].inDeg = inDegree
        #print(self.Vertices[i], self.Vertices[i].inDeg)
    return queue.queue 
    
  # returns in degree of vertex
  def getInDegree(self, vertex):
    vertex = self.get_index(vertex)
    nVert = len(self.Vertices)
    count = 0
    for row in range(nVert):
      if self.adjMat[row][vertex] == 1:
        count += 1
    return count

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
        
  # do the breadth first search in a graph
  def bfs (self, v):
    return

def main():
  # create the Graph object
  cities = Graph()

  # read the number of vertices
  line = sys.stdin.readline()
  line = line.strip()
  num_vertices = int (line)

  # read the vertices to the list of Vertices
  for i in range (num_vertices):
    line = sys.stdin.readline()
    city = line.strip()
    cities.add_vertex (city)

  # read the number of edges
  line = sys.stdin.readline()
  line = line.strip()
  num_edges = int (line)

  # read each edge and place it in the adjacency matrix
  for i in range (num_edges):
    line = sys.stdin.readline()
    edge = line.strip()
    edge = edge.split()
    start =  (edge[0])
    finish =  (edge[1])

    start = cities.get_index(start)
    finish = cities.get_index(finish)
    cities.add_directed_edge (start, finish)
  
  if (cities.has_cycle()):
    print("The Graph has a cycle.")   
  else:
    print("The Graph does not have a cycle.")  
  print()
  if not (cities.has_cycle()):
    print("List of vertices after toposort")
    print(cities.toposort())
  print()
  
if __name__ == "__main__":
  main()

