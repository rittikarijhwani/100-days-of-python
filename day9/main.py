# Secret Auction

print("Welcome to the secret auction program.")

# dictionary to store the name-bid pairs
bids = {}
# set condition to break out of the loop
bidding_over = False

while not bidding_over:
    # unclear whether multiple bids by the same person should be allowed
    # and whether it's possible for a subsequent bid by the same person to be LOWER than their previous one
    # so, just check if there's already a bid with that name (keep it case sensitive)
    while True:
        name = input("What's your name? > ").lower()
        # reject an empty input
        if name == "":
            print("Please enter a name.")
        # this should get evaluated as "truthy" (i.e. True) if there is a value assigned to it in the dictionary
        elif bids.get(name):
            print(f"There is already a bid by {name}. Please enter a different name.")
        else:
            break

    # make sure it's a valid amount (no cents, to keep it simple)
    while True:
        bid_str = input("What is your bid? > $")
        if bid_str == "0":
            print("$0 is not a proper bid. Please try again.")
        elif not bid_str.isdigit():
            print("Please enter a valid amount.")
        else:
            bid = int(bid_str)
            break

    # add to the dictionary, already made sure it's a new key
    bids[name] = bid

    choice = input("Are there any other bidders? Type \"yes\" or \"no\". > ").lower()

    # skip checking the input, just keep going until "no" is entered
    if choice == "no":
        bidding_over = True

    print("\n" * 100)

# find the highest bid
winner_name = ""
top_bid = 0
for key in bids:
    # unclear what to do if there are multiple winners (with identical bids), just pick whoever gets processed first
    if bids[key] > top_bid:
        top_bid = bids[key]
        winner_name = key

print(f"The winner is {winner_name} with a bid of ${top_bid}.")
