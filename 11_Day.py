# Blackjack Game

from art import logo
import random
import sys

def player_choice(choice_p1):
    if choice_p1 == "hit":
        player_score_list.append(random.choice(cards))
        player_score1 = evaluate_player_score()
        print(f"Player's cards: {player_score_list}; Player score: {player_score1}")
        return player_score1
    elif choice_p1 == "stand":
        player_score1 = evaluate_player_score()
        print(f"Player's final hand: {player_score_list}; Player score: {player_score1}")
        return player_score1
    else:
        print("Choose correct option.")
        choice_p_again = input("Hit or Stand?").lower()
        player_choice(choice_p_again)

def dealer_choice(choice_d1):
    if choice_d1 == "hit":
        dealer_score_list.append(random.choice(cards))
        dealer_score1 = evaluate_dealer_score()
        conclusion = True
        return dealer_score1, conclusion
    else:
        #print("Dealer chose to stand.")
        dealer_score1 = evaluate_dealer_score()
        conclusion = False
        return dealer_score1, conclusion

def dealer_strategy(dealer_score_input1):
    if dealer_score_input1 < 16:
        dealer_decision = "hit"
        return dealer_decision
    else:
        dealer_decision = "stand"
        return dealer_decision

def evaluate_player_score():
    total = sum(player_score_list)
    if 11 in player_score_list and total > 21:
        player_score_list.remove(11)
        player_score_list.append(1)
    total = sum(player_score_list)
    return total

def evaluate_dealer_score():
    total = sum(dealer_score_list)
    if 11 in dealer_score_list and total > 21:
        dealer_score_list.remove(11)
        dealer_score_list.append(1)
    total = sum(dealer_score_list)
    return total

def game_result(player_score_input, dealer_score_input):
    if player_score_input < dealer_score_input:
        print("You lose!")
        play_game_decision = False
        return play_game_decision
    elif dealer_score_input < player_score_input:
        print("You win!")
        play_game_decision = False
        return play_game_decision
    elif player_score_input == dealer_score_input:
        print("Draw.")
        play_game_decision = False
        return play_game_decision
    else:
        play_game_decision = True
        return play_game_decision

def until_response_is_yes():
    game_start = input("Do you want to play a game of blackjack (Yes or No): ").lower()
    if game_start == "yes":
        print(logo)
    elif game_start == "no":
        print("Okay. Hit me up if you want to!")
        until_response_is_yes()
    else:
        print("Beg your pardon?")
        until_response_is_yes()

until_response_is_yes()

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_score_list = []
dealer_score_list = []

player_score_list.extend(random.choices(cards, k=2))
player_score = evaluate_player_score()
print(f"Player's cards: {player_score_list}; Player score: {player_score}")

dealer_score_list.extend(random.choices(cards, k=2))
dealer_score = evaluate_dealer_score()
print(f"Dealer's first card: {dealer_score_list[0]}")

if player_score == 21 and dealer_score == 21:
     print("Draw.")
     sys.exit()
elif player_score == 21:
     print("You win by a Blackjack!")
     sys.exit()
elif dealer_score == 21:
     print("Dealer wins by a Blackjack!")
     sys.exit()
else:
    pass

player_plays = True
while player_plays:
    choice_p = input("Hit or Stand? ").lower()
    player_score = player_choice(choice_p)
    if player_score > 21:
        print("You went over. You lose!")
        sys.exit()
    if choice_p == "stand":
        break

dealer_plays = True
while dealer_plays:
    choice_d = dealer_strategy(dealer_score)
    dealer_score, dealer_plays = dealer_choice(choice_d)

    if dealer_score > 21:
           print(f"Dealer's final hand: {dealer_score_list}; Dealer score: {dealer_score}")
           print("Dealer went over. You win!")
           sys.exit()
    if choice_d == "stand":
           print(f"Dealer's final hand: {dealer_score_list}; Dealer score: {dealer_score}")
           break

play_game = True
while play_game:
    play_game = game_result(player_score, dealer_score)
    if not play_game:
           break

#------------------------------------------------------ art.py------------------------------------------------------#
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""  
