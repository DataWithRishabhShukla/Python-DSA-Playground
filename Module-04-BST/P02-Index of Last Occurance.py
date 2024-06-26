"""
ar = [1,10,10,10,20,30] 
    x = 10
    op = 3

    x = 45
    op = -1
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
ar = [1,10,10,10,20,30] 

print(find_last_occurance(ar, 10))
print(find_last_occurance(ar, 70))