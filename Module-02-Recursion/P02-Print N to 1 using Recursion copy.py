

def print_n_to_one(n):
    if n <= 0:
        return 
    print(n)
    print_n_to_one(n-1)

print_n_to_one(5)