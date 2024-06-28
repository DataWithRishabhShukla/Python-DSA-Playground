
def display_one_to_n(n):
    if n == 0:
        return
    display_one_to_n(n-1)
    print(n)

display_one_to_n(4)
display_one_to_n(10)