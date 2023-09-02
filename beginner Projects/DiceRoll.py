import random

min_val = 1
max_val = 6

roll_again = "yes"

while roll_again.lower() == "yes" or roll_again.lower() == "y":
    print("Rolling The Dices...")
    computer_roll = random.randint(min_val, max_val)
    print("The Computer's Roll: ", computer_roll)
    
    # Ask the human player to input their choice of dice number
    human_roll = input("Your Turn! Enter a number from 1 to 6: ")
    
    # Check if the input is a valid number from 1 to 6
    if human_roll.isdigit() and min_val <= int(human_roll) <= max_val:
        human_roll = int(human_roll)
        print("Your Roll: ", human_roll)
        
        # Compare the computer's roll and the human's roll
        if computer_roll > human_roll:
            print("Computer wins!")
        elif computer_roll < human_roll:
            print("You win!")
        else:
            print("It's a tie!")
    else:
        print("Invalid input. Please enter a number between 1 and 6.")
    
    roll_again = input("Roll the Dices Again? (yes/no): ")
