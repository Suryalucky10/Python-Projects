# TODO-1: Ask the user for input
dict1={}
bid1=True
while bid1:
        name=input("What is your name")
        Bid=int(input("What is your bid : $"))
        any1=input("Are there any other Bidders: ").lower()
        dict1[name]=Bid
        if any1=="yes":
            print("\n"*200)
            bid1=True
        elif any1=="no":
            bid1=False
        else:
            print("Invalid input!")
        print(dict1)
m=max(dict1)
print(f"The Auction winner is {m} with a bid of {dict1[m]}$.")
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


