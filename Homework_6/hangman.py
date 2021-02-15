def make_bigger(word):
    if len(word) <= 1:
        return word.upper()

    return word[0].upper() + '  ' + make_bigger(word[1:])


def update_word(the_letter, from_word, to_word):
    if the_letter not in from_word:
        return to_word

    update_index = from_word.index(the_letter)

    return (to_word[0:update_index] + the_letter +
            update_word(the_letter, from_word[update_index + 1:], to_word[update_index + 1:]))


def guessing(word, mistakes_left):

    guessed = False

    guessed_word = '_' * len(word)

    while mistakes_left > 0 and not guessed:
        print(f'Guess the word. {mistakes_left} mistakes left')
        print(make_bigger(guessed_word))

        letter = input('Guess a letter: ').lower()

        change = update_word(letter, word, guessed_word)

        if guessed_word != change:
            guessed_word = change
        else:
            mistakes_left -= 1

        if guessed_word == word:
            guessed = True

    if guessed:
        return make_bigger(word) + '\nYou won the game'
    return 'You lost the game'


if __name__ == '__main__':

    the_word = 'apple'

    mistakes_allowed = 5

    print(guessing(the_word, mistakes_allowed))
