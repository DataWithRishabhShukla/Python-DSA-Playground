
def get_largest_element(lst:list):
    if  not lst :
        return None 
    if len(lst) == 1:
        return lst[0]
    #return max(lst)

    # Using the sort 
    # lst.sort()
    # return lst[-1]

    # using the iteration 
    max = lst[0]
    for x in range(1,len(lst)):
        if lst[x] > max:
            max = lst[x]
    return max   

def get_max(ip):
    if not ip:
        return None
    else:
        res = ip[0]
        for i in range(1,len(ip)):
            if ip[i] > res:
                res = ip[i]
        return res



ip_lst = [3,23,8,97,134]
#ip_lst = [1]
print(bool(ip_lst))
print(f"Largest element list is: {get_largest_element(ip_lst)}")

print(f"Largest element list is: {get_max(ip_lst)}")