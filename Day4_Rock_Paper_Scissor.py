import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n")

picks = [rock, paper, scissors]

print(picks[int(choice)])
computer_choice = random.randint(0, 2)

print(f"Computer chose: {picks[int(computer_choice)]}")

if choice == "0":
    if computer_choice == 0:
        print("It's a draw.")
    elif computer_choice == 1:
        print("You lose.")
    else:
        print("You win.")
elif choice == "1": 
    if computer_choice == 0:
        print("You win.")
    elif computer_choice == 1:
        print("It's a draw.")
    else:
        print("You lose.")
elif choice == "2":
    if computer_choice == 0:
        print("You lose.")
    elif computer_choice == 1:
        print("You win.")
    else:
        print("It's a draw.")
else:   
    print("Invalid input. You lose.")