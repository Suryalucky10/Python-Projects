import random
def deal_cards():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
def calculate(cards):
    if sum(cards)==21and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(use_cards,comp_cards):
    if user_score==com_score:
        return"Draw"
    elif user_score==0:
        return"You win with a blackjack"
    elif com_score==0:
        return "You lose, opponet is with a blackjack"
    elif user_score>21:
        return"you lose"
    elif com_score>21:
        return"you win"
    elif user_score>com_score:
        return "you win"
    else:
        return "you lose"
def play_game():
    user_cards=[]
    com_cards=[]
    user_score=-1
    com_score=-1
    game_over=False
    for _ in range(2):
        user_cards.append(deal_cards())
        com_cards.append(deal_cards())
    while not game_over:
        user_score=calculate(user_cards)
        com_score=calculate(com_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {com_cards[0]}")
        if user