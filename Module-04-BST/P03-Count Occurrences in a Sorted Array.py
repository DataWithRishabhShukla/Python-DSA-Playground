"""
ip: l = [10, 20, 20 , 20 , 30]
    x = 20 
op: 3

ip: l = [20, 20 , 20 , 20]
    x = 20 
op: 4

ip: l = [5, 6, 7,8]
    x = 10 
op: 0

"""

def find_last_occurance(arr,x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if x > arr[mid]:
            low = mid + 1
        elif x < arr[mid]:
            high = mid - 1
        else :
            if mid == len(arr)-1 or arr[mid] != arr[mid+1] :
                return mid
            else :
                low = mid +1 
    return -1

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

def count_occurance(l, x):
    first = find_x_using_bst(l,x)
    if first == -1:
        return 0
    return find_last_occurance(l,x) - first +1

arr = [5,10,10,10,10,10,40]
print(count_occurance(arr,10)) 