from war_player import Player

class BlackjackPlayer(Player):
    def __init__(self, name):
        super(Blackjack, self).__init__(name)
        self.staying = False

    def receive_card(self, card):
        self.hand.append(card)

    def choice(self, dealer_card):
        print "Your hand is {}".format(show_hand())
        print "The deal is showing {}".format(dealer_card)
        player_choice = raw_input("(H)it or (S)tay")
        if player_choice == "S":
            self.staying = True
        return self.staying



    def show_hand(self):
        for card in self.hand:
            print card

    def get_state(self):
        return self.staying

    def get_total(self):
        return sum(self.hand)



class BlackjackDealer(BlackjackPlayer):

    def get_dealer_card(self):
        return self.hand[1]

    def choice(self):
        if sum(self.hand) <= 16:
            self.staying = False
        else:
            self.staying = True
        return self.staying
