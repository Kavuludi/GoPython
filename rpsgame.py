import sys
import random
from enum import Enum

class RPS(Enum):
 ROCK=1
 PAPER=2
 SCISSOR=3

playerchoice = input("Enter...\n 1 for Rock,\n 2 for Paper, or\n 3 for Scissors:\n\n")

player=int(playerchoice)

if player < 1 or player > 3:
    sys.exit(" must enter 1, 2, or 3!")

computerchoice = random.choice("123")

computer=int(computerchoice)

print("")
print("You chose  "  + str(RPS(player)).replace("RPS.", "") + ".")
print("Python chose  "   + str(RPS(computer)).replace("RPS.", "") + ".")
print("")

if player==1 and computer==3:
    print("Congratulations, you won!🎉")
elif player==2 and computer==1:
    print("Congratulations, you won!🎉")
elif player==3 and computer==2:
    print("Congratulations, you won!🎉")
elif player==3 and computer==3:
    print("There was a tie!😆")
else:
    print("You lost!😥")