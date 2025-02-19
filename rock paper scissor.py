import random
value=int(input("What do you choose? type 0 for rock, 1 for paper and 2 for scissor."))
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
if value==0:
    print(rock)
    print("computer chose:")
    cc=random.randint(0,2)
    if cc==0:
       print(rock)
    elif cc==1:
       print(paper)
    else:
       print(scissors)

elif value==1:
    print(paper)
    print("computer chose:")
    cc=random.randint(0,2)
    if cc==0:
       print(rock)
    elif cc==1:
       print(paper)
    else:
       print(scissors)
else:
    print(scissors)
    print("computer chose:")
    cc=random.randint(0,2)
    if cc==0:
       print(rock)
    elif cc==1:
       print(paper)
    else:
       print(scissors)
if value==cc:
    print("draw")
elif (value==0) and cc==1:
    print("you lose")
elif (value==1) and cc==2:
    print("you lose")
elif (value==2) and cc==0:
    print("you lose")
else:
    print("you won")