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

# required auxiliary space of O(n)
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

# without using the auxiliary space 
def remove_duplicates_from_sll_efficient(head):
    curr = head
    prev = None
    
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


head = None
head = insert_at_begin(head, 30)
head = insert_at_begin(head, 20)    
head = insert_at_begin(head, 10)
head = insert_at_begin(head, 5)
head = insert_at_begin(head, 2)

print_list(head)
print(f"\n Removing the duplicates from the list")
# head = remove_duplicates_from_sll(head)
# print_list(head)


head = remove_duplicates_from_sll_efficient(head)
print_list(head)