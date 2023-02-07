import random
import time
import os


def generate_sequence(lvl_sel):
    secret_sequence = [random.randint(1, 101) for _ in range(int(lvl_sel))]
    return secret_sequence

def get_list_from_user(lvl_sel):
    user_input = input("Enter numbers separated by spaces: ")
    user_list = [int(num) for num in user_input.split() if num.isdigit()]
    while len(user_list) != lvl_sel:
        print("Invalid input. Please enter {} numbers separated by spaces.".format(lvl_sel))
        user_input = input("Enter numbers separated by spaces: ")
        user_list = [int(num) for num in user_input.split() if num.isdigit()]
    return user_list


def is_list_equal(secret_sequence, user_list):
    if secret_sequence == user_list:
        return True
    else:
        return False


def play(lvl_sel):
    secret_sequence = generate_sequence(lvl_sel)
    print(secret_sequence)
    time.sleep(0.7)
    os.system('cls')
    result = is_list_equal(secret_sequence, get_list_from_user(lvl_sel))
    if result:
        print("You won!")
        return True
    else:
        print("You lost. The numbers were {}".format(secret_sequence))
        return False
