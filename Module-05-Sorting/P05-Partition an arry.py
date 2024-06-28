"""
ip : = [3,8,6,12,10,7]
index = 5

re-arrange arrayin such a way 
    - all element in the left are lesser than indexed element
    - all element in the right are greater than indexed element
    - order of element does not matter

    [3,6,7,8,12,10,7]
            or
    [6,3,7,8,10,12,7]   
"""

"""
Steps:
    1. create a temp array
    2. swap the indexed elemen to the last
    3. traverse the ip array and append all the element that are less than equal to (<=) indexed array to temp
    4. traverse the ip array and append all the element that are greater than to (>) indexed array to temp
    5. assign all the elements from the 

Time and space complexity:
    Theta(n)
    Theta(n)
"""

def parition_arry(arr,p):
    temp = []
    n = len(arr)
    arr[p], arr[n-1] = arr[n-1], arr[p]
    print(f"after swap : {arr}")

    for x in arr:
        if x <= arr[n-1]:
            temp.append(x)
    
    print(f"temp after the loading all the <= element: {temp}")

    for x in arr:
        if x > arr[n-1]:
            temp.append(x)
    
    print(f"temp after the loading all the > element: {temp}")
    arr = temp

arr1 = [5,13,6,9,12,8,11]
parition_arry(arr1,5)
