# In this file, you have two classes, Card and Deck.

# Both have been set up with some basic methods (constructors, and a couple of dunder methods)

# Deck has two methods which need completing - shuffle and deal.

# With these methods, you should be able to create almost any card game which you can think of!

# We recommend having a go at implementing one of:
# - snap (easiest)
# - blackjack (easy scoring)
# - baccarat (slightly harder scoring)
# - poker (more difficult)

# If you have another card game you want to implement - go for it!

# You can edit/add to/change these classes as you need to.

import random
from enum import Enum

class Card:
    """
    Class to represent a single playing card.
    """

    VALUES = {
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
        "Six": 6,
        "Seven": 7,
        "Eight": 8,
        "Nine": 9,
        "Ten": 10,
        "Jack": 10,
        "Queen": 10,
        "King": 10,
        "Ace": 1
    }

    def __init__(self, rank, suit):
        """
        Creates a playing card with the given rank & suit.
        """
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def value(self, hand_is_high : bool):
        if self.rank == "Ace":
            return 1 if hand_is_high else 11
        
        return self.VALUES[self.rank]

class Deck:
    """
    Class to represent a deck of playing cards.
    """

    SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

    RANKS = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]

    def __init__(self):
        """
        Creates a full deck of cards.
        """
        self.deck = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.deck.append(Card(rank, suit))

    def shuffle(self):
        """Shuffles this deck randomly."""
        random.shuffle(self.deck)

    def deal(self):
        """Removes top card from this deck and returns it."""
        return self.deck.pop()

    def __len__(self):
        return len(self.deck)

    def __str__(self):
        return "\n".join(str(c) for c in self.deck)

class Hand:
    def __init__(self, owner : str):
        self.owner = owner
        self.hand = []

    def value(self):
        """
        compute total value of hand
        """
        sum = 0
        for card in self.hand:
            sum += card.value(sum > 10)

        return sum

    def add_card(self, card : Card):
        self.hand.append(card)

    def __len__(self):
        return len(self.hand)

    def __getitem__(self, key):
        return self.hand[key]

    def is_bust(self):
        return self.value() > 21
    
    def is_21(self):
        return self.value() == 21

def deal(hand : Hand, deck : Deck) -> bool:
    """
    draw card from deck and append to hand
    prints card dealt + hand value
    
    returns if game should end
    """
    hand.add_card(deck.deal())
    new_value = hand.value()

    print(f"{hand.owner} Dealt {str(hand[-1])}, new value: {new_value}")
    if new_value == 21:
        print(f"{hand.owner} {"blackjack" if len(hand) == 2 else "21"}!")
        return True
    if new_value > 21:
        print(f"{hand.owner} bust!")
        return True
    
    return False

def get_winner(a : Hand, b : Hand) -> str:
    """
    returns which hand is winning
    """
    if a.is_21() or b.is_bust():
        return a
    if b.is_21() or a.is_bust():
        return b
    
    return None

def game_loop() -> Hand:
    """
    game loop
    returns winning hand
    """

    deck = Deck()
    deck.shuffle()

    player = Hand("Player")
    dealer = Hand("Dealer")

    for i in range(2):
        if deal(player, deck):
            return get_winner(player, dealer)
        if deal(dealer, deck):
            return get_winner(player, dealer)

    while True:
        print(f"Player Hand: {player.value()}, Dealer Hand: {dealer.value()}")

        player_input = input(f"Player Choise (hit/stand): ")

        if "hit" in player_input.strip().lower():
            if deal(player, deck):
                return get_winner(player, dealer)

        if dealer.value() < 17:
            if deal(dealer, deck):
                return get_winner(player, dealer)
        else:
            if "stand" in player_input.strip().lower():
                return None
    
# Implement a card game!
def main():
    """
    main app loop
    """
    player_score = 0
    dealer_score = 0

    while True:
        print("############################")
        print(f"PLAYER: {player_score}, DEALER: {dealer_score}")
        print("############################")

        winning_hand = game_loop()

        if winning_hand != None:
            if winning_hand.owner == "Player":
                print(f"PLAYER WON WITH {winning_hand.value()}!")
                player_score += 1
            else:
                print(f"DEALER WON WITH {winning_hand.value()}!")
                dealer_score += 1
        else:
            print("DRAW!")
if __name__ == "__main__":
    main()