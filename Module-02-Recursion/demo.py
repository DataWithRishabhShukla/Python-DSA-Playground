

def fun1(n):
    if n == 0:
        return
    print(f"{n} -> GFG")
    fun1(n-1)

fun1(3)

"""
Practice For Recursion (Part 1)
"""

def func(n):
    if n == 0:
        return 
    print(n)
    func(n-1)
    print(n)
    
func(3)

print(f"Using the func2")
def func2(n):
    if n == 0:
        return
    func2(n-1)
    print(n)
    func2(n-1)
func2(3)


"""
Practice For Recursion (Part 2)
"""

print(f"\nUsing the func3")
def fun3(n):
    if n <= 1:
        return 0
    else:
        return 1 + fun3(n//2)

print(fun3(16))


print(f"\nUsing the func4")
def fun4(n):
    if n == 0:
        return 
    fun4(n//2)
    print(f"{n} {n%2}")

fun4(13)
