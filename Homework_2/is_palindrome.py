print('''
--- IS PALINDROME ---
This program checks whether the entered
text is a palindrome or not
''')

string = input('Enter text: \n')

is_palindrome = f'YES! "{string}" is a palindrome'

for i in range(int(len(string) / 2)):
    if string[i] != string[- (i + 1)]:
        is_palindrome = f'No, "{string}" is NOT a palindrome'
        break

print(f'\n-ANSWER-\n{is_palindrome}\n')
