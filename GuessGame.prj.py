import random

low=int(input("entre lower bound :\n"))
hight=int(input("enter hight bound:\n"))
choicePc=random.randint(low,hight)
x=5
geussnumber=0
while geussnumber < x:
    geuss=int(input(f"entre your geuss between {low} and {hight}: \n"))
    if geuss>choicePc:
        print("your geuss is bigger than our number!")
    elif geuss<choicePc:
        print("your geuss is smaller than our number!")
    else:
        print("yooohoooo you're win Congratulations!!!")
        break
    geussnumber+=1
if geussnumber==x:
    print(f"sorry you're loser! the correct number was {choicePc}") 
    