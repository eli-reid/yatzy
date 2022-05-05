import random
import os
from Dice import Six_sided_die, Die
class Hand_of_dice:
    """ Hand of dice makes creates a list of die objects
    :param number: How many dice does the hand have
    :type number: int
    :param value: Die object pointer
    :type value: Die
    """
    
    def __init__(self, number: int=2, die: Die=Die):
        self._dice = [die() for n in range(number)]
    
    @property
    def total(self)->int:
        """ Adds all dice together 
        
        :return: sum 
        :rtype: int
        """
        return sum(self._dice)

    def total_by_value(self, value: int)->int:
        """ Adds dice with the same value
        
        :param value: die value to total
        :type value: int
        :return: sum
        :rtype: int
        """
        return self._dice.count(value) * value
        
    def count(self, value: int)->int:
        """ Counts dice with same value
        
        :param value: die value to count
        :type value: int
        :return: count
        :rtype: int
        """
        return self._dice.count(value)
    
    def sort(self):
        """ Sort dice """             
        self._dice.sort()

    def is_vaild_roll(self, dice_to_roll: str)->bool:
        """Validate roll str
        
        :param dice_to_roll: a string of intergers with what dice to roll
        :type dice_to_roll: str
        :return: bool
        :rtype: bool
        """
        if dice_to_roll.isnumeric():
            dice_to_roll_list = sorted(list(dice_to_roll))
            if int(dice_to_roll_list[-1]) - 1 < len(self._dice) and int(dice_to_roll[0])-1 >= 0:
                return True
        return False
        
    def roll(self, dice_to_roll: str=''):
        """ Checks string for dice to roll if none are given it rolls all dice
        
        :param dice_to_roll: a string of intergers for dice , defaults to ''
        :type dice_to_roll: str, optional
        """
        if len(dice_to_roll) == 0:
            self._roll_all()
        else:
            self._roll_dice(dice_to_roll)
    
    def _roll_all(self):
        """ Rolls all dice """
        for die in self:
             die.roll()

    def _roll_dice(self, dice_to_roll: str):
        """Rolls selected dice
        
        :param dice_to_roll:  a string of intergers for dice
        :type dice_to_roll: str
        :raises ValueError:  If roll string is invalid 
        """
        if not self.is_vaild_roll(dice_to_roll):
            raise ValueError("Invalid roll selection!")
        for die in set(dice_to_roll):
            self._dice[int(die)-1].roll()
    
    def __eq__(self, value): # pragma: no cover
        return self._dice == value

    def __len__(self): # pragma: no cover
        return len(self._dice)

    def __iter__(self): # pragma: no cover
        return iter(self._dice)

    def __getitem__(self, item): # pragma: no cover
        return self._dice[item]

    def __str__(self): # pragma: no cover
        return str([int(die) for die in self._dice])
     
    def __repr__(self): # pragma: no cover
        return self._dice

class yatzy_hand(Hand_of_dice):
    def __init__(self):
        super().__init__(5, Six_sided_die)

    @property
    def is_three_kind(self):
        return self.count(sorted(self)[2]) >= 3

    @property
    def is_four_kind(self)->bool:
        return self.count(sorted(self)[2]) >= 4

    @property
    def is_fullhouse(self)->bool:
        return self.count(sorted(self)[0]) \
            + self.count(sorted(self)[4]) == 5 \
            and not self.is_four_kind

    @property
    def is_sm_straight(self)->bool:
        return set(sorted(self)).issubset({1,2,3,4,5,6}) and len(set(self)) >= 4

    @property
    def is_lg_straight(self)->bool:
        return set(sorted(self)).issubset({1,2,3,4,5,6}) and len(set(self)) == 5

    @property 
    def is_yatzy(self)->bool:
        return self.count(self._dice[0]) == 5


class Test_Hand(yatzy_hand): # pragma: no cover
        def __init__(self, dice: list):
            self._dice :list = dice