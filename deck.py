from player import Player
import random


class Deck(Player):
    def __init__(self, money2):
        super(Deck, self).__init__(money2)

    def deck_action(self):
        while True:
            print('Deck actual points: ', self.check_actual_points())
            if self.points <= 16:
                print('Deck chose hit action')
                self.on_hand = self.on_hand + '\n' + str(random.choice(list(Player.card.values()))) \
                    + " of " + str(random.choice(list(Player.suits.values())))
                print('Cards on deck: ' + '\n' + self.on_hand)
                print('Deck actual points: ', self.check_actual_points())
                break
            else:
                print('Deck chose a stand action')
                print('Deck actual points: ', self.check_actual_points())
                break
