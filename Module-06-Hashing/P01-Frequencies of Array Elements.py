

def naive_count_frequency(arr):
    for i in range(len(arr)):
        flag = False
        for j in range(i):
            if arr[i] == arr[j]:
                flag = True
                break
    
        if flag == True:
            continue

        freq = 1
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                freq = freq + 1
        print(arr[i],freq)


def dict_count_frequency(arr):
    heap = {}
    for x in arr:
        if x in heap:
            heap[x] = heap[x] +1
        else:
            heap[x] = 1

    return heap
    
ip = [10,20,30,40,10]
naive_count_frequency(ip)
print(dict_count_frequency(ip))
