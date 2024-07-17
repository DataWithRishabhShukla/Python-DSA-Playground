

def find_odd(l):
    res = 0
    for num in l:
        res = res ^ num
    
    return res 

print(find_odd([10,10,10,20,20]))