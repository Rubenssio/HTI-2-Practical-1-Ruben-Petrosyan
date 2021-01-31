def is_palindrome_recursive(txt):
    if len(txt) <= 1:
        return True
    return txt[0] == txt[-1] and is_palindrome_recursive(txt[1:len(txt) - 1])


text = input('Enter the text: ')

if is_palindrome_recursive(text):
    print('Yes')
else:
    print('No')
