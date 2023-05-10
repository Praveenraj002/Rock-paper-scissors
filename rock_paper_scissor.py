import random

options = ["rock", "paper", "scissor"]

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer):
  print(f"you chose {player}, computer chose {computer}")
  if player == computer:
    print("It's tie..")
  elif player == "rock":
    if computer == "paper":
      print("computer wins, You lose")
    if computer == "scissors":
      print("you win!")
  elif player == "paper":
    if computer == "scissors":
      print("computer wins, You lose")
    if computer == "rock":
      print("you win!")
  elif player == "scissors":
    if computer == "rock":
      print("computer wins, You lose")
    if computer == "paper":
      print("you win!")

choices = get_choices()

result = check_win(choices["player"], choices["computer"])
print(result)