
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



# Shorter form of the code 
head = None
head = insert_at_begin(head, 40)
head = insert_at_begin(head, 30)
head = insert_at_begin(head, 20)
head = insert_at_begin(head, 10)
head = insert_at_begin(head, 5)

print_list(head)
