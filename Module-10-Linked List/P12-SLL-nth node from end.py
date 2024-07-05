class Node:
    def __init__(self,k):
        self.key = k
        self.next = None

def print_list(head):
    curr = head
    while curr != None:
        print(curr.key, end = " ")
        curr = curr.next

def insert_at_begin(head,key):
    node = Node(key)
    node.next = head
    return node 


head = None
head = insert_at_begin(head, 60)
head = insert_at_begin(head, 50)
head = insert_at_begin(head, 40)
head = insert_at_begin(head, 30)    
head = insert_at_begin(head, 20)
head = insert_at_begin(head, 10)

print_list(head)

