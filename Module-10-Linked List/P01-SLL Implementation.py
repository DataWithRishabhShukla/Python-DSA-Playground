
class Node:
    def __init__(self,k):
        self.key = k
        self.next = None

def print_list(head):
    curr = head
    while curr != None:
        print(curr.key, end = " ")
        curr = curr.next



# Shorter form of the code 
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print_list(head)