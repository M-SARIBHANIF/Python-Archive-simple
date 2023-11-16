def max_bid(total_bids):
    amount = 0
    winner = " "
    for items in total_bids:
        if total_bids[items] > amount:
            amount = total_bids[items]
            winner = items
    print(f"The Winner is {winner} with a bid amount of ${amount}")
total_bids = {}
end = False
while end != True:
    name_person = input("what is your name: ")
    bid_amount = int(input("what is your bid: $"))
    total_bids[name_person] = bid_amount
    choice=input("is there an other bidder(yes or no)")
    if choice == "no":
       end = True
       max_bid(total_bids)


