'''
1 for snake
-1 for water
0 for gun
snake -> water -> gun ->snake
'''
import random


youDict ={"s": 1, "w": -1, "g": 0}
reversedict ={1: "Snake", -1: "Water", 0: "Gun"}

# Get user input 
print("WELCOME TO SNAKE WATER GUN GAME")
youstr = input("Enter your choice (s for snake, w for water, g for gun): ").lower()
while youstr not in youDict:
    youstr= input("Invalid input, Please enter s, w or g: ").lower()


computer= random.choice([0, -1, 1])
you= youDict[youstr]
print(f"You chose : {reversedict[you]}\nComputer chose: {reversedict[computer]}")
   
# Determine Result
if(computer==you):
    print("Its a draw")
elif(computer==-1 and you==1) or (computer==1 and you==0) or (computer==0 and you==-1):
    print("You win! ")
else:
    print("You lose! ")
