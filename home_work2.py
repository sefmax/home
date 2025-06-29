import re

def first_word(text):
    words = re.findall(r"[a-zA-Zа-яА']+", text)
    return words[0] if words else ""

