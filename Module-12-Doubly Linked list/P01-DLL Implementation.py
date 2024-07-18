class Node :
    def __init__(self,data):
        self.data = data
        self.next = None 
        self.prev = None

def print_dll(head):
    if head is None:
        print("!! DLL is empty !!\n")
        return

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


def delete_head_node(head):
    if head is None or head.next is None:
        return None
    
    temp = head.next 
    temp .prev = None
    return temp

def delete_last_node(head):
    if head is None or head.next is None:
        return None

    curr = head
    while curr.next.next != None:
        curr = curr.next
    
    curr.next = None
    return head

def reverse_dll(head):
    if head is None or head.next is None :
        return head
    
    curr = head
    prev = None 

    while curr != None:
        prev = curr
        curr.next , curr.prev = curr.prev , curr.next
        curr = curr.prev
    
    return prev



head = Node(10)

temp1 = Node(20)
temp2 = Node(30)

head.next = temp1
temp1.prev = head
temp1.next = temp2
temp2.prev = temp1

print_dll(head)

head = insert_at_begin(head,5)
print("Inserting at the begin !!")
print_dll(head)

head = insert_at_end(head,40) #inserting at the end of DLL
print("Inserting at the end !!")
print_dll(head)

head_sinle_node = Node(10) #creating the single node DLL 
head_sinle_node = delete_head_node(head_sinle_node)
print("Deleted the head in a single node DLL !!")
print_dll(head_sinle_node)

head = delete_head_node(head) #deleting the head node 
print("Deleted the head !!")
print_dll(head)


head = delete_last_node(head) #delete the last node from the DLL
print("Deleted the last node !!")
print_dll(head)

head_sinle_node = Node(10) #creating the single node DLL 
head_sinle_node = delete_last_node(head_sinle_node)
print("Deleted the last in a single node DLL !!")
print_dll(head_sinle_node)

head = reverse_dll(head) #reversing the dll
print("Reversing the DLL ")
print_dll(head)