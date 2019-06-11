#Deck of Card B!
from random import shuffle
class Card:
	
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value
	
	def __repr__(self):
		return self.value +" of "+ self.suit

class Deck:

	card_suits = ("Hearts", "Diamonds", "Clubs", "Spades")
	card_values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
	
	def __init__(self):
		self.cards = [Card(suit,value) for suit in self.card_suits for value in self.card_values]  
		
	def __repr__(self):
		return "Deck of " + str(self.count())+ " cards"
	
    def __iter__(self):
        return iter(self.cards)
        
    def count(self):
        return len(self.cards)
    
    def _deal(self, num):
		if self.count() == 0:
			raise ValueError("All cards have been dealt")
			
		actual_count = min(self.count(), num)
		dealt_cards = []
		for i in range(actual_count):
				dealt_cards.append(self.cards.pop())
		return dealt_cards

	def deal_card(self):
		return self._deal(1)[0]

	def deal_hand(self,hand_size):
		return self._deal(hand_size) 
	
	def shuffle_deck(self):
		if self.count() != 52:
			raise ValueError("Only full decks can be shuffled") 
		return shuffle(self.cards)
        
        
d = Deck()

for i in d:
    print(i)