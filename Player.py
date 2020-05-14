from Scorecard import Scorecard
from Hand import yatzy_hand
import datetime
class Player:

    def __init__(self, name):
        self.name = name
        self.scorecard = Scorecard()
        self.hand: Hand_of_dice = yatzy_hand()
    
    @property
    def plays_left(self):
        return self.scorecard.plays_left
    
    
class Computer_player(Player): # pragma: no cover
    def __init__(self):
        super().__init__(name = "Computer")
    
    def play_turn(self):
        pass
        
    def should_roll(self)->str:
        pass
    
    def is_hand_scorable(self)->bool:
        pass

    


    
date =datetime.datetime.day
        