'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly chooses a 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.(1 for rock, 2 for paper, 3 for scissors and 4 for quit)
I don't want to be asked to quit each time. I will enter a 4 if I want to quit.
Add conditional statements to figure out who wins and keep the records
Each round tell me what the computer chose, what I chose and also if I won, lost or tied.
When the user quits print an end game message and their win/loss/tie record

'''
import random
comp=0
play=0
tie=0
done=False
while not done:
    print()
    print("enter 1 for rock")
    print("enter 2 for paper")
    print("enter 3 for scissors")
    print("enter 4 for quit")
    game = float(input("What would you like to do? "))
    if game == 4:
        done=True
    else:
        com=random.randrange(1,4)
        if game==1:
            if com==1:
                print()
                print("You and the computer both choose rock. It's a tie!")
                tie+=1
            elif com==2:
                print()
                print("You choose Rock. The Computer choose Paper. You lose!")
                comp+=1
            else:
                print()
                print("You choose rock. The Computer choose Scissors. You Win!")
                play+=1
        elif game==2:
            if com==2:
                print()
                print("You and the computer both choose Paper. It's a tie!")
                tie+=1
            elif com==3:
                print()
                print("You choose Paper. The Computer choose Scissors. You lose!")
                comp+=1
            else:
                print()
                print("You choose Paper. The Computer choose Rock. You Win!")
                play+=1
        else:
            if com==3:
                print()
                print("You and the computer both choose Scissors. It's a tie!")
                tie+=1
            elif com==1:
                print()
                print("You choose Scissors. The Computer choose Rock. You lose!")
                comp+=1
            else:
                print()
                print("You choose Scissors. The Computer choose Paper. You Win!")
                play+=1
print()
print("You won: ", play, " times.")
print("The computer won ", comp, " times.")
print("You and the computer tied ", tie, " times.")