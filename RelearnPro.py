import random
import time  # To put a delay time and make the game smoother and to avoid the user to find out the winning solution


# Bot's Turn
def bot_turn():
    time.sleep(1)  # 1 second interval
    global bots_turn
    if box % 11 != 0:  # If the Bot gets a chance to make a total of 11*n, then the bot will win
        box_n = int(box / 11 + 1)
        bots_turn = box_n * 11 - box  # To put a number of pebbles which make the sum as 11*n
    else:  # If the Bot doesnt get a chance to put pebbles which make the box 11*n, then Bot will play random
        bots_turn = random.randint(1, 10)
    print("Bot has put " + str(bots_turn) + " Pebbles")
    return bots_turn


# Users Turn
def user_turn():
    global users_turn
    print("Your Turn!")
    users_turn = int(input("Enter the number pebbles you want to put: "))  # Asking the user to tell the number of pebbles to put in the box
    while users_turn < 1 or users_turn > 10:  # If the user chooses to put less then 1 or more than 10 pebbles then it has to choose again
        print("You can only put 1-10 pebbles at a chance")
        time.sleep(1)  # 1 second interval
        users_turn = int(input("Enter the number pebbles you want to put: "))  # Asking the user again because of wrong choice
    return users_turn


# Printing the Rules
print("""-----100 Pebbles-----\n
1. Player can put 1-10 Pebbles in a box.
2. If the box gets 100 pebbles or more than the last player to put will lose the game! .\n""")

# The main program
while True:  # To keep the running till the user wants
    box = 0  # initializing that the box has 0 pebbles at start
    user_player = int(input("Enter 1 to play First or 2 to play Second: "))  # Asking the user to play 1st or 2nd
    print()
    while box < 100:  # This game will be looping till the box has 3 digit number of pebbles
        if user_player % 2 == 1:
            user_turn()
            box += users_turn  # Adding the pebbles to the box
            time.sleep(1)  # 1 second interval
            print("\nThe box has " + str(box) + " Pebbles\n")
            if box >= 100:
                print("You Lost!!")  # If the user crossed 100 number of pebbles then it will lose the game
        else:
            print("Bot's Turn!")
            bot_turn()
            box += bots_turn  # Adding the pebbles to the box
            time.sleep(1)  # 1 second interval
            print("\nThe box has " + str(box) + " Pebbles\n")
            time.sleep(1)  # 1 second interval
            if box >= 100:
                print("You Won!!")  # If the Bot crossed 100 number of pebbles then the user will win
        user_player += 1
    if input("Enter 'y' to play again") != "y":  # Asking the user to play again or not
        break
