import random
Rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
Paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
Sissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_hands = [Rock,Paper,Sissors]
CPU_Choise = random.choice(game_hands)
Player_Choise = input("Choose Rock Paper Or Sissors: ")
if Player_Choise == "Rock" or Player_Choise == "rock":
    print(f"You Choose {Rock}")
    if CPU_Choise == Sissors:
        print(f"Computer Choose\n{CPU_Choise}")
        print("You Win")
    elif CPU_Choise == Paper:
        print(f"Computer Choose\n{CPU_Choise}")
        print("You Loose")
    elif CPU_Choise == Rock:
        print(f"Computer Choose\n{CPU_Choise}")
        print("Its a tie")

elif Player_Choise == "Paper" or Player_Choise == "paper":
    print(f"You Choose {Paper}")
    if CPU_Choise == Sissors:
        print(f"Computer Choose\n{CPU_Choise}")
        print("You Loose")
    elif CPU_Choise == Paper:
        print(f"Computer Choose\n{CPU_Choise}")
        print("Its a tie")
    elif CPU_Choise == Rock:
        print(f"Computer Choose\n{CPU_Choise}")
        print("You Win")

elif Player_Choise == "Sissors" or Player_Choise == "sissors":
    print(f"You Choose {Sissors}")
    if CPU_Choise == Sissors:
        print(f"Computer Choose\n{CPU_Choise}")
        print("Its a tie")
    elif CPU_Choise == Paper:
        print(f"Computer Choose\n{CPU_Choise}")
        print("You Loose")
    elif CPU_Choise == Rock:
        print(f"Computer Choose\n{CPU_Choise}")
        print("You Win")
else:
    print("Invalid entry")