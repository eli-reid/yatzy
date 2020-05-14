class Scorecard:

    def __init__(self):
        self._ones: int = None
        self._twos: int = None
        self._threes: int = None
        self._fours: int = None
        self._fives: int = None
        self._sixes: int = None
        self._three_of_kind: int = None
        self._four_of_kind: int = None
        self._fullhouse: int = None
        self._sm_straight: int = None
        self._lg_straight: int = None
        self._yatzy: int = None 
        self._chance: int = None
        self._yatzy_bonus: int = 0
        self._lower_bonus: int = 0
        self._upper_bonus: int = 0


    @property
    def ones(self):
        return '' if self._ones == None else self._ones
    
    @ones.setter 
    def ones(self, value):
        if self._ones is None:
            self._ones = value
        else:
            raise ValueError("Ones have already been set!")

    @property
    def twos(self):
        return '' if self._twos == None else self._twos
    
    @twos.setter 
    def twos(self, value):
        if self._twos is None:
            self._twos = value
        else:
            raise ValueError("Twos have already been set!")

    @property
    def threes(self):
        return '' if self._threes == None else self._threes
    
    @threes.setter
    def threes(self, value):
        if self._threes is None:
            self._threes = value
        else:
            raise ValueError("Threes have already been set!")

    @property
    def fours(self):
        return '' if self._fours == None else self._fours
    
    @fours.setter
    def fours(self, value):
        if self._fours is None:
            self._fours = value
        else:
            raise ValueError("Fours have already been set!")

    @property
    def fives(self):
        return '' if self._fives == None else self._fives
    
    @fives.setter
    def fives(self, value):
        if self._fives is None:
            self._fives = value
        else:
            raise ValueError("Fives have already been set!")

    @property
    def sixes(self):
        return '' if self._sixes == None else self._sixes
    
    @sixes.setter
    def sixes(self, value):
        if self._sixes is None:
            self._sixes = value
        else:
            raise ValueError("Sixes have already been set!")

    @property
    def three_of_kind(self):
        return '' if self._three_of_kind == None else self._three_of_kind
    
    @three_of_kind.setter
    def three_of_kind(self, value):
        if self._three_of_kind is None:
            self._three_of_kind = value
        else:
            raise ValueError("Three of a kind has already been set!")
    
    @property
    def four_of_kind(self):
        return '' if self._four_of_kind == None else self._four_of_kind
    
    @four_of_kind.setter
    def four_of_kind(self, value):
        if self._four_of_kind is None:
            self._four_of_kind = value
        else:
            raise ValueError("Four of a kind has already been set!")

    @property
    def fullhouse(self):
        return '' if self._fullhouse == None else self._fullhouse
    
    @fullhouse.setter
    def fullhouse(self, value):
        if self._fullhouse is None:
            self._fullhouse = value
        else:
            raise ValueError("Full house has already been set!")

    @property
    def sm_straight(self):
        return '' if self._sm_straight == None else self._sm_straight
    
    @sm_straight.setter
    def sm_straight(self, value):
        if self._sm_straight is None:
            self._sm_straight = value
        else:
            raise ValueError("Small straight has already been set!")
    
    @property
    def lg_straight(self):
        return '' if self._lg_straight == None else self._lg_straight
    
    @lg_straight.setter
    def lg_straight(self, value):
        if self._lg_straight is None:
            self._lg_straight = value
        else:
            raise ValueError("Large Straight has already been set!")

    @property
    def yatzy(self):
        return '' if self._yatzy == None else self._yatzy
    
    @yatzy.setter
    def yatzy(self, value):
        if self._yatzy is None:
            self._yatzy = value
        else:
            raise ValueError("Yatzy has already been set!")

    @property
    def chance(self):
        return '' if self._chance == None else self._chance
    
    @chance.setter
    def chance(self, value):
        if self._chance is None:
            self._chance = value
        else:
            raise ValueError("Four of a kind has already been set!")

    @property
    def yatzy_bonus(self):
        return self._yatzy_bonus
    
    @yatzy_bonus.setter
    def yatzy_bonus(self, value):
        self._yatzy_bonus = value

    @property
    def upper_score(self):
        upper_score = 0
        upper_score += self.ones or 0
        upper_score += self.twos or 0
        upper_score += self.threes or 0
        upper_score += self.fours or 0
        upper_score += self.fives or 0
        upper_score += self.sixes or 0
        return upper_score

    @property
    def upper_bonus(self):
       return 35 if self.upper_score > 63 else 0

    @property
    def upper_total(self):
        return self.upper_bonus + self.upper_score
    
    @property
    def lower_total(self):
        return (self.three_of_kind or 0) \
                + (self.four_of_kind or 0) \
                + (self.fullhouse or 0)\
                + (self.sm_straight or 0) \
                + (self.lg_straight or 0) \
                + (self.yatzy or 0) \
                + (self.chance or 0)
    @property
    def grand_total(self):
        return self.upper_total + self.yatzy_bonus + self.lower_total

    @property
    def plays_left(self):
        return list(self.__dict__.values()).count(None)