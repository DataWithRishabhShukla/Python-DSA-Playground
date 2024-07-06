class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

def insert_at_start(head,data):
    if head == None:
        return Node(data)
    else :
        temp = Node(data)
        temp.next = head
        head = temp
        return temp

def print_list(head):
    while head != None:
        print(head.data, end=" ")
        head = head.next


head = None

head = insert_at_start(head, 20)
head = insert_at_start(head, 30)
head = insert_at_start(head, 40)

print_list(head)

# count Nodes
def count_nodes(head):
    count =0 
    curr = head
    while curr != None:
        count += 1
        curr = curr.next
    print(f"\nNo of nodes: {count}")

count_nodes(head)

# Search in node
print("\n\nSearch in node")
head = None
values = [5,4,3,2,1]
for x in values:
    head = insert_at_start(head, x)
print_list(head)

def serach_node(head,data):
    if head == None:
        return False
    
    curr = head 
    while curr != None:
        if curr.data == data :
            return True
        curr = curr.next
    return False

print(serach_node(head,400))

print(serach_node(head,5))


# delete at pos
# Search in node
print("\n\nSearch in node")
head = None
values = [5,4,3,2,1]
for x in values:
    head = insert_at_start(head, x)
print_list(head)

def deleteAtPosition(head, pos):
    #code here
    if head == None:
        return None
    
    curr = head 
    count = 1
    
    while curr != None :
        if count == pos:
            break
        curr = curr.next
        count = count + 1 
    
    print(curr.data)
    curr = head
    for i in range(1,count-1):
        curr = curr.next
    curr.next = curr.next.next
    return head

    

head = deleteAtPosition(head,4)
print_list(head)