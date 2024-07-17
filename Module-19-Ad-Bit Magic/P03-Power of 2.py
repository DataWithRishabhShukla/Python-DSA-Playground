def pow_of_two_naive(num):
    if num == 0:
        return False
    
    while num !=1:
        if num %2 != 0:
            return False
        
        num = num // 2
    return True

def power_of_two(num):
    if num == 0:
        return False
    
    return (num & (num-1)==0)

print(pow_of_two_naive(16))
print(pow_of_two_naive(17))
print(pow_of_two_naive(1))

print(f"Using the bitwise operator !!")
print(power_of_two(17))
print(power_of_two(1))