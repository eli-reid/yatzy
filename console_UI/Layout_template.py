import os
import sys
def print_scorecard(player):
    clear_screen()
    prefix_space =int((61 - len(player.name))/2)
    suffix_space = prefix_space if (61 - len(player.name))%2 == 0 else prefix_space + 1
    name= f"{' ' * prefix_space}Player: {player.name}{' ' * suffix_space}"
    
    print( f"\r+---------------------------------------------------------------------+\n\
            \r|{name}|\n\
            \r+-------------------+-------------------------+-----------------------+\n\
            \r|  Upper Section    |      Lower Section      |         Totals        |\n\
            \r+------------+------+------------------+------+---------------+-------+\n\
            \r| [1] Ones   |  {player.scorecard.ones:2}  | [7] 3 of a Kind  |  {player.scorecard.three_of_kind :2}  |  Upper Score  |  {player.scorecard.upper_score :3}  |\n\
            \r+------------+------+------------------+------+---------------+-------+\n\
            \r| [2] Twos   |  {player.scorecard.twos:2}  | [8] 4 of a Kind  |  {player.scorecard.four_of_kind :2}  |  Upper Bonus  |  {player.scorecard.upper_bonus:3}  |\n\
            \r+------------+------+------------------+------+---------------+-------+\n\
            \r| [3] Threes |  {player.scorecard.threes:2}  | [9] Full House   |  {player.scorecard.fullhouse :2}  |  Upper Total  |  {player.scorecard.upper_total :3}  |\n\
            \r+------------+------+------------------+------+---------------+-------+\n\
            \r| [4] Fours  |  {player.scorecard.fours:2}  | [10] Sm Straight |  {player.scorecard.sm_straight :2}  |  Yatzy Bonus  |  {player.scorecard.yatzy_bonus :3}  |\n\
            \r+------------+------+------------------+------+---------------+-------+\n\
            \r| [5] Fives  |  {player.scorecard.fives:2}  | [11] Lg Straight |  {player.scorecard.lg_straight:2}  |  Lower Total  |  {player.scorecard.lower_total :3}  |\n\
            \r+------------+------+------------------+------+---------------+-------+\n\
            \r| [6] Sixes  |  {player.scorecard.sixes:2}  | [12] Yatzy       |  {player.scorecard.yatzy:2}  |  Grand Total  |  {player.scorecard.grand_total :3}  |\n\
            \r+------------+------+------------------+------+---------------+-------+\n\
            \r                    | [13] Chance      |  {player.scorecard.chance :2}  | \n\
            \r                    +------------------+------+\n"
            )

def print_hand(hand):
     print(f"\r+-----------+-----------+-----------+-----------+-----------+\n\
            \r|  Die # 1  |  Die # 2  |  Die # 3  |  Die # 4  |  Die # 5  |\n\
            \r+-----------+-----------+-----------+-----------+-----------+\n\
            \r|     {hand[0]}     |     {hand[1]}     |     {hand[2]}     |     {hand[3]}     |     {hand[4]}     |\n\
            \r+-----------+-----------+-----------+-----------+-----------+\n"
             )        
             
def print_current_player_hand(player, current_roll = 1, display_hand_header=False, err_msg=''):
    print_scorecard(player)
    hand_header = f"Current Roll #: {current_roll}{'':28} Plays Left: {player.plays_left}" 
    if display_hand_header:
        print(hand_header)
    print_hand(player.hand)
    print(err_msg)

def print_intro_screen():
    line1 = "At the start of each turn all the dice are auto rolled. You can either score the current roll, ".center(99,' ')
    line2 = "or re-roll any or all of the dice. IE: '145' will roll dice 1,4,5 ".center(99,' ')
    line3 = "You may only roll a total of 3 times. After rolling 3 times you must choose a category to score.".center(99,' ')
    line4 = "You may score the dice at any point in the round, i.e. it doesn't have to be after the 3rd roll.".center(99,' ')
    line5 = "Enter number of players".center(99,' ')
    print(f"\
            \r{'':10} .----------------.  .----------------.  .----------------.  .----------------.  .----------------. \n\
            \r{'':10}| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |\n\
            \r{'':10}| |  ____  ____  | || |      __      | || |  _________   | || |   ________   | || |  ____  ____  | |\n\
            \r{'':10}| | |_  _||_  _| | || |     /  \     | || | |  _   _  |  | || |  |  __   _|  | || | |_  _||_  _| | |\n\
            \r{'':10}| |   \ \  / /   | || |    / /\ \    | || | |_/ | | \_|  | || |  |_/  / /    | || |   \ \  / /   | |\n\
            \r{'':10}| |    \ \/ /    | || |   / ____ \   | || |     | |      | || |     .'.' _   | || |    \ \/ /    | |\n\
            \r{'':10}| |    _|  |_    | || | _/ /    \ \_ | || |    _| |_     | || |   _/ /__/ |  | || |    _|  |_    | |\n\
            \r{'':10}| |   |______|   | || ||____|  |____|| || |   |_____|    | || |  |________|  | || |   |______|   | |\n\
            \r{'':10}| |              | || |              | || |              | || |              | || |              | |\n\
            \r{'':10}| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |\n\
            \r{'':10} '----------------'  '----------------'  '----------------'  '----------------'  '----------------' \n\
            \r{'':51}Coded By Eli Reid \n\
            \r{'':10}+{'-' * 99}+\n\
            \r{'':10}|{'':99}|\n\
            \r{'':10}|{line1:99}|\n\
            \r{'':10}|{'':99}|\n\
            \r{'':10}|{line2:99}|\n\
            \r{'':10}|{'':99}|\n\
            \r{'':10}|{line3:99}|\n\
            \r{'':10}|{'':99}|\n\
            \r{'':10}|{line4:99}|\n\
            \r{'':10}|{'':99}|\n\
            \r{'':10}+{'-' * 99 }+\n")
  
def clear_screen():
        os.system('cls')
