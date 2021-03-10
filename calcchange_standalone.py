"""
Write a program to return the current change for a given dollar dollar amount.
The results should be pretty printed for the user

EXAMPLE:
    calcChange(3.43)
OUTPUT:
    Pennies: 3, Nickels: 1, Dimes: 1, Quarters: 1, Dollars: 3


"""


class Change:
    def __init__(self):
        self.pennies = 10
        self.nickels = 0
        self.dimes = 0
        self.quarters = 0
        self.dollars = 0

    def __str__(self):
        # This should probably return something appropriate
        return "?"


def calc_change(dollar_amount):
    # We should update the Change object to have the right values
    return Change()


calc_change(3.43)
