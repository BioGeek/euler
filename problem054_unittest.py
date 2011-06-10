import unittest
from problem054 import *


class PokerHandsTestCase(unittest.TestCase):
    
    def testIsRoyalFlush(self):
        """Test case Royal Flush: Ten, Jack, Queen, King, Ace, in same suit."""
        p = PokerHand("Andrei",[Card('C','10'), Card('C','J'), Card('C','Q'), Card('C','K'),Card('C','A')])
        assert p.isRoyalFlush() == True, "isRoyalFlush should have Ten, Jack, Queen, King, Ace in same suit."""
        q =  PokerHand("Andrei",[Card('H','Q'), Card('H','K'),Card('H','A'), Card('H','10'), Card('H','J')])
        assert q.isRoyalFlush() == True, "isRoyalFlush should have Ten, Jack, Queen, King, Ace in same suit."""
        
    def testIsStraightFlush(self):        
        """Test case Straight Flush: All cards are consecutive values of same suit."""
        p = PokerHand("Andrei",[Card('C','7'), Card('C','8'),Card('C','9'), Card('C','10'), Card('C','J')])
        assert p.isStraightFlush() == True, "isStraightFlush should have all cards of consecutive values and of same suit."""
        
    def testFourOfAKind(self):
        """Test case Four of a Kind: Four cards of the same value."""
        p = PokerHand("Andrei",[Card('C','3'), Card('C','Q'),Card('D','Q'), Card('H','Q'), Card('S','Q')])
        assert p.isFourOfAKind() == True, "isFourOfAKind should have four cards of the same value."""

    def testFullHouse(self):
        """Test case Full House: Three of a kind and a pair."""
        p = PokerHand("Andrei",[Card('H','A'), Card('D','A'),Card('C','A'), Card('H','K'), Card('S','K')])
        assert p.isFullHouse() == True, "isFullHouse should have three of a kind and a pair."""

    def testIsFlush(self):
        """Test case Flush: All cards of the same suit."""
        p = PokerHand("Andrei",[Card('C','2'), Card('C','3'), Card('C','4'), Card('C','5'),Card('C','6')])
        assert p.isFlush() == True, "isFlush should have all cards of the same suit"
        q = PokerHand("Andrei",[Card('H','2'), Card('H','3'), Card('H','4'), Card('H','5'),Card('H','6')])
        assert q.isFlush() == True, "isFlush should have all cards of the same suit"
        
    def testIsStraight(self):
        """Test case Straight: All cards are consecutive values."""
        p = PokerHand("Andrei",[Card('S','5'), Card('D','4'), Card('C','3'), Card('H','2'),Card('H','A')])
        assert p.isStraight() == True, "isStraight should have all cards with consecutive values."
        
    def testIsThreeOfAKind(self):
        """Test case Three of a Kind: Three cards of the same value."""
        
    def testTwoPairs(self):
        """Test case Two Pairs: Two different pairs."""
        
    def testOnePair(self):
        """Test case One Pair: Two cards of the same value."""
        
    def testHighCard(self):
        """Test case High Card: Highest value card."""
    
    
        

    


if __name__ == "__main__":
    unittest.main() # run all tests
