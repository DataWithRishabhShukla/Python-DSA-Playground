print("\n!!Start ofProgram 1 - Queue Using the List!!!\n")

q = []
q.append(10) #enque
q.append(20)
q.append(30)
print(q)
print(q.pop(0)) #deque
print(q.pop(0)) #deque
print(len(q)) #size
print(q[0]) #getFront
print(q[-1]) #getRear
print("\n!!!End of Program 1!!!\n")


print("\n!!Start ofProgram 2 - Queue Using the List!!!\n")
from collections import deque
q = deque()
q.append(10) #enque
q.append(20)
q.append(30)
print(q)
print(q.popleft()) #deque
print(q.popleft()) #deque
print(len(q)) #size
print(q[0]) #getFront
print(q[-1]) #getRear
print("\n!!!End of Program 2!!!\n")