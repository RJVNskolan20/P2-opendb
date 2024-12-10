import os

class Card:    #class 
  def __init__(self,suit,value):      #dundermethod/ specialmethod
    self.suit = suit
    self.value = value
                            
    #vanlig meotd i en klass
  def show(self):
    return f"{self.suit} {self.value}"
  

  def __str__(self):                              #dundermethod  (double underscore __)
    return f"{self.suit}" "{self.value}"
  
  def __repr__(self):
    return f"{self.suit}" "{self.value}"
      
class Deck: 
  def __init__(self, cards=None):
    if cards is None:
        cards = []

    self.cards = cards

  def __str__(self):
    return f"{self.cards}"

  @staticmethod
  def make_deck():
    cards = []
    suits = ["♠", "♥", "♣", "♦"]
    values = ["A" , 2, 3, 4, 6, 7, 8, 9, 10, "J", "Q", "K" ]

    for suit in suits: 
      for value in values: 
        cards.append(Card(suit, value))

          
    return cards 
      
#skapa ett kort 

os.system ("cls")

cards = Deck.make_deck()

deck = Deck(cards)

print(deck)