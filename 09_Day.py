# Blind Auction Simulator

from art import logo
print(logo)

bid_over = True
dict1 = {}
while bid_over:
    name = input("What is your name?: ")
    bid = int(input("What is your bid amount?: "))

    dict1[name] = bid

    new = input("Is there someone else who wants to bid? (Yes or No): ").lower()
    if new == "yes":
        print("\n"*20)
    else:
        bid_over = False
        break

def highest_bidder():
    comparison = 0
    winner = ""
    for bidder in dict1:
        bid_amount = dict1[bidder]
        if bid_amount > comparison:
            comparison = bid_amount
            winner = bidder
    print("Calculating winner...")
    print(f"Highest bidding amount is {comparison}")
    print(f"Winner is {winner}")
highest_bidder()

#------------------------------ art.py ------------------------------#

logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
