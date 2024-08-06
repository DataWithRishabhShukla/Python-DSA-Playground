
class Node:
    def __init__(self,k):
        self.key = k
        self.next = None 


class MyQueue:
    def __init__(self):
        self.rear = None
        self.front = None
        self.sz = 0


    def is_empty(self):
        return self.sz == 0

    def size(self):
        return self.sz
    
    def get_front(self):
        return self.front.key
    
    def get_rear(self):
        return self.rear.key

    def enque(self,x):
        temp = Node(x)

        if self.rear is None:
            self.front = temp
        else:
            self.rear.next = temp
        self.rear = temp
        self.sz +=1
    
    def deque(self):
        if self.front is None:
            return None 
        else:
            res = self.front.key
            self.front = self.front.next
            if self.front is None :
                self.rear = None
            self.sz -=1
            return res
            