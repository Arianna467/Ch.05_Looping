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
nmVSmiles=20
Med=2
drinks=5
Map=0
Health=100
Gold=75
Vill=False
Camel="Old"
LookCam=False

print("Welcome to the camel game!")
print("You went to go visit a friend who lives in the desert.")
print("However you went the wrong direction on the way back and got into some trouble with the natives.")
print("Escape the natives alive to win the game.")
while not done:
    if thirst>6:
        print()
        print("You died of thirst!")
        print("GAME OVER!")
        done=True
        break
    elif tire>8:
        print()
        print("Your camel is dead!")
        print("GAME OVER!")
        done=True
        break
    elif NM>=miles:
        print()
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
        if nmVSmiles<=15:
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
        Event=random.randrange(1,16)
        if Event==1 or Event==6:
            Health-=random.randrange(1,51)
            print("You got caught in a Sand Storm!")
            print("You couldn't move for the night and got pretty injured.")
            print("Luckily your friend packed you a first aid kit.")
            print("Your health was also reduced to",Health)
            print()
            heal=input("Would you like to use your first aid kit? (y or n)")
            if heal=="y" and Med>=1:
                print("You heal to full health and are back on the road.")
                Health=100
            elif heal=="y" and Med<1:
                print("You do not have anything left in your first aid kit.")
                print("Maybe you'll find a village and refill your med kit.")
            else:
                print("You decide the wound isn't too bad and keep moving.")
        elif Event == 2 or Event == 7:
            if Map >= 1:
                print()
                print("You seem to have gotten lost, lucky you have a map to lead you back on the right path.")
                print(
                    "However, as soon as you got back on track it fell apart, looks like you'll have to get a new one soon.")
                map -= 1
                miles += random.randrange(1, 16)
                print("You travel", miles, "miles.")
                mys = random.randrange(7, 15)
                NM += mys
                nmVSmiles = miles - (NM + mys)
            else:
                print()
                print("You seem to have gotten lost and ended up going in circles.")
                print("You didn't advance any miles.")
                mys = random.randrange(7, 15)
                NM += mys
                nmVSmiles = miles - (NM + mys)
        elif Event==3:
            print("You have found an Oasis!")
            print("Your water, thirst, and camel exhaustion has been restored!")
            thirst=0
            tire=0
            drinks=5
        elif Event==4:
            Vill=True
            while Vill is not done:
                if NM >= miles:
                    print("The natives have caught you!")
                    print("GAME OVER!")
                    done = True
                    break
                elif nmVSmiles<=15:
                        print()
                        print("The natives are getting close!")
                else:
                    print()
                print()
                print("You have found a village! You don't have much time to shop around because the Natives are still hot on your trail.")
                print("You think now would be a good time to restock on supplies.")
                print()
                print("A: Talk to the girl fetching water.")
                print("B: Talk to the Camel Sheppard.")
                print("C: Talk to the Medic.")
                print("D: Talk to the Cartographer.")
                print("E: Check status.")
                print("F: leave village.")
                VilAn=input("What would you like to do? ")
                if VilAn.lower().strip()=="a":
                    print()
                    print("You talk to the girl fetching water.")
                    print("She says she will refill your water for 10 gold.")
                    WatPay=input("Do you pay? (y or n) ")
                    if WatPay.lower().strip()=="y" and Gold>=10:
                        print()
                        print("You pay the girl 10 Gold and she refills your water.")
                        mys = random.randrange(1, 6)
                        NM += mys
                        nmVSmiles = miles - (NM + mys)
                        Gold-=10
                        Drinks=5
                    elif WatPay.lower().strip()=="y":
                        print()
                        print("You reach for your bag of gold and realize you dont have enough enough gold to pay the girl.")
                        print("She refuses to give you any water.")
                    else:
                        print()
                        print("You change your mind on refilling your water.")
                elif VilAn.lower().strip()=="b":
                    print()
                    print("You talk to the Camel Sheppard.")
                    print("He explains to you that he has lost one of his camels.")
                    print("He says if you can find the camel he will give you his fastest camel.")
                    print()
                    CamFin=input("Do you help the Camel Sheppard find his camel?(y or n) ")
                    if CamFin.lower().strip()=="y":
                        LookCam=True
                        Cam = random.randrange(1, 4)
                        while LookCam is not done:
                            if NM >= miles:
                                print("The natives have caught you!")
                                print("GAME OVER!")
                                done = True
                                break
                            elif nmVSmiles <= 15:
                                print()
                                print("The natives are getting close!")
                            else:
                                print()
                                print("You figure you have enough time so you head off to look for the camel.")
                            print()
                            print("A. town square.")
                            print("B: Oasis.")
                            print("C. Sand Hills.")
                            print("D. Give up.")
                            Search=input("Where do you look? ")
                            if Search.lower().strip()=="a" and Cam==1:
                                print()
                                print("You found the Camel!")
                                print("You brought it back to the Camel Sheppard and he gave you his fastest camel.")
                                Camel="New"
                                LookCam=False
                                mys = random.randrange(1, 6)
                                NM += mys
                                nmVSmiles = miles - (NM + mys)
                            elif Search.lower().strip()=="a" and Cam!=1:
                                print()
                                print("The camel was not at Town Square.")
                                mys = random.randrange(1, 6)
                                NM += mys
                                nmVSmiles = miles - (NM + mys)
                            elif Search.lower().strip()=="b" and Cam==2:
                                print()
                                print("You found the Camel!")
                                print("You brought it back to the Camel Sheppard and he gave you his fastest camel.")
                                Camel = "New"
                                LookCam = False
                                mys = random.randrange(1, 6)
                                NM += mys
                                nmVSmiles = miles - (NM + mys)
                            elif Search.lower().strip()=="b" and Cam!=2:
                                print()
                                print("The camel was not at the Oasis.")
                                mys = random.randrange(1, 6)
                                NM += mys
                                nmVSmiles = miles - (NM + mys)
                            elif Search.lower().strip()=="c" and Cam==3:
                                print()
                                print("You found the Camel!")
                                print("You brought it back to the Camel Sheppard and he gave you his fastest camel.")
                                Camel = "New"
                                LookCam = False
                                mys = random.randrange(1, 6)
                                NM += mys
                                nmVSmiles = miles - (NM + mys)
                            elif Search.lower().strip()=="c" and Cam!=3:
                                print()
                                print("The camel was not at the Sand Hills.")
                                mys = random.randrange(1, 6)
                                NM += mys
                                nmVSmiles = miles - (NM + mys)
                            else:
                                print()
                                print("You give up on looking for the camel.")
                                LookCam=False
                elif VilAn.lower().strip()=="c":
                    print()
                    print("You talk to the Medic, she makes a couple offers:")
                    print("A: She will heal you completely for 10 Gold.")
                    print("B: She will refill your med kit for 20 Gold.")
                    print("C: She will heal you and refill your med kit for 30 Gold.")
                    print("D: Decline her offers.")
                    MedAn=input("What would you like to do? ")
                    if MedAn.lower().strip()=="a" and Gold>=10:
                        print()
                        print("She heals you to full health for 10 Gold.")
                        Health=100
                        Gold-=10
                        mys = random.randrange(1, 6)
                        NM += mys
                        nmVSmiles = miles - (NM + mys)
                    elif MedAn.lower().strip()=="a":
                        print()
                        print("You reach for your walet and discover you don't have the money to pay.")
                        print("The medic refuses to offer service to you.")
                    elif MedAn.lower().strip()=="b" and Gold>=20:
                        print()
                        print("She refills your med kit for 20 Gold.")
                        Med=2
                        Gold-=20
                        mys = random.randrange(1, 6)
                        NM += mys
                        nmVSmiles = miles - (NM + mys)
                    elif MedAn.lower().strip()=="b":
                        print()
                        print("You reach for your walet and discover you don't have the money to pay.")
                        print("The medic refuses to offer service to you.")
                    elif MedAn.lower().strip()=="c" and Gold>=30:
                        print()
                        print("She heals you and refills your med kit for 30 Gold.")
                        Med=2
                        Health=100
                        Gold-=30
                        mys = random.randrange(1, 6)
                        NM += mys
                        nmVSmiles = miles - (NM + mys)
                    elif MedAn.lower().strip()=="c":
                        print()
                        print("You reach for your walet and discover you don't have the money to pay.")
                        print("The medic refuses to offer service to you.")
                    else:
                        print()
                        print("You decline the medics offers and head back to the market.")
                elif VilAn.lower().strip()=="d":
                    print()
                    print("You talk to the Cartographer.")
                    print("He says he will give you a map 15 Gold.")
                    MapBuy=input("Do you wish to buy a map? (y or n) ")
                    if MapBuy.lower().strip()=="y" and Gold>=15:
                        print()
                        print("You bought a map for 15 Gold, this could come in handy later on the road.")
                        Map+=1
                        Gold-=15
                    elif MapBuy.lower().strip()=="y":
                        print()
                        print("You reach for your wallet to pay for the map but you realize you don't have enough.")
                        print("The Cartographer refuses to give you a map.")
                    else:
                        print()
                        print("You decline the offer and head back to the market.")
                elif VilAn.lower().strip()=="e":
                    print()
                    print("Miles traveled:", miles)
                    print("Drinks in canteen:", drinks)
                    print("The natives are", nmVSmiles, "miles behind you.")
                    print("Meds in med kit:", Med)
                    print("Your health is:", Health)
                    print("Amount of Gold:", Gold)
                    print("Camel tired level:", tire, )
                    if Camel == "Old":
                        print("Camel speed: Moderate")
                    else:
                        print("Camel speed: High")
                else:
                    print()
                    print("After gathering what you needed you headed off towards your destination.")
                    Vill=False
        elif Event==5 and nmVSmiles>15:
            print()
            FinGold=random.randrange(1,26)
            print("You look down to see something shining in the sand.")
            print("You get off your camel to see what it is.")
            print("You see that its gold.")
            print("Upon searching through the sand you find",FinGold,"Gold!")
            Gold+=FinGold
        else:
            if Camel=="Old":
                print()
                mys1=random.randrange(5,13)
                print("You move",mys1,"miles forward.")
                miles+=mys1
                thirst+=1
                tire+=1
                mys = random.randrange(7, 15)
                NM += mys
                nmVSmiles = miles - (NM + mys)
            else:
                print()
                mys1 = random.randrange(10, 21)
                print("You move", mys1, "miles forward.")
                miles += mys1
                thirst += 1
                tire += 1
                mys = random.randrange(7, 15)
                NM += mys
                nmVSmiles = miles - (NM + mys)
    elif game.lower()=="c":
        print()
        Event=random.randrange(1,16)
        if Event == 1 or Event==6:
            Health-=random.randrange(1,51)
            print("You got caught in a Sand Storm!")
            print("You couldn't move for the night and got pretty injured.")
            print("Your health was reduced to", Health)
            print("Luckily your friend packed you a first aid kit.")
            print()
            heal = input("Would you like to use your first aid kit? (y or n)")
            if heal == "y" and Med >= 1:
                print()
                print("You heal to full health and are back on the road.")
                Health=100
            elif heal == "y" and Med < 1:
                print()
                print("You do not have anything left in your first aid kit.")
                print("Maybe you'll find a village and refill your med kit.")
            else:
                print()
                print("You decide the wound isn't too bad and keep moving.")
        elif Event==2 or Event==7:
            if Map >= 1:
                print()
                print("You seem to have gotten lost, lucky you have a map to lead you back on the right path.")
                print(
                    "However, as soon as you got back on track it fell apart, looks like you'll have to get a new one soon.")
                Map -= 1
                miles += random.randrange(1, 16)
                print("You travel", miles, "miles.")
                mys = random.randrange(7, 15)
                NM += mys
                nmVSmiles = miles - (NM + mys)
            else:
                print()
                print("You seem to have gotten lost and ended up going in circles.")
                print("You didn't advance any miles.")
                mys = random.randrange(7, 15)
                NM += mys
                nmVSmiles = miles - (NM + mys)
        elif Event==3:
            Vill=True
            while Vill is not done:
                if NM >= miles:
                    print("The natives have caught you!")
                    print("GAME OVER!")
                    done = True
                    break
                elif nmVSmiles<=15:
                        print()
                        print("The natives are getting close!")
                else:
                    print()
                print()
                print("You have found a village! You don't have much time to shop around because the Natives are still hot on your trail.")
                print("You think now would be a good time to restock on supplies.")
                print()
                print("A: Talk to the girl fetching water.")
                print("B: Talk to the Camel Sheppard.")
                print("C: Talk to the Medic.")
                print("D: Talk to the Cartographer.")
                print("E: Check status.")
                print("F: leave village.")
                VilAn=input("What would you like to do? ")
                if VilAn.lower().strip()=="a":
                    print()
                    print("You talk to the girl fetching water.")
                    print("She says she will refill your water for 10 gold.")
                    WatPay=input("Do you pay? (y or n) ")
                    if WatPay.lower().strip()=="y" and Gold>=10:
                        print()
                        print("You pay the girl 10 Gold and she refills your water.")
                        mys = random.randrange(1, 6)
                        NM += mys
                        nmVSmiles = miles - (NM + mys)
                        Gold-=10
                        Drinks=5
                    elif WatPay.lower().strip()=="y":
                        print()
                        print("You reach for your bag of gold and realize you dont have enough enough gold to pay the girl.")
                        print("She refuses to give you any water.")
                    else:
                        print()
                        print("You change your mind on refilling your water.")
                elif VilAn.lower().strip()=="b":
                    print()
                    print("You talk to the Camel Sheppard.")
                    print("He explains to you that he has lost one of his camels.")
                    print("He says if you can find the camel he will give you his fastest camel.")
                    print()
                    CamFin=input("Do you help the Camel Sheppard find his camel?(y or n) ")
                    if CamFin.lower().strip()=="y":
                        LookCam=True
                        Cam = random.randrange(1, 4)
                        while LookCam is not done:
                            print()
                            if NM >= miles:
                                print("The natives have caught you!")
                                print("GAME OVER!")
                                done = True
                                break
                            elif nmVSmiles <= 15:
                                print()
                                print("The natives are getting close!")
                            else:
                                print()
                                print("You figure you have enough time so you head off to look for the camel.")
                            print()
                            print("A. town square.")
                            print("B: Oasis.")
                            print("C. Sand Hills.")
                            print("D. Give up.")
                            Search=input("Where do you look? ")
                            if Search.lower().strip()=="a" and Cam==1:
                                print()
                                print("You found the Camel!")
                                print("You brought it back to the Camel Sheppard and he gave you his fastest camel.")
                                Camel="New"
                                LookCam=False
                                mys = random.randrange(1, 6)
                                NM += mys
                                nmVSmiles = miles - (NM + mys)
                            elif Search.lower().strip()=="a" and Cam!=1:
                                print()
                                print("The camel was not at Town Square.")
                                mys = random.randrange(1, 6)
                                NM += mys
                                nmVSmiles = miles - (NM + mys)
                            elif Search.lower().strip()=="b" and Cam==2:
                                print()
                                print("You found the Camel!")
                                print("You brought it back to the Camel Sheppard and he gave you his fastest camel.")
                                Camel = "New"
                                LookCam = False
                                mys = random.randrange(1, 6)
                                NM += mys
                                nmVSmiles = miles - (NM + mys)
                            elif Search.lower().strip()=="b" and Cam!=2:
                                print()
                                print("The camel was not at the Oasis.")
                                mys = random.randrange(1, 6)
                                NM += mys
                                nmVSmiles = miles - (NM + mys)
                            elif Search.lower().strip()=="c" and Cam==3:
                                print()
                                print("You found the Camel!")
                                print("You brought it back to the Camel Sheppard and he gave you his fastest camel.")
                                Camel = "New"
                                LookCam = False
                                mys = random.randrange(1, 6)
                                NM += mys
                                nmVSmiles = miles - (NM + mys)
                            elif Search.lower().strip()=="c" and Cam!=3:
                                print()
                                print("The camel was not at the Sand Hills.")
                                mys = random.randrange(1, 6)
                                NM += mys
                                nmVSmiles = miles - (NM + mys)
                            else:
                                print()
                                print("You give up on looking for the camel.")
                                LookCam=False
                elif VilAn.lower().strip()=="c":
                    print()
                    print("You talk to the Medic, she makes a couple offers:")
                    print("A: She will heal you completely for 10 Gold.")
                    print("B: She will refill your med kit for 20 Gold.")
                    print("C: She will heal you and refill your med kit for 30 Gold.")
                    print("D: Decline her offers.")
                    MedAn=input("What would you like to do? ")
                    if MedAn.lower().strip()=="a" and Gold>=10:
                        print()
                        print("She heals you to full health for 10 Gold.")
                        Health=100
                        Gold-=10
                        mys = random.randrange(1, 6)
                        NM += mys
                        nmVSmiles = miles - (NM + mys)
                    elif MedAn.lower().strip()=="a":
                        print()
                        print("You reach for your wallet and discover you don't have the money to pay.")
                        print("The medic refuses to offer service to you.")
                    elif MedAn.lower().strip()=="b" and Gold>=20:
                        print()
                        print("She refills your med kit for 20 Gold.")
                        Med=2
                        Gold-=20
                        mys = random.randrange(1, 6)
                        NM += mys
                        nmVSmiles = miles - (NM + mys)
                    elif MedAn.lower().strip()=="b":
                        print()
                        print("You reach for your wallet and discover you don't have the money to pay.")
                        print("The medic refuses to offer service to you.")
                    elif MedAn.lower().strip()=="c" and Gold>=30:
                        print()
                        print("She heals you and refills your med kit for 30 Gold.")
                        Med=2
                        Health=100
                        Gold-=30
                        mys = random.randrange(1, 6)
                        NM += mys
                        nmVSmiles = miles - (NM + mys)
                    elif MedAn.lower().strip()=="c":
                        print()
                        print("You reach for your wallet and discover you don't have the money to pay.")
                        print("The medic refuses to offer service to you.")
                    else:
                        print()
                        print("You decline the medics offers and head back to the market.")
                elif VilAn.lower().strip()=="d":
                    print()
                    print("You talk to the Cartographer.")
                    print("He says he will give you a map 15 Gold.")
                    MapBuy=input("Do you wish to buy a map? (y or n) ")
                    if MapBuy.lower().strip()=="y" and Gold>=15:
                        print()
                        print("You bought a map for 15 Gold, this could come in handy later on the road.")
                        Map+=1
                        Gold-=15
                    elif MapBuy.lower().strip()=="y":
                        print()
                        print("You reach for your wallet to pay for the map but you realize you don't have enough.")
                        print("The Cartographer refuses to give you a map.")
                    else:
                        print()
                        print("You decline the offer and head back to the market.")
                elif VilAn.lower().strip()=="e":
                    print()
                    print("Miles traveled:", miles)
                    print("Drinks in canteen:", drinks)
                    print("The natives are", nmVSmiles, "miles behind you.")
                    print("Meds in med kit:", Med)
                    print("Your health is:", Health)
                    print("Amount of Gold:", Gold)
                    print("Camel tired level:", tire, )
                    if Camel == "Old":
                        print("Camel speed: Moderate")
                    else:
                        print("Camel speed: High")
                else:
                    print()
                    print("After gathering what you needed you headed off towards your destination.")
                    Vill=False
        elif Event == 4:
            print("You have found an Oasis!")
            print("Your water, thirst, and camel exhaustion has been restored!")
            thirst = 0
            tire = 0
            drinks = 5
        elif Event==5 and nmVSmiles>15:
            print()
            FinGold=random.randrange(1,26)
            print("You look down to see something shining in the sand.")
            print("You get off your camel to see what it is.")
            print("You see that its gold.")
            print("Upon searching through the sand you find",FinGold,"Gold!")
            Gold+=FinGold
        else:
            if Camel == "Old":
                print()
                mys1 = random.randrange(10, 21)
                print("You move", mys1, "miles forward.")
                miles += mys1
                thirst += 1
                tire += 1
                mys = random.randrange(7, 15)
                NM += mys
                nmVSmiles = miles - (NM + mys)
            else:
                print()
                mys1 = random.randrange(10, 31)
                print("You move", mys1, "miles forward.")
                miles += mys1
                thirst += 1
                tire += 1
                mys = random.randrange(7, 15)
                NM += mys
                nmVSmiles = miles - (NM + mys)
    elif game.lower()=="d":
        print()
        Steal=random.randrange(1,21)
        if Steal==1:
            print()
            Gold1=random.randrange(0,Gold)
            drinks1=random.randrange(0,drinks)
            Med1=random.randrange(0,Med)
            print("While you were sleeping it seems someone went through your things.")
            print("It seems they stole",Gold1,"Gold,",drinks1,"Water, and",Med1,"Medicine.")
            Gold-=Gold1
            drinks-=drinks1
            Med-=Med1
        else:
            print("You stop of the night.")
            print("Your camel is happy.")
            tire=0
        mys=random.randrange(7,15)
        NM+=mys
        nmVSmiles=miles-(NM+mys)
    elif game.lower()=="e":
        print()
        print("Miles traveled:",miles)
        print("Drinks in canteen:",drinks)
        print("The natives are",nmVSmiles,"miles behind you.")
        print("Meds in med kit:",Med)
        print("Your health is:",Health)
        print("Amount of Gold:",Gold)
        print("Camel tired level:",tire,)
        if Camel=="Old":
            print("Camel speed: Moderate")
        else:
            print("Camel speed: High")
    else:
        done = True