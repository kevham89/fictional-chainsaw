import random

class BlackjackGame:
    def __init__(self):
        self.suits = ['♠', '♥', '♦', '♣']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
        self.deck = []
        self.player_hand = []
        self.dealer_hand = []

    def create_deck(self):
        """Create a shuffled deck of cards."""
        self.deck = [f"{rank}{suit}" for suit in self.suits for rank in self.ranks]
        random.shuffle(self.deck)

    def deal_card(self):
        """Deal a card from the deck."""
        if len(self.deck) < 10:
            self.create_deck()
        return self.deck.pop()

    def calculate_hand_value(self, hand):
        """Calculate the value of a hand, accounting for Aces."""
        value = 0
        ace_count = 0
        
        for card in hand:
            rank = card[:-1]  # Get rank (everything except last character)
            value += self.values[rank]
            if rank == 'A':
                ace_count += 1
        
        # Adjust for Aces if hand is busted
        while value > 21 and ace_count > 0:
            value -= 10
            ace_count -= 1
        
        return value

    def display_hand(self, hand, name, hide_first=False):
        """Display a hand of cards."""
        cards_str = ', '.join(hand)
        if hide_first:
            cards_str = f"[Hidden], {', '.join(hand[1:])}"
        
        value = self.calculate_hand_value(hand)
        print(f"{name}: {cards_str} (Value: {value})")

    def play(self):
        """Main game loop."""
        print("\n" + "="*40)
        print("        WELCOME TO BLACKJACK!")
        print("="*40)
        
        while True:
            # Reset hands
            self.player_hand = []
            self.dealer_hand = []
            self.create_deck()
            
            # Deal initial cards
            self.player_hand = [self.deal_card(), self.deal_card()]
            self.dealer_hand = [self.deal_card(), self.deal_card()]
            
            print("\n--- New Hand ---")
            self.display_hand(self.player_hand, "Your Hand")
            self.display_hand(self.dealer_hand, "Dealer's Hand", hide_first=True)
            
            # Check for blackjack
            player_value = self.calculate_hand_value(self.player_hand)
            dealer_value = self.calculate_hand_value(self.dealer_hand)
            
            if player_value == 21:
                print("\n🎉 BLACKJACK! You win!")
                self.show_dealer_hand()
                if input("\nPlay again? (y/n): ").lower() != 'y':
                    break
                continue
            
            # Player's turn
            while True:
                player_value = self.calculate_hand_value(self.player_hand)
                
                if player_value > 21:
                    print(f"\n💥 BUST! Your hand value is {player_value}. You lose!")
                    break
                
                action = input("\nHit or Stand? (h/s): ").lower()
                if action == 'h':
                    self.player_hand.append(self.deal_card())
                    self.display_hand(self.player_hand, "Your Hand")
                elif action == 's':
                    print("\nYou stand.")
                    break
                else:
                    print("Invalid input. Please enter 'h' or 's'.")
            
            # If player didn't bust, dealer plays
            player_value = self.calculate_hand_value(self.player_hand)
            if player_value <= 21:
                self.show_dealer_hand()
                
                # Dealer must hit on 16 or less
                while self.calculate_hand_value(self.dealer_hand) < 17:
                    print("Dealer hits...")
                    self.dealer_hand.append(self.deal_card())
                    self.display_hand(self.dealer_hand, "Dealer's Hand")
                
                # Determine winner
                dealer_value = self.calculate_hand_value(self.dealer_hand)
                
                if dealer_value > 21:
                    print(f"\n🎉 Dealer busts with {dealer_value}. You win!")
                elif dealer_value > player_value:
                    print(f"\n😔 Dealer wins: {dealer_value} vs {player_value}")
                elif dealer_value < player_value:
                    print(f"\n🎉 You win: {player_value} vs {dealer_value}")
                else:
                    print(f"\n🤝 Push! Both have {player_value}")
            
            # Ask to play again
            if input("\nPlay again? (y/n): ").lower() != 'y':
                break
        
        print("\nThanks for playing! Goodbye! 👋")

    def show_dealer_hand(self):
        """Reveal dealer's full hand."""
        print("\n--- Dealer's Hand ---")
        self.display_hand(self.dealer_hand, "Dealer's Hand")


if __name__ == "__main__":
    game = BlackjackGame()
    game.play()
