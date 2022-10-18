'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random
import math
done=False
miles=0
thirst=0
tire=0
NM=-20
drinks=5
print("Welcome to the camel game!")
print("You went the wrong direction in the dessert and got into some trouble with the natives.")
print("Escape the natives alive to win the game.")
while not done:
    if thirst>6:
        print("You died of thirst!")
        print("GAME OVER!")
        done=True
        break
    elif tire>8:
        print("Your camel is dead!")
        print("GAME OVER!")
        done=True
        break
    elif NM>=miles:
        print("The natives have caught you!")
        print("GAME OVER!")
        done=True
        break
    elif miles>=200:
        print()
        print("You made it back alive!!!")
        print("congrats, you won the game!")
        done=True
        break
    else:
        if thirst>4:
            print()
            print("You are thirsty!")
        if tire>5:
            print()
            print("Your camel is getting tired!")
        if NM-miles<15 and NM-miles>-1:
            print()
            print("The natives are getting close!")
    print()
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. stop for the night.")
    print("E. Status Check.")
    print("Q. Quit.")
    print()
    game=(input("What would you like to do? "))
    if game.lower()=="a":
        print()
        if drinks>=0:
            drinks-=1
            thirst=0
        else:
            print()
            print("You have no water left.")
    elif game.lower()=="b":
        print()
        Oas=random.randrange(1,21)
        if Oas==1:
            print("You have found an Oasis!")
            print("Your water, thirst, and camel exhaustion has been restored!")
            thirst=0
            tire=0
            drinks=5
        else:
            mys=random.randrange(5,13)
            print("You move",mys,"miles forward.")
            miles+=mys
            thirst+=1
            tire+=1
            NM+=random.randrange(7,15)
    elif game.lower()=="c":
        print()
        Oas = random.randrange(1, 21)
        if Oas == 1:
            print("You have found an Oasis!")
            print("Your water, thirst, and camel exhaustion has been restored!")
            thirst = 0
            tire = 0
            drinks = 5
        else:
            mys=random.randrange(10,21)
            print("You move",mys,"miles forward.")
            miles+=mys
            thirst+=1
            tire+=random.randrange(1,4)
            NM+=random.randrange(7,15)
    elif game.lower()=="d":
        print()
        print("You stop of the night.")
        print("Your camel is happy.")
        tire=0
        NM+=random.randrange(7,15)
    elif game.lower()=="e":
        print()
        print("Miles traveled:",miles)
        print("Drinks in canteen:",drinks)
        print("The natives are",NM-miles,"miles behind you.")
    else:
        done = True