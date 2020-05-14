import os
from Game import Game 
from console_UI.Layout_template import *
roll = 0;

def score_current_hand(game):
    score_input=''
    info_msg= ''
    if game.is_yatzy_bonus:
        info_msg = "YATZY Bonus must be played in upper section if unless that number is filled in alread then it can be played in lower sevtion!"
    while (score_input == ''):
        try:
            roll = 1 
            print_current_player_hand(game.current_player, roll, True, info_msg)
            score_input = input("Score Hand Option[1-13]: ")
            game.score_hand(score_input)
            
        except ValueError as error:
            info_msg = f"{error} Please try agian!"
            score_input = ''

        except KeyError:
            info_msg = f"'{score_input}' is an invlid selection, Please choose a number 1-13'"
            score_input = ''

def title_screen():
    print_intro_screen();
    players = input("Please enter player's names seperated by comma: ")
    game = Game(players.split(','))
    play_game(game)

def play_game(game):   
    while not game.game_over:
        user_input = ''
        err_msg = ''
        #update_screen('')
        for roll in range(1,4):
            if  roll == 1:
                game.current_player.hand.roll()
                print_current_player_hand(game.current_player, roll, True)
            
            while user_input != 's' and roll != 3:
                print_current_player_hand(game.current_player, roll, True, err_msg)
                user_input = input("[Roll All] Press enter, [Roll Selected 1 - 5] Enter the numbers press enter, [Score Hand] 's' :") 
                if user_input == 's':
                    break
                try:
                    game.current_player.hand.roll(user_input)
                    break
                except ValueError as error:
                    err_msg = f"{error}"
                    user_input = ''
                
            if roll == 3 or user_input == 's':
                break
            print_current_player_hand(game.current_player, roll, True)

        score_current_hand(game)
        print_current_player_hand(game.current_player)
        if input("Press Enter [Next Player] or q [Quit]") == 'q':
            break
        game.get_next_player()

    winner = game.get_winner()

    print_scorecard(winner)
    print(f"{winner.name} is the winner!")

title_screen()