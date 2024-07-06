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

def nth_element_from_end(head,e):
    if head == None :
        return None
    
    curr = head
    count = 0

    while curr != None :
        count = count + 1 
        curr = curr.next 

    if e > count :
        return None


    # print(f"\n\nLegth of list is  : {count}")
    # print(f"Legth - index {e}  : {count-e}")
    curr = head 
    for i in range(count-e):
        curr = curr.next

    print(f"\n{e}th element from end is : {curr.key}")

# using the two pointer approach

def nth_element_from_end_two_pntr(head,n):
    if head == None:
        return None
    
    first = head 
    for i in range(n):
        if first == None:
            return
        first = first.next

    second = head
    while first != None:
        first = first.next
        second = second.next 
    print(f"\n{n}th element in the SLL is :{second.key}")



head = None
head = insert_at_begin(head, 60)
head = insert_at_begin(head, 50)
head = insert_at_begin(head, 40)
head = insert_at_begin(head, 30)    
head = insert_at_begin(head, 20)
head = insert_at_begin(head, 10)

print_list(head)

nth_element_from_end(head,4)
nth_element_from_end(head,1)
nth_element_from_end(head,10)

nth_element_from_end_two_pntr(head,4)
nth_element_from_end_two_pntr(head,1)
nth_element_from_end_two_pntr(head,10)