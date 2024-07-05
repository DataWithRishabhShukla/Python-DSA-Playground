
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
        curr = curr.next

    curr.next = node
    return head

def insert_at_pos(head, pos, key):
    node = Node(key)
    if head == None:
        return Node(key)
    
    curr = head
    pointer = 1
    while curr.next != None:
        if pos == pointer:
            break 
        pointer = pointer +1
        curr = curr.next
    
    # print(f"Current pointer value {pointer}")

    if curr.next == None:
        print(f"\nWARN : POS: {pos} is greater than length of LL: {pointer}. Ignoring the insert...\n")
        return head

    temp = curr.next 
    curr.next = node
    node.next = temp

    return head



# Shorter form of the code 
head = None
head = insert_at_begin(head, 40)
head = insert_at_begin(head, 30)
head = insert_at_begin(head, 20)
head = insert_at_begin(head, 10)
head = insert_at_begin(head, 5)


print_list(head)
print("\nInserting 66 at pos 2 ...")
head = insert_at_pos(head, 2 , 66)
print_list(head)
print("\n\n")

print_list(head)
print("\nInserting 99 at pos 5 ...")
head = insert_at_pos(head, 5 , 99)
print_list(head)
print("\n\n")


print_list(head)
print("\nInserting 111 at pos 9 ...")
head = insert_at_pos(head, 9 , 111)
print_list(head)
print("\n\n")
