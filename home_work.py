def popular_words (text, *words):
    new_text = text.lower().split()
    result = {}

    for word in words:
        check = new_text.count(word.lower())
        result[word.lower()] = check

    return result