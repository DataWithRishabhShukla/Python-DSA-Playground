""" Reverse the order of words in string """

def reverse_words_order(s1):
    return " ".join(s1.split()[::-1])

print(reverse_words_order("welcome to gfg"))
print(reverse_words_order("I Love coding"))


def reverse_words_in_place(s1):
    rev = ''
    for words in s1.split():
        rev = words + rev
    return rev

print(reverse_words_in_place("welcome to gfg"))
print(reverse_words_in_place("I Love coding"))