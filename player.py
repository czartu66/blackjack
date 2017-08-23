import random


class Player(object):

    card_points = {'Two': 2, "Three": 3, 'Four': 4, "Five": 5, 'Six': 6, 'Seven': 7, "Eight": 8, "Nine": 9, "Ten": 10,
            'Jack': 10, "Queen": 10, "King": 10, "Ace": 11 or 1}
    card = {1: 'Ace', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
            10: 'Ten', 11: 'Jack', 12: 'Queen', 13: 'King'}
    suits = {1: 'Spades', 2: 'Hearts', 3: 'Diamonds', 4: 'Clubs'}

    def __init__(self, money, points=0, bet=0, on_hand=None):
        self.points = points
        self.money = money
        self.bet = bet
        self.on_hand = on_hand

    def give_bet(self):
        """
        In this method player gives a bet and it is subtracted from total money which player has
        :return: total sum of player's money
        """
        while True:
            try:
                self.bet = int(raw_input('Give your bet (Please enter an integer): '))
            except:
                print "You didn't enter an integer, please try again"
                continue
            if self.bet > self.money:
                print "You don't have this amount of money, give smaller value"
            else:
                print "You gave your bet"
                break
        self.money -= self.bet
        return 'Your current money: %d ' % self.money

    def money_win(self):
        """
        In this method player gets double amount of his bet- he wins
        :return: double amount of bet money + player money
        """
        self.money = self.money + (self.bet * 2)
        return self.money

    def money_draw(self):
        """
        In this method player gets his money back - it's a draw
        :return: amount of bet money + player money
        """

    def drawing(self):
        """
        This metod draw random cards from deck of cards
        :return: Two cards which are on hand of a player
        """
        self.on_hand = \
            str(random.choice(Player.card.values())) + " of " + str(random.choice(Player.suits.values()))+'\n'
        self.on_hand =  \
            self.on_hand + str(random.choice(Player.card.values())) + " of " + str(random.choice(Player.suits.values()))
        return self.on_hand

    def check_actual_points(self):
        """
        This method checks actual points of a Player
        :return: Actual points value
        """
        cards = self.on_hand.split('\n')
        cards_values = [i.split()[0] for i in cards]
        self.points = 0
        for element in xrange(0, len(cards_values)):
            points = [val for key, val in Player.card_points.iteritems() if key == cards_values[element]]
            points = map(str, points)
            points = int(''.join(points))
            self.points += points
            element += 1
        return self.points

    def choose_val_of_ace(self):
        """
        In this method Player can choose which value will have an Ace card
        """
        while True:
            val_of_ace = int(raw_input('Choose value of Ace(you can choose 1 or 11): '))
            if val_of_ace == 1:
                Player.card_points['Ace'] = 1
                break
            if val_of_ace == 11:
                Player.card_points['Ace'] = 11
                break
            else:
                print 'You gave incorrect value, choose between 1 or 11'

    def choose_action(self):
        """
        In this method Player choose one from two avaible actions: hit or stand
        """
        while True:
            action = raw_input("Choose action (You can choose 'hit' or 'stand'): ")
            if action == 'hit':
                print 'You chose hit action'
                self.on_hand = self.on_hand + '\n' + str(random.choice(Player.card.values())) \
                               + " of " + str(random.choice(Player.suits.values()))
                print 'Your cards: ' + '\n' + self.on_hand
                print 'Your actual points: ',  self.check_actual_points()
                break
            if action == 'stand':
                print 'You chose stand action'
                break
            else:
                print "You chose wrong action. Try again, choose 'hit' or 'stand'"
                continue




