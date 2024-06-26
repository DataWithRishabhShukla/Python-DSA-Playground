" Find the left most character that repeats "

def check_left_most_repeat(s1):
    for char in s1:
        if s1.count(char) > 1:
            return char
    return -1 

def check_left_most_repeat_using_set(s1):
    seen = set()
    for char in s1:
        if char in seen:
            return char
        seen.add(char)
    return -1

print(check_left_most_repeat("geeksforgeeks"))
print(check_left_most_repeat("abbcc"))
print(check_left_most_repeat("abcd"))


print(check_left_most_repeat_using_set("geeksforgeeks"))
print(check_left_most_repeat_using_set("abbcc"))
print(check_left_most_repeat_using_set("abcd"))