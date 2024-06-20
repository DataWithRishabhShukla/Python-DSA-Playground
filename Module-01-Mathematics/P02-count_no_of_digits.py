number = int(input("Enter Number: "))
no_of_digit = 0
while number > 0:
    number = number //10
    no_of_digit += 1

print(f"No of digits: {no_of_digit}")

"""
Time Complexity:

"""

