from blackjack_deck import Deck
from blackjack_player import Player, Dealer
from blackjack_rules import Rules

class Blackjack(object):

    def __init__(self, amount):
        self.player = Player(amount)
        self.dealer = Dealer()
        self.deck = Deck()
        self.rules = Rules()

        # self.play()

    def play(self):
        while self.player.money > 0:
            self.play_once()

    def play_once(self):
        amount = self.player.bet()
        self.deck.shuffle()
        dealer_hand = []
        player_hand = []

        #intial draw
        for i in xrange(2):
            dealer_hand.append(self.deck.draw_card())
            player_hand.append(self.deck.draw_card())

        if self.rules.is_blackjack(player_hand):
            self.player.win( amount * 1.5 )
            return

        #Hit or Stay
        while self.rules.total_value(player_hand) < 21:
            if not self.player.hit(player_hand, dealer_hand[1]):
                break;
            player_hand.append(self.deck.draw_card())


        player_total_value = self.rules.total_value(player_hand)
        if player_total_value >= 21:
            self.player.lose( amount )
            return

        while self.rules.total_value(dealer_hand) < 21:
            if not self.dealer.hit(dealer_hand):
                break;
            dealer_hand.append(self.deck.draw_card())

        dealer_total_value = self.rules.total_value(dealer_hand)

        if player_total_value < dealer_total_value:
            self.player.lose(amount)
        elif player_total_value > dealer_total_value:
            self.player.win(amount)
        else:
            self.player.push()

if __name__ == "__main__":
    blackjack = Blackjack(100)
    blackjack.play()
