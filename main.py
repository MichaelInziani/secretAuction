from replit import clear

from art import logo
print(logo)

bids = {}
bidding_finished = False


def find_highest_bidder(bidder_record):
    highest_bid = 0
    winner = ""
    for bidder in bidder_record:
        bid_amount = bidder_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid amount of ${highest_bid}.")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid amount?: "))
    bids[name] = price
    should_continue = input("Is there any other bidder? Type 'yes' or 'no': ").lower()
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
