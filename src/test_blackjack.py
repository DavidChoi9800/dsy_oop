from blackjack_deck import Card, Deck
from blackjack_rules import Rules
from blackjack_player import Dealer, Player
import blackjack as blackjack
import nose.tools as n


rules = Rules()

def test_value():
    cards = [Card('5', 'c'), Card('K', 'd')]
    n.assert_equal(rules.total_value(cards), 15)

def test_ace_value1():
    cards = [Card('6', 'c'), Card('A', 'd')]
    n.assert_equal(rules.total_value(cards), 17)

def test_ace_value2():
    cards = [Card('7', 'c'), Card('J', 's'), Card('A', 'd')]
    n.assert_equal(rules.total_value(cards), 18)


# def test_player_take_card():
#     player = HumanPlayer('player', 100)
#     player.take_card((Card('J', 's')))
#     n.assert_equal(len(player.cards), 1)
#     n.assert_equal(
#         player.cards[0].number == 'J' and player.cards[0].suit == 's', True
#     )
