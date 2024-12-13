import time
import random
rand_num = (int)(random.random()*100)
last_input = 0
def typing_text(c):
    for c in c:
        print(c, end="", flush=True)
        time.sleep(.05)
def typing_text_long(c):
    for c in c:
        print(c, end="", flush=True)
        time.sleep(.2)        
typing_text("Lets play a game... \n\nGuess the number between 1 and 100...\nI'll give you ten tries...\nIf you fail, you...\n")
typing_text_long("DIE.\n")
typing_text("NOW GUESS.\n")
for j in range(10):  
    typing_text(f"Try {j+1}\n")
    typing_text("Guess:")
    num_in=int(input())
    if(num_in==last_input and j>0):
        typing_text("Dumbass\n")
    if(j==8):
        typing_text_long("LAST GUESS.\n")
    if(num_in<1 or num_in>100 and j!=9):
        typing_text(f"Come on man! I said between 1 and 100\n")
    elif(num_in>rand_num and j!=9 and last_input!=num_in):
        typing_text(f"Lower...\n")
    elif(num_in<rand_num and j!=9 and last_input!=num_in):
        typing_text(f"Higher...\n")
    elif(num_in==rand_num):
        typing_text(f"Correct...\nYou beat me...\nI'll let you live this time...")
        break
    elif(num_in != rand_num and j == 9):
        typing_text_long("UNFORTUANATE.\nNOW YOU DIE...\n")
        typing_text("(you get stabbed and die)")
    last_input=num_in

