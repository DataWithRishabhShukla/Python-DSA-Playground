
import os
os.system('clear')


def list_reverse(ip):
    # Approach - 1
    return ip[::-1]

l  = [10,20,30,40]
print(list_reverse(l))

l = ['geeks', 'ide', 'courses']
print(list_reverse(l))

l  = [10,20,30,40]
l.reverse()
print(l)


l  = [10,20,30,40]
temp = list(reversed(l))
print(temp)


def custom_reverse_logic(ip):
    if len(ip) <2:
        return ip
    i = 0
    j = len(ip)-1
    print(f"Before reversal {ip}")
    while i < j:
        ip[i], ip[j] = ip[j],ip[i]
        i = i + 1
        j = j - 1
    print(f"After reversal {ip}")

l = [10,20,30,40]
custom_reverse_logic(l)