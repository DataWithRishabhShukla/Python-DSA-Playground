

def is_palindrome(str,start,end):
    if start >= end:
        return True
    return str[start] == str[end] and is_palindrome(str, start+1, end-1)

ip = 'abcba'
print(f"{ip} is palindrome: {is_palindrome(ip,0,len(ip)-1)}")

ip = 'aba'
print(f"{ip} is palindrome: {is_palindrome(ip,0,len(ip)-1)}")

ip = 'c'
print(f"{ip} is palindrome: {is_palindrome(ip,0,len(ip)-1)}")