import random
def chk_ans(Guess,random_no):
    if Guess>random_no:
        print("Too High")
    elif Guess<random_no:
        print("Too Low")
    else:
        print("Correct Guess")

def set_Difficulty():
    choice = input("Choose A Difficulty Easy OR Hard: ").lower()
    if choice == 'easy':
        return 10
    else:
        return 5
    
def game():
    print("Welcome to The NO Guessing Game")
    random_no = random.randint(1,100)
    turns = set_Difficulty()
    Guess = 0
    print(f"Im thinking of a no between 1-100->{random_no}")
    while turns !=0 and Guess != random_no:
        print(f"You Have {turns} Turns")
        Guess = int(input("Enter A Guess No: "))
        chk_ans(Guess,random_no)
        turns -=1
    if turns == 0:
        print(f"You Loose turns={turns}")
    elif Guess == random_no:
        print("You Win")
game()



