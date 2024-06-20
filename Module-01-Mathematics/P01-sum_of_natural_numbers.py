def get_sum(n:int):
    sum = 0
    for i in range(1,n+1):
        sum+=i
    return sum

print(get_sum(5))

"""
Time Complexity:

Match Formula: (n*(n+1))/2
n = 10 -> (10 * 11)/2 -> 55

How did we arrive at formula:

Sn = 1  +   2   +   3   +   4           ....n
Sn = n  +   n-1 +   n-2 +   n-4         ....1
----------------------------------------------
2Sn = (n+1) + (n+1) + (n+1) + (n+1) + (n+1) ....(n+1)

2Sn = n*(n+1)

Sn = n*(n+1)/2

"""