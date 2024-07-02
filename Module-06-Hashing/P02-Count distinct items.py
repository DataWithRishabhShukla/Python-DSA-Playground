


def naive_count_distinct_item(arr):
    count = 0
    for i in range(len(arr)):
        flag = False
        for j in range(i):
            print(f"element in scope : {arr[i]} {arr[j]}")
            if arr[i] == arr[j]:
                flag = True
        if flag :
            continue

        count = count + 1
    print(f"No of elements : {count}")


ip = [10,20,10,30,30,20]
naive_count_distinct_item(ip)

print(len(set(ip)))