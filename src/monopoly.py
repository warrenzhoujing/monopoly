import logging
from random import shuffle
from random import randrange
from collections import deque

from src.log_config import config_logger

board = ["Go", "Gelang Road", "Comunity Chest", "Serangoon Road", "Income Tax", "Ang Mo Kio Station",
         "Farrer Road", "Chance", "Braddell Road", "Thomson Road", "Jail", "Battery Road", "Empress Place",
         "Empress Place", "Connaught Drive", "City Hall Station", "Colombo Court", "Havelock Road",
         "ST Andrews Road", "Free Parking", "Robinson Road", "Chance", "Shenton Way", "Coller Quay",
         "Jurong East Station", "Marina Square", "Emerald Hill", "Water Works", "Raffles City", "Jail",
         "Tanglin Road", "Orchard Road", "Community Chest", "Scotts Road", "Bedok Station", "Chance", "Nassim Road",
         "Super Tax", "Queen Astrid Park"]

chance_cards_list = [
    "Make general repairs on all of your Property. For each House pay $250. For each Hotel pay $1,000.",
    "Your building loan matures. Receive $1,500.",
    "GET OUT OF JAIL FREE. This card may be kept until needed or sold.",
    "Advance to BATTERY ROAD. IF you pass GO collect $2,000.",
    "Advance to COLLER QUAY. IF you pass GO collect $2,000.",
    "Advance to QUEEN ASTRID PARK. IF you pass GO collect $2,000.", "Advance to GO. Collect $2,000.",
    "Go back three spaces.", "Pay school fees of $1,500.", "Bank pays you dividend of $500.",
    "Take a ride to CITY HALL STATION. IF you pass GO collect $2,000.",
    "You are assessed for street repairs: per House $400; per Hotel $1,150.",
    "You have won a crossword competition. Collect $2,000.", "Speeding fine. Pay $150.",
    "Drunk in charge. $200 fine", "Go to jail. Move directly to Jail. DO NOT PASS GO SO, DO NOT COLLECT $2,000."]
shuffle(chance_cards_list)
#chance_cards_deque = deque(chance_cards_list)
chance_cards_deque = deque(["Bank pays you dividend of $500."])


class Player:
    def __init__(self, name):
        self.__name = name
        self.__location = 0
        self.__won = False
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

    def at_chance(self):
        return board[self.__location] == 'Chance'

    def pay(self, amount):
        self.__money -= amount

    def __str__(self):
        return "{} with ${} is at {}".format(self.__name, self.__money, board[self.__location])


def main():
    config_logger()
    players = [Player('Felix'), Player('John')]

    play(players)


def play(players):
    turn = 1
    while turn <= 10:
        player = pick_player(players, turn)

        player.throw_dice()
        logging.debug(player.dice)

        player.location += player.dice[0] + player.dice[1]
        logging.debug(str(player))

        check_at_chance(player)

        turn += 1
        logging.debug("\n")


def check_at_chance(player):
    if player.at_chance():
        chance_top_card = chance_cards_deque.popleft()
        logging.debug(chance_top_card)
        chance_cards_deque.append(chance_top_card)
        if chance_top_card == 'Pay school fees of $1,500.':
            player.pay(1500)
            logging.debug(str(player))
        elif chance_top_card == 'Bank pays you dividend of $500.':
            player.pay(-500)
            logging.debug(str(player))


def pick_player(players, turn):
    index = turn % len(players)
    player = players[index]
    logging.debug(player)
    return player


if __name__ == '__main__':
    main()
