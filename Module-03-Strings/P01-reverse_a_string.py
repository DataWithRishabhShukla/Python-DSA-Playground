


def reverse_String(ip):
    rev = ""
    for i in ip:
        rev = i + rev
    
    return rev

    #return ip[::-1]

    # Without slicing  -> throws error 
    # n = len(ip)
    # start = 0
    # end = n - 1
    # while start < end:
    #     ip[start], ip[end] = ip[end], ip[start]
    #     start += 1
    #     end -= 1
    # return ip

    # Error : ip[start], ip[end] = ip[end], ip[start] TypeError: 'str' object does not support item assignment


print(reverse_String("hello"))