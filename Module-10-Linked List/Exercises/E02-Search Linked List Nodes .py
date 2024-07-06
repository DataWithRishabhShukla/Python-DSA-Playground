class Node:
    def __init__(self,key) -> None:
        self.key = key
        self.next = None

def insert_at_start(head,key):
    if head == None:
        return Node(key)
    else :
        temp = Node(key)
        temp.next = head
        head = temp
        return temp

def print_list(head):
    while head != None:
        print(head.key, end=" ")
        head = head.next


head = None

head = insert_at_start(head, 20)
head = insert_at_start(head, 30)
head = insert_at_start(head, 40)

print_list(head)


def count_nodes(head):
    count =0 
    curr = head
    while curr != None:
        count += 1
        curr = curr.next
    print(f"\nNo of nodes: {count}")

count_nodes(head)
