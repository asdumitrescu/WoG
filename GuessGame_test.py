import random
from Score import add_score
from Utils import Screen_cleaner
def generate_number(lvl_sel):

    secret_number = random.randint(1, lvl_sel)
    return secret_number


def get_guess_from_user(lvl_sel):

    while True:
        number = input(f"Please choose number between 1 to {lvl_sel}: ")
        if number.isdigit() and int(number) >= 1 and int(number) <= lvl_sel:
            return int(number)
        else:
            print("Invalid input, please enter a number between 1 to", lvl_sel)


def compare_results(number, secret_number):

    if number == secret_number:
        return True
    else:
        return False


def play(lvl_sel):

    secret_number = generate_number(lvl_sel)

    number = int(get_guess_from_user(lvl_sel))

    result = compare_results(number, secret_number)

    if result:
        Screen_cleaner()
        print("CONGRATULATIONS !!!")
        return True
    else:
        Screen_cleaner()
        print("BETTER LUCK NEXT TIME !!!")
        print(f'The number was: {secret_number}')
        print('\n')
        return False
