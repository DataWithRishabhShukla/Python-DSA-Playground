class Node :
    def __init__(self,data):
        self.data = data
        self.next = None 
        self.prev = None

def print_dll(head):
    curr = head
    print("Printing the DLL: ")
    while curr != None:
        print(curr.data, end = " ")
        curr = curr.next
    print('\n')

def insert_at_begin(head,data):
    node = Node(data)
    if head is None:
        return node 
    
    node.next = head
    head.prev = node
    return node

def insert_at_end(head,data):
    node = Node(data)

    if head is None :
        return node
    
    curr = head 
    while curr.next != None:
        curr = curr.next 
    
    curr.next = node
    node.prev = curr
    return head


head = Node(10)

temp1 = Node(20)
temp2 = Node(30)

head.next = temp1
temp1.prev = head
temp1.next = temp2
temp2.prev = temp1

print_dll(head)

head = insert_at_begin(head,5)
print_dll(head)

head = insert_at_end(head,40)
print_dll(head)