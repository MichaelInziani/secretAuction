

from art import logo
print(logo)

bids = {}
continue_bidding = True

def find_the_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ''
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

def clear_screen():
    print("\n" *100 )

while continue_bidding:
    name = input("What is your name? \n ")
    price = float(input("What is your bidding price?\n $"))
    bids[name] = price

    should_continue = input("Are there any more bidders? Type 'yes' to continue or 'no' to exit.\n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_the_highest_bidder(bids)
    elif should_continue == "yes":
        clear_screen()

