def check_anagram(s1,s2):
    if len(s1) != len(s2):
        return False 

    # for i in range(len(s1)):
    #     if s1[i] in s2 and (s1.count(s1[i]) == s2.count(s1[i])):
    #         flag = True
    #     else:
    #         flag = False

    # return flag 

    """
    The current implementation of your function has a logical flaw: it sets flag to True or False in each iteration of the loop, 
    which means the final result only reflects the outcome of the last character comparison. This can cause incorrect results
    """


    for char in s1:
        if s1.count(char) != s2.coount(char):
            return False
    return True