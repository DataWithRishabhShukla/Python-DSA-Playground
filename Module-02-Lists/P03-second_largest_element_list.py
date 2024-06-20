def get_second_max(lst:list):
    if not lst:
        return None

    lst.sort()
    lst.remove(lst[-1])
    return lst[-1]

def get_sec_max(ip):
    if len(ip) <1:
        return None
    else:
        lar = get_max(ip)
        sec_max = None
        for x in ip:
            if x != lar:
                if sec_max == None:
                    sec_max = x
                else: 
                    sec_max = max(x,sec_max)
        return sec_max



def get_max(ip):
    if not ip:
        return None
    else:
        res = ip[0]
        for i in range(1,len(ip)):
            if ip[i] > res:
                res = ip[i]
        return res

ip_list = [10,5,8,20]
print(get_second_max(ip_list))
ip_list = [10,10,10]
print(get_sec_max(ip_list))
ip_list = [20,10,20,8,12]
print(get_sec_max(ip_list))


def get_max_one_traversal(ip):
    first_max = float('-inf')
    second_max = float('-inf') 

    for x in ip:
        if x > first_max :
            second_max = first_max
            first_max = x
        elif x > second_max  and x != first_max:
            second_max = x
    return second_max

ip_list = [20,10,20,8,12]
ip_list = [20, 20, 20,88]
print(get_max_one_traversal(ip_list))


def get_max_one_traversal_gfg(ip):
    first_max = ip[0]
    second_max = None 

    for x in ip[1:]:
        if x > first_max:
            second_max = first_max
            first_max = x
        elif x != first_max:
            if x > second_max  or  second_max == None:
                second_max = x
    return second_max

ip_list = [20, 20, 20]
print(get_max_one_traversal_gfg(ip_list))



