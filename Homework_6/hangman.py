import random
import os


def get_a_random_line(file_path):
    with open(file_path) as f:
        items = [line for line in f.readlines()]
        return random.choice(items).strip()


def make_bigger(word):
    if len(word) <= 1:
        return word.upper()

    return word[0].upper() + '  ' + make_bigger(word[1:])


def update_word(the_letter, from_word, to_word):
    if the_letter not in from_word:
        return to_word

    update_index = from_word.index(the_letter)

    return (to_word[0:update_index] + the_letter +
            update_word(
                the_letter,
                from_word[update_index + 1:],
                to_word[update_index + 1:]
                )
            )


# def guessing(word, mistakes_left):
#
#     guessed = False
#     guessed_word = '_' * len(word)
#
#     while mistakes_left > 0 and not guessed:
#         print(f'Guess the word. {mistakes_left} mistakes left')
#         print(make_bigger(guessed_word))
#
#         letter = ''
#         while len(letter) != 1:
#             letter = input('Guess a letter: ').lower()
#
#         change = update_word(letter, word, guessed_word)
#
#         if guessed_word != change:
#             guessed_word = change
#         else:
#             mistakes_left -= 1
#
#         if guessed_word == word:
#             guessed = True
#
#     if guessed:
#         return make_bigger(word) + '\nYou won the game'
#     return 'You lost the game, the word was: ' + word.upper()


def guessing_recursive(word, mistakes_left, guess):
    if word == guess:
        return make_bigger(word) + '\nYou won the game'

    if mistakes_left < 1:
        return 'You lost the game, the word was: ' + word.upper()

    print(f'Guess the word. {mistakes_left} mistakes left')
    print(make_bigger(guess))

    letter = ''
    while len(letter) != 1:
        letter = input('Guess a letter: ').lower()

    # եթե ժամանակ լինի, մտածել հետևյալ 5 տողը ավելի սիրուն/օպտիմալ ինչպես կարելի է գրել
    change = update_word(letter, word, guess)
    if guess != change:
        guess = change
    else:
        mistakes_left -= 1

    return guessing_recursive(word, mistakes_left, guess)


if __name__ == '__main__':

    file = 'fruits.txt'
    dir_path = os.path.dirname(os.path.abspath(__file__))  # current directory
    file_path = os.path.join(dir_path, file)

    the_word = get_a_random_line(file_path)
    mistakes_allowed = 5

    # print(guessing(the_word, mistakes_allowed))  # not recursive version of the function
    print(guessing_recursive(the_word, mistakes_allowed, '_' * len(the_word)))
