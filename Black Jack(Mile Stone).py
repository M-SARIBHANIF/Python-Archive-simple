import random
def Deal_Card():
    """Returns a random card"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(list):
    """Sum() can also be used"""
    total = 0
    for items in list:
        total += items
    if 11 in list and 10 in list and len(list) == 2:
        return 0
    if 11 in list and sum(list)>21:
        list.remove(11)
        list.append(1)

    return total

def compare(user_score,dealer_score):
    if user_score == dealer_score:
        print("DRAW")
    elif dealer_score == 0:
        print("Dealer has Black Jack")
    elif user_score == 0:
        print("User Has Black Jack")
    elif user_score > 21:
        print("You Went Over Board")
    elif dealer_score > 21:
        print("Dealer Went Over Board")
    elif user_score > dealer_score:
        print("User Wins ")
    else:
        print("Dealer Wins ")

user_card = []
dealer_card = []
Game_over = False


"""Deal two cards to each player"""
for _ in range(2):
    user_card.append(Deal_Card())
    dealer_card.append(Deal_Card())
while not Game_over:
    print(f"Your Cards: {user_card},Current Score: {calculate_score(user_card)}")
    print(f"Computers First Card: {dealer_card[0]}")

    if calculate_score(user_card) == 0 or calculate_score(dealer_card) == 0 or calculate_score(user_card) > 21:
        Game_over = True
    else:
        continue_game = input("type 'y' if you want an other card and 'n' if not: ")
        if continue_game == 'y':
            user_card.append(Deal_Card())
        else:
            Game_over = True
while calculate_score(dealer_card) != 0 and calculate_score(dealer_card) < 17:
    dealer_card.append(Deal_Card())
    calculate_score(dealer_card)
compare(calculate_score(user_card),calculate_score(dealer_card))







