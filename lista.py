# Simple Blackjack Game in Python
# This code defines a simple command-line Blackjack game where the player can play against a dealer. The player starts with a balance of $100 and can place bets on each round. The game continues until the player runs out of money or chooses to stop playing.
# The game includes classes for Card, Deck, Hand, and BlackjackGame to manage the game logic and flow. The player can choose to hit or stand during their turn, and the dealer will play according to standard Blackjack rules. The game also handles reshuffling the deck when it runs low on cards.

import random

class Card:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def get_value(self):
        if self.rank == 'Ace':
            return 11
        elif self.rank in ['Jack', 'Queen', 'King']:
            return 10
        else:
            return int(self.rank)


class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()
        self.shuffle()
    
    def create_deck(self):
        for suit in Card.suits:
            for rank in Card.ranks:
                self.cards.append(Card(suit, rank))
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        return self.cards.pop()


class Hand:
    def __init__(self):
        self.cards = []
    
    def add_card(self, card):
        self.cards.append(card)
    
    def get_value(self):
        value = 0
        aces = 0
        
        for card in self.cards:
            if card.rank == 'Ace':
                aces += 1
                value += 11
            else:
                value += card.get_value()
        
        while value > 21 and aces > 0:
            value -= 10
            aces -= 1
        
        return value
    
    def __str__(self):
        return ', '.join([str(card) for card in self.cards])


class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.player_balance = 100
        self.current_bet = 0
    
    def play_round(self):
        # Reset hands for new round
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        
        # Get bet
        while True:
            try:
                bet = int(input(f"\nYour balance: ${self.player_balance}\nEnter bet amount: $"))
                if bet <= 0:
                    print("Bet must be positive!")
                    continue
                if bet > self.player_balance:
                    print("Insufficient funds!")
                    continue
                self.current_bet = bet
                break
            except ValueError:
                print("Enter a valid number!")
        
        # Deal initial cards
        for _ in range(2):
            self.player_hand.add_card(self.deck.deal())
            self.dealer_hand.add_card(self.deck.deal())
        
        print(f"\n--- Blackjack Game ---")
        print(f"Your hand: {self.player_hand} (Value: {self.player_hand.get_value()})")
        print(f"Dealer's hand: {self.dealer_hand.cards[0]}, [hidden card]")
        
        # Check for player blackjack
        if self.player_hand.get_value() == 21:
            print("\nBLACKJACK! You win!")
            self.player_balance += self.current_bet * 1.5
            return
        
        # Player's turn
        while True:
            choice = input("\nHit or Stand? (H/S): ").upper()
            if choice == 'H':
                self.player_hand.add_card(self.deck.deal())
                print(f"Your hand: {self.player_hand} (Value: {self.player_hand.get_value()})")
                
                if self.player_hand.get_value() > 21:
                    print("BUST! You lose!")
                    self.player_balance -= self.current_bet
                    return
            elif choice == 'S':
                break
            else:
                print("Invalid input! Enter H or S.")
        
        # Dealer's turn
        print(f"\nDealer's hand: {self.dealer_hand} (Value: {self.dealer_hand.get_value()})")
        
        while self.dealer_hand.get_value() < 17:
            print("Dealer hits...")
            self.dealer_hand.add_card(self.deck.deal())
            print(f"Dealer's hand: {self.dealer_hand} (Value: {self.dealer_hand.get_value()})")
        
        # Determine winner
        player_value = self.player_hand.get_value()
        dealer_value = self.dealer_hand.get_value()
        
        if dealer_value > 21:
            print("\nDealer busts! You win!")
            self.player_balance += self.current_bet
        elif player_value > dealer_value:
            print("\nYou win!")
            self.player_balance += self.current_bet
        elif player_value < dealer_value:
            print("\nDealer wins!")
            self.player_balance -= self.current_bet
        else:
            print("\nPush (Tie)!")
        
        # Reshuffle if deck is running low
        if len(self.deck.cards) < 20:
            print("\nReshuffling deck...")
            self.deck = Deck()
    
    def run(self):
        print("=== Welcome to Blackjack ===")
        
        while self.player_balance > 0:
            self.play_round()
            
            if self.player_balance <= 0:
                print("\nGame Over! You're out of money!")
                break
            
            play_again = input("\nPlay another round? (Y/N): ").upper()
            if play_again != 'Y':
                break
        
        print(f"\nGame Over! Final balance: ${self.player_balance}")


if __name__ == "__main__":
    game = BlackjackGame()
    game.run()
