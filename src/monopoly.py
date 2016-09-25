import random

places = ["Go", "Gelang Road", "Comunity Chest", "Serangoon Road", "Income Tax", "Ang Mo Kio Station",
          "Farrer Road", "Chance", "Braddell Road", "Thomson Road", "Jail", "Battery Road", "Empress Place",
          "Empress Place", "Connaught Drive", "City Hall Station", "Colombo Court", "Havelock Road",
          "ST Andrews Road", "Free Parking", "Robinson Road", "Chance", "Shenton Way", "Coller Quay",
          "Jurong East Station", "Marina Square", "Emerald Hill", "Water Works", "Raffles City", "Go to Jail",
          "Tanglin Road", "Orchard Road", "Community Chest", "Scotts Road", "Bedok Station", "Chance", "Nassim Road",
          "Super Tax", "Queen Astrid Park"]


class Player:
    def __init__(self, name):
        self.__name = name
        self.__location = 0
        self.__won = False
        self.__dice = (0, 0)
        self.__money = 15000

    def throw_dice(self):
        self.__dice = (random.randrange(1, 6), random.randrange(1, 6))

    @property
    def dice(self):
        return self.__dice

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        self.__location = value

    def __str__(self):
        return "{} is at {}".format(self.__name, places[self.__location])


def main():
    players = [Player('Felix'), Player('John')]

    turn = 1
    while turn <= 10:
        index = turn % len(players)
        player = players[index]
        print(player)
        player.throw_dice()
        print(player.dice)
        player.location += player.dice[0] + player.dice[1]
        print(player)
        print()

        turn += 1

if __name__ == '__main__':
    main()
