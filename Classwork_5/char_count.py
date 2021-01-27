def char_count(txt):

    count = {}
    for char in txt:
        if char not in count:
            count[char] = txt.count(char)
    return count

print(char_count(input('Enter text: ')))
