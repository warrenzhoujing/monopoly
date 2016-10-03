import logging
from random import randrange

from src.board import board


class Player:
    def __init__(self, name):
        self.__name = name
        self.__location = 0
        self.__in_jail = False
        self.__jail_dice_count = 0
        self.__dice = (0, 0)
        self.__money = 15000

    def throw_dice(self):
        self.__dice = (randrange(1, 6), randrange(1, 6))

    @property
    def dice(self):
        return self.__dice

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        self.__location = value

    @property
    def in_jail(self):
        return self.__in_jail

    @in_jail.setter
    def in_jail(self, value):
        self.__in_jail = value

    @property
    def jail_dice_count(self):
        return self.__jail_dice_count

    @jail_dice_count.setter
    def jail_dice_count(self, value):
        self.__jail_dice_count = value

    def get_out_of_jail(self):
        self.in_jail = False
        self.jail_dice_count = 0
        logging.debug("%s has gotten out of jail" % self.__name)

    def at_chance(self):
        return board[self.__location] == 'Chance'

    def pay(self, amount):
        self.__money -= amount
        if amount > 0:
            logging.debug("%s has paid %d" % (self.__name, amount))
        else:
            logging.debug("%s has been paid %d" % (self.__name, -amount))

    def receive(self, amount):
        self.pay(-amount)

    def __str__(self):
        state = "{} with ${} is %s {}".format(self.__name, self.__money, board[self.__location])

        if self.__in_jail:
            return state % "in"
        return state % "visiting"
