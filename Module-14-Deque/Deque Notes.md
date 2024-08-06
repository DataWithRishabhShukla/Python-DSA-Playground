###                  Deque

#### Video 1 
- Deque - Doubly ended queue 
- Allows insertion and deletion from both the ends 
- Index based access is pallowed
- Slicing is not allowed 
- Internally uses advance version of DLL

```python
from collections import deque
```


#### Deque Operation 
- insertFront()
- insertRear()
- deleteFront()
- deleteRear()
- isFull()
- isEmpty()
- size()
- getFront()
- getRear()

#### Deque Application 
- A deque can be used used as both stack and queue - LIFO and FIFO both can be implemented 
- Maintianing history of action 
- Manintaining priority queue with two types of priority 
- Maximum . Minimum of size k in  subarray in 
 

####  Deque Python 
Deque can be implemented using below in python.
1. Using List 
2. Using collections.deque
3. Using Linked List - Dyanmic Sized array


```python
"""
Using List 
    - cache friendly 
    - insertion and deletion in O(1) but worst case it can be Linear


Using deque
    - Not cache friendly 
    - Insertion and deletion is alwyas in O(1)
    - based on the doulbly linked list implementation 
"""
```

#### Queue Implementation Using the DLL
- insertRear(x)
    - We will be modifying the front only when it's empty 
    - Otherwise always modifying the rear pointer  
    - Connect the link between existing deque and new node
    - connect prev of new node to existing deque
    - update the rear 
    - update the size

-   

```python 


```
