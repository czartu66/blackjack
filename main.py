from player import Player
from deck import Deck

p = Player(100)
d = Deck(1000)

while True:
    print(p.give_bet())
    p.drawing()
    d.drawing()

    print('Your cards: ' + '\n')
    print(p.on_hand)
    print('First card on Deck: ' + '\n')
    print(d.on_hand.split('\n', 1)[0])
    if 'Ace' in p.on_hand:
        p.choose_val_of_ace()
        print('Your actual points: ', p.check_actual_points())
    else:
        print('Your actual points: ', p.check_actual_points())
    while True:
        p.choose_action()
        if p.points < 21:
            print('Cards on Deck: ')
            print(d.on_hand)
            d.deck_action()
        if d.points > 21 or p.points == 21 or 21 - p.points < 21 - d.points:
            print('You won')
            p.money_win()
            break
        elif d.points == 21 or 21 - d.points < 21 - p.points or p.points > 21:
            print('Deck won')
            break
        elif p.points > 21 and d.points > 21:
            print("It's a draw")
            p.money_draw()
            break
    finish = input('Do you want to finish the game? [answer yes or no]' + '\n')
    while finish != 'yes' or finish != 'no':
        break
    if finish == 'yes' or p.money == 0:
        print('You finished or you dont have enough money')
        break
# print d.give_bet()
