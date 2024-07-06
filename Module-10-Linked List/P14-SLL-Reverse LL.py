
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

head = None
head = insert_at_begin(head, 30)
head = insert_at_begin(head, 20)    
head = insert_at_begin(head, 10)
head = insert_at_begin(head, 5)

import os 
os.system('clear')

print(f"\n Removing the duplicates from the list")
print_list(head)
head = reverse_linked_list(head)
print_list(head)
