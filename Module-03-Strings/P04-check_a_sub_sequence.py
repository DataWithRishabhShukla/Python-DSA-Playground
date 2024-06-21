def check_sub_sequence(s1, s2):
    if len(s2) > len(s1):
        return False
    
    max_count = 0
    for c in s2:
        if c not in s1 :
            return False
        char_index = s1.index(c) 
        if max_count == 0 :
            max_count = char_index
        elif char_index < max_count:
            return False
    return True 

def check_sub_sequence_2(s1, s2):
    i , j = 0 , 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[i]:
            j += 1
        i += 1

    return j == len(s2)
    
print(check_sub_sequence('ABCD','AD'))
print(check_sub_sequence('ABCDE','AED'))