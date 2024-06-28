

def merge_sort_array(arr1,arr2):
    i,j ,k = 0, 0, 0
    temp = []
    while i < len(arr1) or j <len(arr2):
        print(f"i : {i} \nj : {j}")
        print(f"arr1 : {arr1[i:]}")
        print(f"arr2 : {arr2[j:]}")
        print(f"temp : {temp}")
        print('\n')
        if i == len(arr1):
            temp.extend(arr2[j:])
            break
        elif j == len(arr2):
            temp.extend(arr1[i:])
            break
        elif arr1[i] < arr2[j]:
            temp.append(arr1[i])
            i += 1
            #print(temp)
        else:
            temp.append(arr2[j])
            j += 1
            #print(temp)
    
    print(temp)
   
merge_sort_array([5,6,7,19],[3,8,9])