with open('poker.txt') as f:
    data = f.readlines()
    
# http://www.daniweb.com/software-development/python/threads/256610   
class Card():
    SUIT = { 'C':'Clubs', 'D':'Diamonds', 'H':'Hearts', 'S':'Spades' }
    VALUES = { '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, \
                        '10':10, 'J':12, 'Q':13, 'K':14, 'A':15 }

    def __init__(self,ctupl):
        """ New card instance.
        'ctupl' = (str,str): denoting (SUIT,VALUES) """
        if type(ctupl) != tuple:
            raise TypeError("Need (str,str) tuple.")
        self.suit = ctupl[0]
        self.value = ctupl[1]

    def __init__(self,suit,value):
        if type(suit) != str or type(value) != str:
            raise TypeError("Need str,str as parameters.")
        self.suit = suit
        self.value = value

    def __cmp__(self,other):
        """ Overide __cmp__ method.
        Compare two cards. """
        if Card.VALUES[self.value] < Card.VALUES[other.value]:
            return -1
        elif Card.VALUES[self.value] > Card.VALUES[other.value]:
            return 1
        else:
            # Can go SUIT comparison
            return 0
            
    def __str__(self):
        """ Overriding to_string() function """
        return "%s of %s" % (self.value,self.SUIT[self.suit])

class PokerHand():
    SIZE = 5
    RANKS = { 0: "Straight Flush", 1: "Four of a Kind", 2: "Full House", \
              3: "Flush", 4: "Straight", 5: "Three of a Kind", \
              6: "Two Pairs", 5: "Pair", 6: "High Card" }

    def __init__(self,player,cards):
        """ New poker hand. (str,[cards]) """
        if len(cards) < PokerHand.SIZE:
            raise ValueError("Invalid hands size: %d/%d" % (len(cards),5))
        self.player = player
        self.cards = cards
        self.cards.sort()

    def __str__(self):
        """ Overriding to_string function """
        return "[%s]: %s" % (self.player, ", ".join([ str(x) for x in self.cards ]))
        
    def isRoyalFlush(self):
        """Royal Flush: Ten, Jack, Queen, King, Ace, in same suit."""
        same_suit = len(set([self.cards[i].suit for i in range(self.SIZE)]))==1
        values = sorted([self.cards[i].value for i in range(self.SIZE)])
        return values

    def isFlush(self):
        """Flush: All cards of the same suit."""
        return len(set([self.cards[i].suit for i in range(self.SIZE)]))==1
        
"""        
High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.

Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
"""


if __name__ == "__main__":
    print "Poker Hands"
    p = PokerHand("Andrei",[Card('C','2'), Card('C','3'), Card('C','4'), Card('C','5'),Card('C','6')])
    print p
    print ("Is %sa flush." % '' if p.isFlush() else 'not ')
