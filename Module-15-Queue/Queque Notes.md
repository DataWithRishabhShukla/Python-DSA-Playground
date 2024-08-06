###                  Queue Data Structure

#### Video 1 - Queue Data Structure
- FIFO 
- **Queue Operations**
    - enque() -> Insertion at the end
    - deque() -> Deletion at the start
    - getFront()
    - getRear()
    - size()
    - isEmpty()


#### Video 2 - Applications of Queue Data Structure
- Single resource and Multiple Consumers 
- Synchornization between slow and fast devices 
- In operating system - 
- In computer networks
- Variations - Deque , Priority Queue , Doubly Ended Queue 


#### Video 2 - Queue in Python 
- Using List 
- Using Collections.deque
- Using queue.Queue 
    - Only used in multithreded environmenets 
    - Uses Collections.deque internally 
- Our own Implementation 

- **Using List**
    - Only disadvantage in pop uses O(n) time as it removes and shift all elements.
    - enque -> O(1)
    - deque -> O(n)
```python
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
```

- **Using collection deque**
    - Recomended way to implement queue in python
    - Internally uses python 
```python
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
```