
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
    if pos == 1:
        node.next = head
        return node
        
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

def delete_first_node(head):
    if head == None:
        return None
    else :
        return head.next 

def delete_last_node(head):
    if head == None:
        return None
    
    if head.next == None:
        return None

    curr = head 
    # pos = 1
    while curr.next.next != None:
        curr = curr.next
        # pos = pos + 1
    # print(pos)
    # print(curr.key)
    print(f"deleting the node {curr.next.key}...")
    curr.next = None
    return head
    # print(curr.next.key)
    
def delete_nth_node(ptr):
    temp = ptr.next
    ptr.key = ptr.next.key
    ptr.next = temp.next


def insert_in_sorted_sll(head,element):
    temp = Node(element)
    
    if head == None:
        return temp
    elif element < head.key:
        temp.next = head
        return temp
    else: 
        curr = head
        while curr.next != None:
            if element > curr.key and element  < curr.next.key :
                break
            curr = curr.next
        
        temp.next = curr.next
        curr.next = temp
        return head

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

def print_middle_efficient(head):
    if head == None:
        return None 
    
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next 
    print(slow.key)


head = None
head = insert_at_begin(head, 60)
head = insert_at_begin(head, 50)
head = insert_at_begin(head, 40)
head = insert_at_begin(head, 30)    
head = insert_at_begin(head, 20)
head = insert_at_begin(head, 10)

print("\n")
print_list(head)
print("\n")

print_middle(head)
print_middle_efficient(head)
