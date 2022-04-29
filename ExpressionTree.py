
#  Description: Computes mathematical expression through the use of binary trees and stacks

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    # returns top of stack
    def peek(self):
        return self.stack[0]
    
    def __str__(self):
        s = ''
        for i in range(len(self.stack)):
            s += str((self.stack[i]))
        return s
    
class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree (object):
    def __init__ (self):
        self.root = None
    
    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree (self, expr):
        stack = Stack()
        expr = expr.split(' ')
        self.root = Node(expr[0])
        current = self.root
        # loop through expression
        for ch in expr:
            if ch == ' ':
                continue
            newNode = Node(ch)
            if ch == '(':
                current.lChild = newNode
                stack.push(current)
                current = newNode
            # if operator
            elif ch in operators:
                current.data = ch
                stack.push(current)
                current.rChild = newNode
                current = newNode
            # if is number
            elif isNumber(ch):
                current.data = ch
                if not stack.is_empty():
                    current = stack.pop()
            # if right parenthesis and stack not empty
            if ch == ')' and not stack.is_empty():
                current = stack.pop()
            #print('current',current.data)

                
    # when parsing infix
   # def in_order(self, aNode):
      #  if (aNode != None):
      #      self.in_order(aNode.lChild)
       #     #print(aNode.data, end = ' ')
         #   self.in_order(aNode.rChild)
                
    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):
        string = self.post_order(self.root)
        theStack = Stack()
        tokens = string.strip().split(' ')
        #print(tokens)
        # loop through tokens
        for item in tokens:
            if (item in operators):
                oper2 = theStack.pop()
                oper1 = theStack.pop()
                # push evaluated expression onto stack
                theStack.push (self.operate (oper1, oper2, item))
            else:
                theStack.push (item)
            #print(theStack)
            #print(theStack.peek())
            #print()
        #theStack.pop()
        return float(theStack.pop())
    
    # evaluates given expression
    def operate (self,oper1, oper2, token):
        expr = str(oper1) + token + str(oper2)
        #print(expr)
        return eval (expr)       
    
    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
        string = ''
        # iterate through binary tree in form of root(print), left, right
        if (aNode != None):
            string += str((aNode.data)) + ' '
            string += self.pre_order(aNode.lChild)
            string += self.pre_order(aNode.rChild)
        return string

    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):
        string = ''
        # iterate through binary tree in form of left, right, root(print)
        if (aNode != None):
            string += self.post_order(aNode.lChild)
            string += self.post_order(aNode.rChild)
            string += str((aNode.data)) + ' '
        return string
    
# checks if input num is a valid number   
def isNumber(num):
    str = '0123456789.-'
    for d in num:
        if (d not in str):
            return False
    return True
                
# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
 
    tree = Tree()
    tree.create_tree(expr)
    #tree.in_order(tree.root)
    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()
