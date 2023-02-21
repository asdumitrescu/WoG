import os
import time

SCORES_FILE_NAME = 'Scores.txt'
BAD_RETURN_CODE = "ERROR CODE 214"
LAST_SCORES = 'last_scores.txt'


def Screen_cleaner():

     time.sleep(0.7)
     if (os.name == 'posix'):
        os.system('clear')
     else:
        os.system('cls')


def transfer_and_clear_file(src_file, cp_file):
    
    with open(src_file, 'r') as scores:
        current_score = scores.read().strip()

    with open(cp_file, 'w') as scores:
        scores.write(current_score)

    with open(src_file, 'w') as scores:
        scores.write('')



