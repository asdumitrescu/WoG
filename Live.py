



def welcome():

    user_name = input("Please enter your name: ")
    print('\n')

    print('''Hello {} and welcome to the World of Games
           Here you can find many cool games to play.\n'''.format(user_name))
    return user_name

def load_game(user_name):
    while True:
        while True:  # Loop forever
            game_sel = input("""1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.
        2. Guess Game - guess a number and see if you chose like the computer. 
        3. Currency Roulette - try and guess the value of a random amount of USD in ILS.
            >>>:   """)  # Get the user input

            while game_sel < "1" or game_sel > "3":
                print('Oooops Wrong INPUT! Please try entering again numbers from 1 to 3')
                game_sel = input("""Please choose a game from the list:   
            1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
            2. Guess Game - guess a number and see if you chose like the computer 
            3. Currency Roulette - try and guess the value of a random amount of USD in ILS
                            >>>:   """)

            if game_sel == "1":
                print('You Chose 1. Memory Game\n')
            elif game_sel == "2":
                print('You Chose 2. Guess Game\n')
            elif game_sel == "3":
                print('You chose 3. Currency Roulette\n')
            else:
                print('\n')
            if game_sel.isdigit():  # They entered a number!
                break
        game_sel = int(game_sel)
        while True:  # Loop forever
            lvl_sel = input("""Please choose a game difficulty from 1 to 5:   
                   1 - VERY EASY
                   2 - EASY
                   3 - MEDIUM
                   4 - HARD
                   5 - VERY HARD
                   >>>:""") # Get the user input

            while lvl_sel < "1" or lvl_sel > "5":
                print('Oooops Wrong INPUT! Please try entering again numbers from 1 to 5')
                lvl_sel = input("""Please choose game difficulty from 1 to 5:   
                       1 - VERY EASY
                       2 - EASY
                       3 - MEDIUM
                       4 - HARD
                       5 - VERY HARD
                       >>>:  """)
            if lvl_sel == "1":
                print('Difficulty level', lvl_sel, 'selected! VERY EASY')
                break
            elif lvl_sel == "2":
                print('Difficulty level', lvl_sel, 'selected! EASY')
                break
            elif lvl_sel == "3":
                print('Difficulty level', lvl_sel, 'selected! MEDIUM')
                break
            elif lvl_sel == "4":
                print('Difficulty level', lvl_sel, 'selected! HARD')
                break
            elif lvl_sel == "5":
                print('Difficulty level', lvl_sel, 'selected! VERY HARD')

            if lvl_sel.isdigit():
                break
            else:
                print('\n')
        lvl_sel = int(lvl_sel)


        if game_sel == 1:
            from MemoryGame_test import play
            play(lvl_sel)
            while True:
                repeat = input("""Do you want to play again the same game with the same difficulty,
                                                or you want to play another game?
                                                To continue playing the same game with the same difficulty please type in Y or y:
                                                To Choose another game please type in N or n:  
                                                If you want to Exit please type in Q or q:  """)
                if repeat.startswith('Y') or repeat.startswith('y'):
                    play(lvl_sel)
                elif repeat.startswith('N') or repeat.startswith('n'):
                    break
                elif repeat.startswith('Q') or repeat.startswith('q'):
                    print(f"Was nice to see you {user_name}!!! Thanks for playing my game, see you next time !")
                    exit()
                else:
                    print("Invalid input, try again!")
        elif game_sel == 2:
            from GuessGame_test import play
            play(lvl_sel)
            while True:
                repeat = input("""Do you want to play again the same game with the same difficulty,
                                                or you want to play another game?
                                                To continue playing the same game with the same difficulty please type in Y or y:
                                                To Choose another game please type in N or n:  
                                                If you want to Exit please type in Q or q:  """)
                if repeat.startswith('Y') or repeat.startswith('y'):
                    play(lvl_sel)
                elif repeat.startswith('N') or repeat.startswith('n'):
                    break
                elif repeat.startswith('Q') or repeat.startswith('q'):
                    print(f"Was nice to see you {user_name}!!! Thanks for playing my game, see you next time !")
                    exit()
                else:
                    print("Invalid input, try again!")
        elif game_sel == 3:
            from CurrencyRoulette_test import play
            play(lvl_sel)
            while True:
                repeat = input("""Do you want to play again the same game with the same difficulty,
                                                or you want to play another game?
                                                To continue playing the same game with the same difficulty please type in Y or y:
                                                To Choose another game please type in N or n:  
                                                If you want to Exit please type in Q or q:  """)
                if repeat.startswith('Y') or repeat.startswith('y'):
                    play(lvl_sel)
                elif repeat.startswith('N') or repeat.startswith('n'):
                    break
                elif repeat.startswith('Q') or repeat.startswith('q'):
                    print(f"Was nice to see you {user_name}!!! Thanks for playing my game, see you next time !")
                    exit()
                else:
                    print("Invalid input, try again!")
        else:
            print("Wrong choice, Try again!")
            load_game(user_name)

