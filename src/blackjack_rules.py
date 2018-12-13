class Rules(object):
    def total_value(self, cards):
        total_value = 0

        for card in cards:
            if card.number.isdigit():
                total_value += int(card.number)
            elif card.number in "JQK":
                total_value += 10
            elif total_value <= 10:
                total_value += 11
            else:
                total_value += 1

        return total_value

    def is_blackjack(self, cards):
        if len(cards) == 2 and self.total_value(cards) == 21:
            print "WTF~~ It's blackjack"
            return True
        else:
            print "Blackjack? Fuck you. It's just illusion"
            print "Your cards are {} and {}".format(cards[0], cards[1])
            return False
