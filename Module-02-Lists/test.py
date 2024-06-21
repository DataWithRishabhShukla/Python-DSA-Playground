ip = [12, 35, 1, 10, 34, 1]


def get_second_largest(ip):
    if not ip or len(ip) < 2:
        return -1
    
    max = ip[0]
    sc_mx = None

    for x in ip[1:]:
        if x > max :
            sc_mx = max
            max = x
        elif x != max :
            if x >  sc_mx or sc_mx == None :
                sc_mx = x 
    return sc_mx

print(get_second_largest(ip))