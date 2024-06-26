"""
ar = [1,10,10,10,20,30] 
    x = 10
    op = 1

    x = 45
    op = -1
"""
def find_x_using_bst(l,x):
    low  = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high)//2
        if x < l[mid]:
            high = mid -1
        elif x > l[mid] :
            low = mid + 1
        else:
            if mid == 0 or l[mid] != l[mid-1]:
                return mid
                
            else:
                high = mid - 1
    return -1




def find_x_naive_approach(l,x):
    for i in range(0,len(l)):
        if l[i] == x :
            return i
    return -1

ar = [1,10,10,10,20,30]
print(find_x_naive_approach(ar, 10))
print(find_x_naive_approach(ar, 45))

print("***** using the bst approach ..\n")
print(find_x_using_bst(ar, 10))
print(find_x_using_bst(ar, 45))
