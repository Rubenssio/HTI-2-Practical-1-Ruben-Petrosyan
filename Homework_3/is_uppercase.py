def is_uppercase(text):
    """Checks whether the every letter in the given text is uppercase
    and returns 'Yes' or 'No' accordingly:
        'Yes' - if every letter IS uppercase,
        'No'  - if every letter IS NOT uppercase"""

    if text.isupper():
        return 'Yes'
    return 'No'


print(is_uppercase(input("Enter the text: ")))
