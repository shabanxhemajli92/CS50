class Card:
    """Represents a standard playing card."""
def __init__(self, suit=0, rank=2):
    self.suit = suit
    self.rank = rank

    # suitnames = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    # rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
    # '8', '9', '10', 'Jack', 'Queen', 'King']
    # def __str__(self):
    #     return '%s of %s' % (Card.rank_names[self.rank],
    # Card.suitnames[self.suit])

card1= Card(2,11) 
print(card1)   