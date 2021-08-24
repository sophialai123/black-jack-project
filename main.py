import random
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculator_score(cards):
  #if 11 cards and 10 in cards and len(cards)== 2:
  if sum(cards)== 21 and len(cards)== 2:
    return 0

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"

  elif user_score == computer_score:
    return "It is a draw ."
  elif computer_score == 0:
    return "Lose, opponent has Blackjack"
  elif user_score == 0:
    return "You win with a Blackjack"
  elif user_score > 21:
    return "You went over. you lose."
  elif computer_score > 21:
    return "Opponent went over. you lose."
  elif computer_score < user_score:
    return "You win."
  else:
    return "You lose."

user_cards = [ ]
computer_cards = []
is_game_over = False
for _ in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())

while not is_game_over:
  user_score = calculator_score(user_cards)
  computer_score = calculator_score(computer_cards)

  print(f"Your cards are {user_cards}, and current score is : {user_score}")
  print(f"Computer's first card is {computer_cards[0]}")
  if user_score == 0 and computer_score == 0 and user_score > 21:
    is_game_over = True
  else:
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card == 'y':
        user_cards.append(deal_card())
    else:
      is_game_over = True

while computer_score != 0 and computer_score < 17:
  computer_cards.append(deal_card())
  computer_score = calculator_score(computer_cards)

print(compare(user_score,computer_score))







