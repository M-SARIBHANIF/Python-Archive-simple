import random
def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_description}, from {account_country}")
def chk_answer(guess,A_fol,B_fol):
    if A_fol>B_fol:
        return guess == "a"
    else:
        return guess == "b"
logo ="""
.__    .__       .__                     .__                 
|  |__ |__| ____ |  |__     ___________  |  |   ______  _  __
|  |  \|  |/ ___\|  |  \   /  _ \_  __ \ |  |  /  _ \ \/ \/ /
|   Y  \  / /_/  >   Y  \ (  <_> )  | \/ |  |_(  <_> )     / 
|___|  /__\___  /|___|  /  \____/|__|    |____/\____/ \/\_/  
     \/  /_____/      \/                                     
"""
print(logo)
vs_logo = """
\  \/ /  ___/
 \   /\___ \ 
  \_//____  >
          \/ 
"""
score = 0
game_continue = True
data = [
    {'name':'Instagram',
     'follower_count':346,
     'description':'social media platform',
     'country':'United States',
    },
    {
     'name':'Cristiano Ronaldo',
     'follower_count':215,
     'description':'footballer',
     'country':'portugal',
    },
    {
     'name':'Dwayne Johnson',
     'follower_count':181,
     'description':'Actor and professional wrestler',
     'country':'United States',
    }
]
account_b = random.choice(data)
while game_continue:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A: {format_data(account_a)}")
    print(vs_logo)
    print(f"Against B: {format_data(account_b)}")
    guess = input("Who has more followers A or B: ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = chk_answer(guess,a_follower_count,b_follower_count)
    if is_correct:
        score += 1
        print(f"You're Correct,Current Score {score}")
    else:
        print(f"Sorry You're wrong,Final score{score}")
        game_continue = False
