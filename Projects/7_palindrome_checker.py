# **Palindrome Checker** → Check if a word/phrase is a palindrome.

def palindrome_checker(val):
    inp_val = str(val).lower().replace(" ", "")
    return inp_val == inp_val[::-1]

print(palindrome_checker(121))
print(palindrome_checker("race car"))
print(palindrome_checker("1213 121"))

print("hi hello".replace(" ", ""))