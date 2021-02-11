def guess_the_number(the_range, number_of_guesses):
    number_of_guesses += 1
    the_guess = round((the_range[0] + the_range[1]) / 2)

    print(f'My guess number {number_of_guesses} is: {the_guess}')
    print(f'(if correct input 0, if your number is higher than {the_guess} input 1, else -1)')
    missed = int(input())

    if not missed:
        return {'number': the_guess, 'number_of_guesses': number_of_guesses}

    if the_range[0] - the_range[1] == 0:
        return {'number': None, 'number_of_guesses': number_of_guesses}

    if missed < 0:
        return guess_the_number((the_range[0], the_guess - 1), number_of_guesses)
    else:
        return guess_the_number((the_guess + 1, the_range[1]), number_of_guesses)


min_max = 1, 999  # ստուգել արդյոք կոդը ճիշտ կաշխատի եթե min_max = 999, 1
result = None
steps = 'steps'

print(f'Think of a number between {min_max[0]} and {min_max[1]}.\nInput 0 once you’re ready to play.')

while result != 0:
    result = int(input())
print("Let's go!")

result = guess_the_number(min_max, 0)

if result['number_of_guesses'] == 1:
    steps = 'step'

if result['number'] is None:
    print(f"\nI couldn't guess in {result['number_of_guesses']} {steps}! This means you cheated!")
else:
    print(f"\nI guessed in {result['number_of_guesses']} {steps}!")
