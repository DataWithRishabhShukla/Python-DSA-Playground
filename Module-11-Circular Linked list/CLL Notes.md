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


#### Inserting in the circular list 
- using naive approach requires O(n)
##### Tricky approach O(1) 

- Point node.next = head.next 
- We insert the values after the head -> head.next = node
- Swap the values between head and temp
- Just return head in case of insert at start
- Just return temp in case of insert at end


```python 
def insert_at_end_tricky(head,key):
    temp =  Node(key)
    if head == None :
        temp.next = temp
        return temp
    
    temp.next = head.next 
    head.next = temp
    head.key, temp.key = temp.key , head.key
    return temp

def insert_at_start_tricky(head,key):
    temp =  Node(key)
    if head == None :
        temp.next = temp
        return temp
    
    temp.next = head.next 
    head.next = temp
    head.key, temp.key = temp.key , head.key
    return head 
```


#### Edge Cases 
1. List is empty
2. List has one element 
3. List has more than one element 