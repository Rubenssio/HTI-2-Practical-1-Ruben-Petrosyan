# վերնագիր
print('''
--- IS PALINDROME ---
This program checks whether the entered
text is a palindrome or not
''')

# տվյալի մուտքագրում
string = input('Enter a text to check, or "-1" to exit the program: \n')

# որ տեսնենք քանի անգամ ենք կոդը աշխատացրել
answer_counter = 0

# ծրագիրը աշխատացնում ենք քանի դեռ «-1» չի մուտքագրվել
while string != "-1":

    # սկզբում ենթադրում ենք որ մուտքագրված տեքստը պալինդրոմ է
    is_palindrome = f'YES! "{string}" is a palindrome'

    # ստուգում ենք արդյոք մուտքագրված տեքստը իրականում պալինդրոմ է թե՝ ոչ
    for i in range(int(len(string) / 2)):
        if string[i] != string[- (i + 1)]:
            is_palindrome = f'No, "{string}" is NOT a palindrome'
            break

    # տպում ենք արդյունքը
    answer_counter += 1
    print(f'\n-ANSWER N{answer_counter}-\n{is_palindrome}\n')

    # օգտատերին հնարավորություն ենք տալիս նոր տեքստ մուտքագրել ստուգելու համար
    string = input('If you want to try again enter a new text, or "-1" to exit the program: \n')

# Goodbye note
print('Thanks for using our program!')