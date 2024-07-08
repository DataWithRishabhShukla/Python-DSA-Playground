
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
    


head = Node(10)
head.next = Node(5)
head.next.next = Node(20)
head.next.next.next = Node(15)
head.next.next.next.next = head

print_circular(head)

# corner cases 
# 1. List is empty
# 2. List has 1 element 