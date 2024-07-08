### Topic - Circular Linked List 

#### CLL Advantage
* we can traverse the whole list from any node
* Useful for implementing - Queue DS, Round Robin 
* We can insert at beginning and end by just maintaning one tail pointer 

#### CLL Disadvantage
* Implementations of operations become complex

#### Traversing the circular list 

```python 
# corner cases 
# 1. List is empty
# 2. List has 1 element 

def print_circular(head):
    if head == None:
        return None 
    print(head.key, end=" ")
    curr = head.next
    while curr != head:
        print(curr.key ,end=" ")
        curr = curr.next
```