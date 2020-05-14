import random

class Die:
    def __init__(self, sides: int=2):
        self.sides = sides
        self._value: int = 1
 
    @property
    def value(self):
        return self._value

    def roll(self):
        random.seed(random.randint(1467, 6504838)*random.randint(157, 6504838))
        self._value = random.randint(1, self.sides)

    def __int__(self): # pragma: no cover
        return int(self._value)
        
    def __eq__(self, value): # pragma: no cover
        return self.value == value
    
    def __add__(self, other): # pragma: no cover
        return self.value + other
    
    def __radd__(self, other): # pragma: no cover
        return self.__add__(other)
    
    def __gt__(self, value): # pragma: no cover
        return self._value > value

    def __ge__(self, value): # pragma: no cover
        return self._value >= value

    def __lt__(self, value): # pragma: no cover  
        return self._value < value

    def __le__(self, value): # pragma: no cover  
        return self._value <= value

    def __str__(self): # pragma: no cover
        return str(self._value)

    def __hash__(self): # pragma: no cover
        return hash(self._value)
    
    def __repr__(self): # pragma: no cover
        return self._value


class Six_sided_die(Die): # pragma: no cover
    def __init__(self):
        super().__init__(sides=6)