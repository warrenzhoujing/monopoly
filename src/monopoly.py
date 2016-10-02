import logging
from collections import deque
from random import shuffle

from src.log_config import config_logger
from src.player import Player

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
    "Drunk in charge. $200 fine", "Go to jail. Move directly to Jail. DO NOT PASS GO, DO NOT COLLECT $2,000."]
shuffle(chance_cards_list)
# chance_cards_deque = deque(chance_cards_list)
chance_cards_deque = deque(["Go to jail. Move directly to Jail. DO NOT PASS GO, DO NOT COLLECT $2,000."])


def main():
    config_logger()
    players = [Player('Felix'), Player('John')]
    play(players)


def play(players):
    turn = 1
    while turn <= 10:
        player = pick_player(players, turn)

        throw_dice(player)
        update_state(player)
        check_at_chance(player)

        turn += 1
        logging.debug("\n")


def throw_dice(player):
    player.throw_dice()
    logging.debug(player.dice)


def update_state(player):
    if player.in_jail:
        player.jail_dice_count += 1

        if player.jail_dice_count < 3:
            if player.dice[0] == player.dice[1]:
                player.get_out_of_jail()
        else:
            player.pay(50)
            player.get_out_of_jail()
    else:
        player.location += player.dice[0] + player.dice[1]

    logging.debug(player)


def check_at_chance(player):
    if player.at_chance():
        chance_top_card = chance_cards_deque.popleft()
        chance_cards_deque.append(chance_top_card)

        logging.debug("Chance card: %s" % chance_top_card)

        if chance_top_card == 'Pay school fees of $1,500.':
            player.pay(1500)
        elif chance_top_card == 'Bank pays you dividend of $500.':
            player.pay(-500)
        elif chance_top_card == 'Go back three spaces.':
            player.location -= 3
        elif chance_top_card == 'You have won a crossword competition. Collect $2,000.':
            player.pay(-2000)
        elif chance_top_card == 'Go to jail. Move directly to Jail. DO NOT PASS GO, DO NOT COLLECT $2,000.':
            player.location = 10
            player.in_jail = True

        logging.debug(player)


def pick_player(players, turn):
    index = turn % len(players)
    player = players[index]
    logging.debug(player)
    return player


if __name__ == '__main__':
    main()
