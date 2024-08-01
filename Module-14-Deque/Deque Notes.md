###                  Deque

#### Video 1 
- Deque - Doubly ended queue 
- Allows insertion and deletion from both the ends 
- Index based access is pallowed
- Slicing is not allowed 
```python
from collections import deque
```
- Internally uses advance version of DLL
#### Deque Operation 
- InsertFront()
- InsertRear()
- DeleteFront()
- DeleteRear()
- isFull()
- isEmpty()
- size()
- getFront()
- getRear()

#### Deque Application 
- A deque can be used used as both stach and queue - LIFO and FIFO both can be implemented 
- Maintianing history of action 
- Manintaining priority queue with two types of priority 
- Maximum . Minimum of size k in  subarray in 
 

####  Deque Python 
Stack can be implemented using below in python.
1. Using List 
2. Using collections.deque
3. Using queue.LIFOQueue
4. Using our own implementation 

```python
"""
Using List 
    - cache friendly 
    - insertion and deletion in O(1) but worst case it can be Linear


Using deque
    - Not cache friendly 
    - Insertion and deletion is alwyas in O(1)
    - based on the doulbly linked list implementation 
"""
```

#### Video 3 Stack Implementation Custom 
```python 
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

```

#### Video 4 Application of Stack 
- Functions calls - recursive 
- Balanced parathesis [(a+b) *{c +(d-e)}]
- Reversing Items 
- Infix to postfix /prefix 
    - a+b -> Infix
    - +ab -> Prefix
    - ab+ -> Postfix
    - Infix is more human readable
    - but infix is difficult for compiler
    - so compilet would  convert the infix to prefix or postfix   
- Evaluation of postfix /prefix
- Stock span problem 
- Undo / Redo or Forward /Backward 