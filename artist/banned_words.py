from json import load

def banned_words(title):
    title = title.lower()
    data = load(open('./banned_words.json'))
    words = data['words']
    for i in words:
        if i in title:
            return False
    return True
