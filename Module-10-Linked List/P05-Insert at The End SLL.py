
class Node:
    def __init__(self,k):
        self.key = k
        self.next = None

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

def insert_at_begin(head,key):
    node = Node(key)
    node.next = head
    return node 

def insert_at_end(head,key):
    node = Node(key)

    if  head == None:
        return node
    curr = head
    while curr.next != None:
        #print(f"inside while {curr.key} {curr.next}")
        curr = curr.next
    
    curr.next = node

    return head



# Shorter form of the code 
head = None
head = insert_at_begin(head, 40)
head = insert_at_begin(head, 30)
head = insert_at_begin(head, 20)
head = insert_at_begin(head, 10)
head = insert_at_begin(head, 5)

print_list(head)
print(f"\n Inserting at the end node 100..")
head = insert_at_end(head, 100)
print_list(head)