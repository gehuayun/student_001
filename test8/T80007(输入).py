def reverse(text):
    """对调"""
    return text[::-1]


def is_palindrome(text):
    """判断对调后是否对称"""
    return text == reverse(text)


something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")
