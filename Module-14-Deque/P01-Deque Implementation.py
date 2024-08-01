from collections import deque
print("\nProgram 1!!!\n")
d = deque()
print(d)

d.append(10)
print(d)

d.append(20)
d.append(30)
print(d)

d.appendleft(40)
print(d)

print(d.pop())
print(d.popleft())
print(d)
print("\n!!!End of Program !!!\n")

from collections import deque
print("\n!!Start ofProgram 2!!!\n")
d = deque([10,20,30,40])
print(d)

d.insert(2,10)
print(d)
d.remove(10)
print(d)
d.extend([50,60])
print(d)
d.extendleft([10,15]) # deque([15, 10, 20, 10, 30, 40, 50, 60])
print(d)
print("\n!!!End of Program 2!!!\n")


print("\n!!Start ofProgram 3!!!\n")
from collections import deque
d = deque([10,20,30,40])
print(d)
d.rotate(2)
print(d)
d.rotate(-2)
print(d)
d.reverse()
print(d)

print("\n!!!End of Program 3!!!\n")


print("\n!!Start ofProgram 4!!!\n")
from collections import deque
d = deque([10,20,30,40])
print(d)
print(d[2])
d[2] = 100
print(d)
print(d[-1])
print(d[0])

print("\n!!!End of Program 4!!!\n")