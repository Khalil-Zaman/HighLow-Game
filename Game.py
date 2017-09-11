import random

printplay = False
cards = []


def deck():
    for i in range(1, 53):
        cards.append(i)


def print_card(i):
    i = i % 13
    if i == 0:
        return 'A'
    elif i == 12:
        return 'K'
    elif i == 11:
        return 'Q'
    elif i == 10:
        return 'J'
    else:
        i = i + 1
        return str(i)

deck()


class Player:

    player_cards = []
    player_number = 0
    cards = []

    def __init__(self, player_number):
        self.player_cards = []
        self.player_number = player_number
        for i in range(0, 26-len(self.player_cards)):
            card = random.randint(0, len(cards)-1)
            self.player_cards.append(cards[card])
            cards.pop(card)

    def no_cards(self):
        return len(self.player_cards)

    def print_cards(self):
        print("Player " + str(self.player_number) + ". Cards: ", end="")
        for i in range(0, len(self.player_cards)):
            print(print_card(self.player_cards[i]), end=" ")
        print("")

    def set_cards(self, cs):
        self.player_cards.clear()
        for c in cs:
            self.player_cards.append(c)

    def play(self):
        if len(self.player_cards) > 0:
            c = self.player_cards[0]%13
            self.player_cards.pop(0)
            return c
        else:
            return -1

    def add(self, cs):
        for c in cs:
            self.player_cards.append(c)


def play_game(iteration_number = 1000):
    won = []
    iterations = 1
    player_won = random.randint(1, 2)
    while ((player1.no_cards() > 0) and (player2.no_cards() > 0)) and iterations <= iteration_number:
        if player_won == 1:
            c1 = player1.play()
            c2 = player2.play()
            won.append(c1)
            won.append(c2)
            if c1 > c2:
                player1.add(won)
                won.clear()
            elif c2 > c1:
                player2.add(won)
                won.clear()
        else:
            c1 = player1.play()
            c2 = player2.play()
            won.append(c2)
            won.append(c1)
            if c1 > c2:
                player1.add(won)
                won.clear()
            elif c2 > c1:
                player2.add(won)
                won.clear()
        print("Iteration " + str(iterations))
        player1.print_cards()
        player2.print_cards()
        iterations += 1
        print("")


def hack_the_game():
    player1.set_cards([
        12, 11, 10, 9, 8, 7, 6,
        25, 24, 23, 22, 21, 20, 21,
        38, 37, 36, 35, 34, 33,
        51, 50, 49, 48, 47, 46])
    player2.set_cards([
        1, 2, 3, 4, 5,
        13, 14, 15, 16, 17, 18, 19,
        26, 27, 28, 29, 30, 31, 32,
        39, 40, 41, 42, 43, 44, 45])

player1 = Player(1)
player2 = Player(2)

print("Initial cards: ")
player1.print_cards()
player2.print_cards()
print("")

#hack_the_game()
play_game(1000)