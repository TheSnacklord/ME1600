#Imports the random class
import random
#generates the random int betwen 1-100
rand_num = random.randint(1, 100)  
#Just and introduction and explanation
print("Lets play a game\nGuess the number between 1 and 100.\nI'll give you ten tries.\n")
#Interates through 0-9 counting the number of trys, while testin gif it is in the bounds and whether it is above or below
for attempt in range(10):  
    #prints what try it is
    print(f"Try {attempt+1}")
    #asks for the guess of the user
    print("Guess:")
    #collects users integer input
    num_in=int(input())
    #conditional checking if the int is withing the bounds 
    if(num_in<1 or num_in>100):
        print(f"Come on man! I said between 1 and 100\n")
    #conditional checking if the number is higher
    elif(num_in>rand_num ):
        print(f"Lower...\n")
    #conditional checking if the number is lower
    elif(num_in<rand_num ):
        print(f"Higher...\n")
    #checking if it is the number (kind of redundant)
    elif(num_in==rand_num):
        print(f"Correct!\nYou Win!")
        break
#statement if you dont get it in the amount of tries
if(num_in != rand_num):
    print(f"Nice Try!\nThe number was {rand_num}")


