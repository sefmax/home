import re


def is_palindrome(text):
    new_text = re.sub(r'[^a-zA-Z0-9]','',text).lower()
    return new_text == new_text[::-1]