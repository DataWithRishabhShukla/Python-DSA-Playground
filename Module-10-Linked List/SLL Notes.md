### Topic - SLL 

#### Singly Linked List
- We need to give curr != None only when we in case of searching and printing the elements.
- In the other cased we need not traverse till the last element .
- 

```python
def print_list(head):
    curr = head
    while curr != None:
        print(curr.key, end = " ")
        curr = curr.next

def search(head, x):
    curr = head 
    pos = 0
    while curr != None :
        pos = pos + 1
        if curr.key == x:
            return pos
        curr = curr.next
    return -1 

def insert_at_end(head,key):
    node = Node(key)

    if  head == None:
        return node
    curr = head
    while curr.next != None:
        curr = curr.next

    curr.next = node
    return head
```

### Finding Middle of SLL
- if we don't use and in [while fast != None and fast.next != None] , then slow pointed will be stuck .
```python
def print_middle(head):
    if head == None:
        return None 
    
    curr = head
    pos = 0
    while curr != None :
        curr = curr.next
        pos = pos + 1
    
    curr = head
    for i in range(pos//2):
        curr = curr.next
    print(curr.key)

# Using the single traversal
def print_middle_efficient(head):
    if head == None:
        return None 
    
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next 
    print(slow.key)
```

### nth node from the last 
- we need find nth node from last in liked list.
- Last node index is - 1
- 
```python

```