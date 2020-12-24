string = input('Enter text: ')

is_palindrome = 'Yes'

for i in range(int(len(string) / 2)):
    if string[i] != string[- (i + 1)]:
        is_palindrome = 'No'
        break

print(is_palindrome)
