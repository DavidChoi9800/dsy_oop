from blackjack_rules import Rules


class Dealer(object):
    def hit(self, cards):
        self.rules = Rules()
        return self.rules.total_value(cards) <= 16


class Player(object):
    def __init__(self, money):
        self.name = raw_input("Enter your name: ")
        print "Welcome {}".format(self.name)
        self.money = money

    def bet(self):
        amount = 0
        while not (amount > 0 and amount <= self.money):
            amount = input("You have %d money. How much would you like to bet? " % self.money)
        return amount

    def win(self, amount):
        print "You won %d! " % amount
        self.money += amount

    def lose(self, amount):
        print "You lost %d! " % amount
        self.money -= amount

    def push(self):
        print "Wow push!!!"

    def hit(self, player_cards, dealer_card ):
        str_player_cards = " ".join([str(card) for card in player_cards])
        print "You have {}.".format(str_player_cards)
        print "Dealer has {}.".format(str(dealer_card))

        while True:
            choice = raw_input( "What would you like to do? hit or stay(Hit/Stay)?" )
            if choice.lower() in ("hit", "h"):
                return True
            if choice.lower() in ("stay", "s"):
                return False
