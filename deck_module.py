#creating a module that returns deck of cards
#the function returns a list called deck_of_cards

def create_deck():
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    ranks = ['Ace','2','3','4','5','6','7','8','9','10', 'Jack', 'Queen', 'King']
    deck_of_cards = []

    for suit in suits:
        for rank in ranks:
           deck_of_cards.append(f'{rank} of {suit}')
            
    return deck_of_cards
#cards = create_deck()
#print(cards)
#print(len(cards))