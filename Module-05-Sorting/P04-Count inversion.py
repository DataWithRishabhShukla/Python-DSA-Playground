"""
if i < j and arr[i] , arr[j]

ip : [2,4,1,3,5]
inversion : (2,1) , (4,1) , (4,3)
op : 3

If array is sorted in increasing order then 
ip : [1,2,3,4,5]
op : 0

If array is sorted in decreasing order then 
ip : [4,3,2,1]
op :  6
"""

def check_inversion(arr):
    num_inversion = 0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[j] < arr[i]:
                print(arr[i],arr[j])
                num_inversion += 1

    print(f"Num inversion : {num_inversion}")

arr = [2,4,1,3,5]
check_inversion(arr)

arr = [4,3,2,1]
check_inversion(arr)