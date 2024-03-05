# To reverse the string
def rev(str):
    return str[::-1]

# To compare the string and compare whether palindrome
def is_palindrome(str):
    reversed_str = rev(str)
    return str == reversed_str

string = "radar"
if is_palindrome(string):
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")
