
arr = [1,2,3,4,5]

def prints_array(arr , n):
    if n == 0:
        return
    
    
    prints_array(arr, n = n-1)
    print(arr[n-1])

prints_array(arr,5)