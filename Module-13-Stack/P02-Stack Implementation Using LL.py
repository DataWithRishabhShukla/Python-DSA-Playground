import math

class Node:
    def __init__(self,d):
        self.data = d
        self.next = None


class MyStack:
    def __init__(self):
        self.head = None 
        self.sz = 0

    def push(self,x):
        temp = Node(x)
        temp.next = self.head
        self.head = temp
        self.sz += 1
    
    def size(self):
        return self.sz
    
    def peek(self):
        if self.head is None:
            return math.inf
        return self.head.data
    
    def pop(self):
        if self.head is None:
            return math.inf
        res = self.head.data
        self.head = self.head.next
        self.sz -= 1
        return res

stack  = MyStack()
print(stack.pop())
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.size())
print(stack.pop())
print(stack.size())
print(stack.peek())