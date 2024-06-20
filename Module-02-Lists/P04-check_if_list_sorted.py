def check_if_list_sorted(ip):
    if not ip:
        return False

    prev_element = ip[0]
    for x in ip[1:]:
        if x > prev_element or x == prev_element:
            prev_element = x
            continue
        else:
            return False
    return True

ip_list = [2,30,35]
print(check_if_list_sorted(ip_list))

ip_list = [2,30,35,4]
print(check_if_list_sorted(ip_list))

ip_list = []
print(check_if_list_sorted(ip_list))

ip_list = [10,10,10]
print(check_if_list_sorted(ip_list))


def check_if_all_sorted_compre(ip):
    return all([ip[i] <= ip[i+1] for i in range(len(ip)-1)])

print("using check_if_all_sorted_compre")
ip_list = [2,30,35]
print(check_if_all_sorted_compre(ip_list))

ip_list = [2,30,35,4]
print(check_if_all_sorted_compre(ip_list))

ip_list = []
print(check_if_all_sorted_compre(ip_list))

ip_list = [10,10,10]
print(check_if_all_sorted_compre(ip_list))

ip_list = [30]
print(check_if_all_sorted_compre(ip_list))