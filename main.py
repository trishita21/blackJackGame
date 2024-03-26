############### Blackjack Project #####################

import random
import art
from replit import clear

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
  num = random.randint(0, len(cards) - 1)
  return cards[ num ]

def calculate_score(card_list):
  if sum(card_list) == 21 and len(card_list) == 2:
    return 0

  sum_val = sum(card_list)
  if sum_val > 21 and 11 in card_list:
    card_list.remove(11)
    card_list.append(1)
  return sum(card_list)

def compare(user_score, comp_score):
  if user_score > 21 and comp_score > 21:
    return "You went over. You lose!!"
  
  if user_score == comp_score:
    return "Draw"
  elif comp_score == 0:
    return "Lose, opponent has Blackjack! "
  elif user_score == 0:
    return "Win with a Blackjack"
  elif user_score > 21:
    return "You went over. You lose!!"
  elif comp_score > 21:
    return "Computer went over. You win!!"
  elif user_score > comp_score:
    return "You win!"
  else:
    return "You lose!!"


def play():
  print(art.logo)
  
  user_cards = []
  computer_cards = []
  gameEnd = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not gameEnd:
  
    user_score = calculate_score(user_cards)
    comp_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or comp_score == 0 or user_score > 21:
      gameEnd = True
    else:
      user_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_deal.lower() == 'y':
        user_cards.append(deal_card())
      else:
        gameEnd = True

  while comp_score != 0 and comp_score < 17:
    computer_cards.append(deal_card())
    comp_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {comp_score}")
  print(compare(user_score, comp_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play()
