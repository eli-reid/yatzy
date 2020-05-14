from Player import Player 
from functools import wraps

def yatzy_Bonus(func): 
    @wraps(func)
    def inner(self):
        if self.is_yatzy_bonus:
            self.add_yatzy_bonus()
        func(self)  
    return inner

class Game:

    def __init__(self, player_names: list, *args, **kwargs):
        self.player_list: list = [Player(name) for name in player_names]
        self.current_player: Player = None
        self._next_player = self._next_player_gen()
        self.get_next_player()
        self._options: dict = self._scoring_options()
        self.fullhouse_value: int = 25
        self.sm_straight_value: int = 30
        self.lg_straight_value: int = 40
        self.yatzy_value: int = 50
        self.yatzy_bonus_value: int = 100
        self.yatzy_bonus_enabled: bool = True
        self.yatzy_bonus_max: int = 300
        
        
    def _scoring_options(self)->dict:
        option: int = 1
        options: dict = {}
        for name in self.__class__.__dict__.keys():
            if '_score' in str(name):
                options[str(option)] = self.__getattribute__(name)
                option += 1
        return options  

    @property
    def game_over(self)->bool:
        return self.current_player.plays_left <= 0   

    @property
    def is_yatzy_bonus(self)->bool:
        return  self.yatzy_bonus_enabled \
                and self.current_player.hand.is_yatzy \
                and self.current_player.scorecard.yatzy == self.yatzy_value
    
    def add_yatzy_bonus(self):
        self.current_player.scorecard.yatzy_bonus = self.current_player.scorecard.yatzy_bonus + self.yatzy_bonus_value \
                                                    if self.current_player.scorecard.yatzy_bonus < self.yatzy_bonus_max \
                                                    else self.currrent_player.scorecard.yatzy_bonus
    
    def score_hand(self, option):
        self._options[option]()

    @yatzy_Bonus
    def _score_ones(self):
       self.current_player.scorecard.ones = self.current_player.hand.total_by_value(1)

    @yatzy_Bonus
    def _score_twos(self):
        self.current_player.scorecard.twos = self.current_player.hand.total_by_value(2)  
    
    @yatzy_Bonus
    def _score_threes(self):
        self.current_player.scorecard.threes = self.current_player.hand.total_by_value(3)

    @yatzy_Bonus
    def _score_fours(self):
        self.current_player.scorecard.fours = self.current_player.hand.total_by_value(4)

    @yatzy_Bonus
    def _score_fives(self):
        self.current_player.scorecard.fives = self.current_player.hand.total_by_value(5)

    @yatzy_Bonus
    def _score_sixes(self):
        self.current_player.scorecard.sixes = self.current_player.hand.total_by_value(6)

    @yatzy_Bonus
    def _score_3_kind(self):
        self.current_player.scorecard.three_of_kind = self.current_player.hand.total \
            if self.current_player.hand.is_three_kind else 0
    
    @yatzy_Bonus
    def _score_4_kind(self):
        self.current_player.scorecard.four_of_kind = self.current_player.hand.total \
            if self.current_player.hand.is_four_kind else 0
        
    @yatzy_Bonus
    def _score_fullhouse(self):
        self.current_player.scorecard.fullhouse = self.fullhouse_value \
            if self.current_player.hand.is_fullhouse else 0 
    
    @yatzy_Bonus
    def _score_sm_straight(self):
        self.current_player.scorecard.sm_straight = self.sm_straight_value \
            if self.current_player.hand.is_sm_straight else 0

    @yatzy_Bonus
    def _score_lg_straight(self):
        self.current_player.scorecard.lg_straight = self.lg_straight_value \
            if self.current_player.hand.is_lg_straight else 0

    @yatzy_Bonus
    def _score_yatzy(self):
        self.current_player.scorecard.yatzy = self.yatzy_value \
            if self.current_player.hand.is_yatzy else 0
    
    @yatzy_Bonus
    def _score_chance(self):
        self.current_player.scorecard.chance = self.current_player.hand.total 
    
    def get_winner(self):
        player_grand_total_dict = {}
        for player in self.player_list:
            player_grand_total_dict[player.scorecard.grand_total] = player
        return player_grand_total_dict[max(player_grand_total_dict.keys())]

    def _next_player_gen(self):
        while True:
            for player in self.player_list:
                yield player
    
    def get_next_player(self):
        self.current_player = next(self._next_player)
