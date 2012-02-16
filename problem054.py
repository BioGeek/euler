# In the card game poker, a hand consists of five cards and are ranked, 
# from lowest to highest, in the following way:
# 
# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
#
# If two players have the same ranked hands then the rank made up of the
# highest value wins; for example, a pair of eights beats a pair of fives 
# (see example 1 below). But if two ranks tie, for example, both players 
# have a pair of queens, then highest cards in each hand are compared (see
# example 4 below); if the highest cards tie then the next highest cards are
# compared, and so on.
#
#Consider the following five hands dealt to two players:
#
# Hand	Player 1	 	    Player 2	 	    Winner
# 1	 	5H 5C 6S 7S KD      2C 3S 8S 8D TD      Player 2
#       Pair of Fives       Pair of Eights
# 	
# 2	 	5D 8C 9S JS AC      2C 5C 7D 8S QH      Player 1
#       Highest card Ace    Highest card Queen
# 	
# 3	 	2D 9C AS AH AC      3D 6D 7D TD QD      Player 2
#       Three Aces          Flush with Diamonds
# 	
# 4	 	4D 6S 9H QH QC      3D 6D 7H QD QS      Player 1
#       Pair of Queens      Pair of Queens
#       Highest card Nine   Highest card Seven
# 	
# 5	 	2H 2D 4C 4D 4S      3C 3D 3S 9S 9D      Player 1
#       Full House          Full House
#       With Three Fours    with Three Threes
# 	
# The file, poker.txt, contains one-thousand random hands dealt to two
# players. Each line of the file contains ten cards (separated by a single
# space): the first five are Player 1's cards and the last five are Player 
# 2's cards. You can assume that all hands are valid (no invalid characters 
# or repeated cards), each player's hand is in no specific order, and in each
# hand there is a clear winner.
#
# How many hands does Player 1 win?

class Card():
  SUITS = { 'C':'Clubs', 'D':'Diamonds', 'H':'Hearts', 'S':'Spades' }
  VALUES = { '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, \
             'T':10, 'J':11, 'Q':12, 'K':13, 'A':14 }
  
  def __init__(self, vs):
    """ New card instance."""
    self.value = vs[0]
    self.numericalvalue = self.VALUES[self.value]
    self.suit = vs[1]
    
  def __cmp__(self,other):
    """ Overide __cmp__ method.
    Compare two cards. """  
    if self.numericalvalue < other.numericalvalue:
      return -1
    elif self.numericalvalue > other.numericalvalue:
      return 1
    else:
      # Can go SUIT comparison
      return 0
      
  def __str__(self):
    """ Overriding to_string() function """
    return "%s of %s" % (self.value,self.SUITS[self.suit])
   
 
class Hand():
  """ A Poker hand"""
  def __init__(self, cards):
    """ New poker hand."""
    self.cards = [Card(card) for card in cards.split()]
    self.cards.sort()
    self.values = [card.value for card in self.cards]
    self.suits  = [card.suit  for card in self.cards]
 
  def __str__(self):
    """ Overriding to_string function """
    return ", ".join([ str(x) for x in self.cards ])
    
  def _all_same_suit(self):
    return len(set(self.suits)) == 1
      
  def _all_consecutive_values(self):
    return all([self.cards[i].numericalvalue+1==self.cards[i+1].numericalvalue \
                for i in range(len(self.cards)-1)])
  
    
  def is_royal_flush(self):
    """Ten, Jack, Queen, King, Ace, in same suit."""
    return self._all_same_suit() and \
           self.values == ['T', 'J', 'Q', 'K', 'A']
    
  def is_straight_flush(self):
    """All cards are consecutive values of same suit."""
    return self._all_same_suit() and self._all_consecutive_values()
    
  def is_four_of_a_kind(self):
    """Four cards of the same value"""
    return 4 in [self.values.count(i) for i in set(self.values)]
    
  def is_full_house(self):
    """Three of a kind and a pair"""
    return self.is_three_of_a_kind() and self.is_one_pair()
    
  def is_flush(self):
    """All cards from the same suit"""
    return self._all_same_suit()
    
  def is_straight(self):
    """All cards are consecutive values"""
    return self._all_consecutive_values()
    
  def is_three_of_a_kind(self):
    """Three cards of the same value"""
    return 3 in [self.values.count(i) for i in set(self.values)]
    
  def is_two_pairs(self):
    """Two different pairs"""
    return [self.values.count(i) for i in set(self.values)].count(2) == 2
    
  def is_one_pair(self):
    """Two cards of the same value"""
    return 2 in [self.values.count(i) for i in set(self.values)]
    
#  def __cmp__(self):
#    """returns -1, if a < b
#                0 if a == b
#                1 if a > b
#    """
#    if not self.is_royal_flush() and other.is_royal_flush():
#      return -1
#    elif self.is_royal_flush() and not other.is_royal_flush():
#      return 1
#    else:
    
    
  

 
 
if __name__ == "__main__":
  a = Hand('JC TC AC KC QC')
  b = Hand('AD KD QD JD TD')
  assert a.is_royal_flush()
  assert b.is_royal_flush()
  
  c = Hand('JC TC 9C KC QC')
  d = Hand('QS JS TS 9S 8S')
  assert c.is_straight_flush()
  assert d.is_straight_flush()
  
  e = Hand('9C 9C 9D 9H JH')
  f = Hand('7C 7S 7D 7H JH')
  assert e.is_four_of_a_kind()
  assert f.is_four_of_a_kind()
  
  g = Hand('7S 7H 7D 4S 4C')
  h = Hand('3C 3S 3D 6C 6H')
  assert g.is_full_house()
  assert h.is_full_house()
  
  i = Hand('QC TC 7C 6C 4C')
  j = Hand('QD 9D 7D 4D 3D')
  assert i.is_flush()
  assert j.is_flush()
  
  k = Hand('QC JS TS 9H 8H')
  l = Hand('TC 9D 8H 7C 6S')
  assert k.is_straight()
  assert l.is_straight()
  
  m = Hand('2D 2S 2C KS 6H')
  n = Hand('QS QH QD 7S 4C')
  assert m.is_three_of_a_kind()
  assert n.is_three_of_a_kind()
  
  o = Hand('JH JC 4C 4S 9H')
  p = Hand('8H 8C 4S 4C TS')
  assert o.is_two_pairs()
  assert p.is_two_pairs()
  
  q = Hand('4H 4S KS TD 5S')
  r = Hand('9H 9C AH QD TD')
  assert q.is_one_pair()
  assert r.is_one_pair()
  
  
  
  
  


