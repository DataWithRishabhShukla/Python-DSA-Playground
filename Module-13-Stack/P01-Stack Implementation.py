
#using the list data structures 
print("\n\nStack implementation using the deque!!")
stack = []
stack.append(10) #Insertion 
stack.append(20) #Insertion 
stack.append(30) #[10, 20, 30] 

print(stack.pop()) # deletion 
top = stack[-1]
print(top)

size = len(stack)
print(size)


"""
Using List 
    - cache friendly 
    - insertion and deletion in O(1) but worst case it can be Linear


Using deque
    - Not cache friendly 
    - Insertion and deletion is alwyas in O(1)
    - based on the doulbly linked list implementation 
"""


from collections import deque

print("\n\nStack implementation using the deque!!")
stack = deque()
print(type(stack))
stack.append(10)
stack.append(20)
stack.append(30)

print(stack.pop())

top = stack[-1]
print(top)

size = len(stack)
print(size)