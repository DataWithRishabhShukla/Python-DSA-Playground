
class Node:
    def __init__(self,data):
        self.key = data
        self.next = None

def print_circular(head):
    if head == None:
        return None 
    print(head.key, end=" ")
    curr = head.next
    while curr != head:
        print(curr.key ,end=" ")
        curr = curr.next

def insert_at_start(head,key):
    temp =  Node(key)

    if head == None:
        temp.next = temp
        return temp

    curr = head 
    while curr.next != head:
        curr = curr.next 

    curr.next = temp
    temp.next = head
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

def insert_at_end(head,key):
    node = Node(key)
    
    if head == None:
        node.next = node
        return node    

    curr = head 
    while curr.next != head:
        curr = curr.next 

    temp = curr.next
    curr.next = node
    node.next = temp

    return head 

def insert_at_end_tricky(head,key):
    temp =  Node(key)
    if head == None :
        temp.next = temp
        return temp
    
    temp.next = head.next 
    head.next = temp
    head.key, temp.key = temp.key , head.key
    return temp
    
head = Node(10)
head.next = Node(5)
head.next.next = Node(20)
head.next.next.next = Node(15)
head.next.next.next.next = head

print_circular(head)
print('\n')

head = insert_at_start(head,300)
print_circular(head)


print('\n')
head = insert_at_end(head,400)
print_circular(head)