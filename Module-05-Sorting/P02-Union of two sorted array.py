
def union_two_sorted_array(arr1,arr2):
    i,j,k =0,0,0
    res =[]

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            if arr1[i] not in res:
                res.append(arr1[i])
            i += 1
        else:
            if arr2[j] not in res:
                res.append(arr2[j])
            j += 1
    while i < len(arr1):
        if arr1[i] not in res:
            res.append(arr1[i])
        i += 1
    while j < len(arr2):
        if arr2[j] not in res:
            res.append(arr2[j])
        j += 1

    print(res)


arr1 = [3,3,5,8]
arr2 = [2,8,9,10,15]
union_two_sorted_array(arr1, arr2)

