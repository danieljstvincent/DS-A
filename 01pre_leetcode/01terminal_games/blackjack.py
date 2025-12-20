"""
Blackjack Game

Try to get as close to 21 as possible without going over!
"""

import random
import os

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def create_deck():
    """Create a standard 52-card deck."""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def get_card_value(card):
    """Get the numeric value of a card."""
    rank = card[0]
    if rank in ['J', 'Q', 'K']:
        return 10
    elif rank == 'A':
        return 11  # Will be handled as 1 if needed
    else:
        return int(rank)

def calculate_hand_value(hand):
    """Calculate the total value of a hand."""
    total = 0
    aces = 0
    
    for card in hand:
        value = get_card_value(card)
        if value == 11:
            aces += 1
        total += value
    
    # Adjust for aces
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    
    return total

def display_hand(hand, is_dealer=False, hide_first=False):
    """Display a hand of cards."""
    if hide_first and is_dealer:
        print("Dealer's hand: [Hidden], ", end="")
        for i, card in enumerate(hand[1:], 1):
            print(f"{card[0]} of {card[1]}", end=", " if i < len(hand) - 1 else "\n")
        print("(Total: ?)")
    else:
        player = "Dealer's" if is_dealer else "Your"
        print(f"{player} hand: ", end="")
        for i, card in enumerate(hand):
            print(f"{card[0]} of {card[1]}", end=", " if i < len(hand) - 1 else "\n")
        total = calculate_hand_value(hand)
        print(f"(Total: {total})")

def deal_card(deck, hand):
    """Deal a card from the deck to a hand."""
    if deck:
        hand.append(deck.pop())

def main():
    """Main game loop."""
    deck = create_deck()
    player_hand = []
    dealer_hand = []
    
    clear_screen()
    print("=" * 50)
    print("🃏 BLACKJACK 🃏")
    print("=" * 50)
    print("\nTry to get as close to 21 as possible without going over!")
    print("Dealer must hit until they reach 17 or higher.\n")
    
    # Initial deal
    deal_card(deck, player_hand)
    deal_card(deck, dealer_hand)
    deal_card(deck, player_hand)
    deal_card(deck, dealer_hand)
    
    # Player's turn
    while True:
        display_hand(player_hand, is_dealer=False)
        display_hand(dealer_hand, is_dealer=True, hide_first=True)
        
        player_value = calculate_hand_value(player_hand)
        
        if player_value == 21:
            print("\n🎉 Blackjack! You win!")
            break
        elif player_value > 21:
            print("\n💥 Bust! You went over 21. Dealer wins.")
            break
        
        choice = input("\nHit or Stand? (h/s): ").lower().strip()
        
        if choice == 'h':
            deal_card(deck, player_hand)
            clear_screen()
        elif choice == 's':
            break
        else:
            print("Please enter 'h' for hit or 's' for stand.")
    
    # Dealer's turn
    if calculate_hand_value(player_hand) <= 21:
        print("\n" + "-" * 50)
        print("Dealer's turn:")
        display_hand(dealer_hand, is_dealer=True)
        
        while calculate_hand_value(dealer_hand) < 17:
            print("Dealer hits...")
            deal_card(deck, dealer_hand)
            display_hand(dealer_hand, is_dealer=True)
        
        dealer_value = calculate_hand_value(dealer_hand)
        player_value = calculate_hand_value(player_hand)
        
        print("\n" + "=" * 50)
        print("FINAL RESULTS:")
        print("=" * 50)
        display_hand(player_hand, is_dealer=False)
        display_hand(dealer_hand, is_dealer=True)
        print()
        
        if dealer_value > 21:
            print("🎉 Dealer busts! You win!")
        elif dealer_value > player_value:
            print("💀 Dealer wins!")
        elif dealer_value < player_value:
            print("🎉 You win!")
        else:
            print("🤝 Push! It's a tie.")
    
    input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()

