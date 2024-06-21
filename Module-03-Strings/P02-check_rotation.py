
def check_rotation(ip1 , ip2):
    if len(ip1) != len(ip2):
        return False 
    
    for char in ip1:
        if ip1.count(char) != ip1.count(char):
            return False
    return True


print(check_rotation('ABCD','BCADD'))