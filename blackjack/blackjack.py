from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

def random_cards():
    i = random.randint(0, len(cards) - 1)
    return cards[i]

play = input("\nDo you want to play blackjack? Type 'yes' or 'no': ")

while play.lower() == "yes":
    print(logo)
    player = [random_cards(), random_cards()]
    dealer = [random_cards(), random_cards()]

    print(f"\nYour cards: {player}")
    print(f"Dealer's one card: [{dealer[0]}, ? ]")

    if 10 in player and 11 in player:
        print("\nYou win with 21 🎉")
    elif 10 in dealer and 11 in dealer:
        print(f"\nYou lose! Dealer got 21 with two cards {dealer}!")
    else:
        score_player = sum(player)
        score_dealer = sum(dealer)

        response = input("\nDo you want to draw another card? Type 'yes' or 'no': ")
        
        while response.lower() == "yes" and score_player < 21:
            player.append(random_cards())
            score_player = sum(player)
            if score_player > 21:
                print(f"\nYou lose 🥲! Your cards: {player}")
                break
            elif score_player == 21:
                print(f"You win with 21 🎉! Your cards: {player}")
                break
            print(f"\nYour cards: {player}")
            response = input("\nDo you want to draw another card? Type 'yes' or 'no': ")
        
        while score_dealer < 17 and score_player < 21:
            dealer.append(random_cards())
            score_dealer = sum(dealer)
            if score_dealer > 21:
                print(f"You win 🎉! Dealer's cards are {dealer}")
                break
        
        if score_dealer > score_player and score_dealer < 21:
            print(f"\nYou lose 🥲! Dealer's cards are {dealer}")
        elif score_player > score_dealer and score_player < 21:
            print(f"\nYou win 🎉! Your cards: {player} - Dealer's cards: {dealer}")
        elif score_dealer == score_player :
            print(f"\n  It's a draw! Dealer got {dealer}")

    play = input("\nDo you want to play blackjack again? Type 'yes' or 'no': ")

print("\nBye Bye!")
