import random

class Dice():
    """A dice object with a number of sides and a result"""
    def __init__(self, sides):
        self.sides = sides
        self.res = 0

    def roll(self):
        """Roll the dice and return the result"""
        self.res = random.randint(1, self.sides)

    def high_pass(self, threshold):
        """Return the result if it is above the threshold, otherwise return 0"""
        if self.res > threshold:
            return self.res
        else:
            return 0

    def low_pass(self, threshold):
        """Return the result if it is below the threshold, otherwise return 0"""
        if self.res < threshold:
            return self.res
        else:
            return 0

    def reroll(self, threshold):
        """Return the result if it is below the threshold, otherwise roll again"""
        if self.res < threshold:
            return self.res
        else:
            return self.roll()

    def __str__(self):
        """Return the result as a string"""
        return str(self.res)

    def __repr__(self):
        """Return the result as a string"""
        return str(self.res)

    def __int__(self): 
        """Return the result as an integer"""
        return self.res

    def __float__(self): 
        """Return the result as a float"""
        return float(self.res)

    def __add__(self, other):
        """Return the sum of the result and another number"""
        return self.res + other

    def __sub__(self, other):
        """Return the difference of the result and another number"""
        return self.res - other

    def __mul__(self, other):
        """Return the product of the result and another number"""
        return self.res * other

    def __truediv__(self, other):
        """Return the quotient of the result and another number"""
        return self.res / other

    def __floordiv__(self, other):
        """Return the quotient of the result and another number"""
        return self.res // other

    def __mod__(self, other):
        """Return the remainder of the result and another number"""
        return self.res % other

    def __pow__(self, other):
        """Return the result to the power of another number"""
        return self.res ** other

    def __lt__(self, other):
        """Return True if the result is less than another number"""
        return self.res < other

    def __le__(self, other):
        """Return True if the result is less than or equal to another number"""
        return self.res <= other

    def __eq__(self, other):
        """Return True if the result is equal to another number"""
        return self.res == other

    def __ne__(self, other):
        """Return True if the result is not equal to another number"""
        return self.res != other

    def __gt__(self, other):
        """Return True if the result is greater than another number"""
        return self.res > other

    def __ge__(self, other):
        """Return True if the result is greater than or equal to another number"""
        return self.res >= other   

