# այս նույն խնդիրը փորձում եմ լուծել նաև ցանկացած range-ի համար
# կարող եք տեսնել number_guesser_for_any_number.py -ը

def guess_the_number(the_range, number_of_guesses):
    number_of_guesses += 1

    the_guess = (the_range[0] + the_range[1]) // 2

    print(f'My guess number {number_of_guesses} is: {the_guess}')
    print(f'(if correct input 0, if your number is higher than {the_guess} input 1, else -1)')
    missed = int(input())

    # checking if the number has been found
    if not missed:
        return {'number': the_guess, 'number_of_guesses': number_of_guesses}

    # checking if out of range
    if the_range[0] >= the_range[1]:
        return {'number': None, 'number_of_guesses': number_of_guesses}

    # checking if the guess was high or low
    if missed < 0:
        return guess_the_number((the_range[0], the_guess - 1), number_of_guesses)

    return guess_the_number((the_guess + 1, the_range[1]), number_of_guesses)


if __name__ == '__main__':

    result = None
    steps = 'steps'

    print(f'Think of a number between 1 and 999.\nInput 0 once you’re ready to play.')

    while result != 0:
        try:
            result = int(input())
        except ValueError:
            print("That's not even a number...")
    print("Ok, let's go!")

    result = guess_the_number((1, 999), 0)

    if result['number_of_guesses'] == 1:
        steps = 'step'

    if result['number'] is None:
        print(f"\nI couldn't guess in {result['number_of_guesses']} {steps}! This means you cheated!")
    else:
        print(f"\nI guessed in {result['number_of_guesses']} {steps}!")

# այս նույն խնդիրը փորձում եմ լուծել նաև ցանկացած range-ի համար
# կարող եք տեսնել number_guesser_for_any_number.py -ը
