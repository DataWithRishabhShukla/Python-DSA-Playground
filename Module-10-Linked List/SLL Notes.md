### Topic - SLL 

#### Singly Linked List
- We need to give curr != None only when we in case of searching and printing the elements.
- In the other cased we need not traverse till the last element .


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

```python
def nth_element_from_end(head,e):
    if head == None :
        return None
    
    curr = head
    count = 0

    while curr != None :
        count = count + 1 
        curr = curr.next 

    if e > count :
        return None


    # print(f"\n\nLegth of list is  : {count}")
    # print(f"Legth - index {e}  : {count-e}")
    curr = head 
    for i in range(count-e):
        curr = curr.next

    print(f"\n{e}th element from end is : {curr.key}")

# using the two pointer approach

def nth_element_from_end_two_pntr(head,n):
    if head == None:
        return None
    
    first = head 
    for i in range(n):
        if first == None:
            return
        first = first.next

    second = head
    while first != None:
        first = first.next
        second = second.next 
    print(f"\n{n}th element in the SLL is :{second.key}")
```

### remove duplicates from the sorted linked list 

```python
def remove_duplicates_from_sll(head):
    if head == None:
        return None
    
    curr = head 
    while curr != None and curr.next != None:
        if  curr.key == curr.next.key :
            curr.next = curr.next.next
        else:
            curr = curr.next 
    
    return head
```

### reverse a linked list
*  below used the auxiliary od O(n)
```python
def reverse_linked_list(head):
    if head == None:
        return None
    
    stack = []
    curr = head
    while curr != None :
        stack.append(curr.key)
        curr = curr.next

    print(stack)

    curr = head
    while curr != None:
        item = stack.pop()
        curr.key = item
        curr = curr.next
    return head
```