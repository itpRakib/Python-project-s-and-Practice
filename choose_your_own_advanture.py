name = input("What is your name? ")
print("Welcome", name, "to the Choose Your Own Adventure game!")

answer = input(
    "You are at a crossroad, do you want to go left or right? ").lower() 


if answer == "left":
    answer = input("You come to a lake. Do you want to swim across or wait for a boat? Type 'swim' or 'wait': ").lower()
    
    if answer == "swim":
        print("You swam across and were eaten by a crocodile. Game Over.")

    elif answer == "walk":
        print("You walked for many miles, ran out of water and lost the game. Game Over.")
    
    else:
        print("Not a valid option. Game Over.")

elif answer == "right":
    answer=input("You come to a mountain. Do you want to climb it or go around it? Type 'climb' or 'around': ").lower()

    if answer == "back":
        print("you go back to the crossroad. Game Over.")

    elif answer == "cross":
        print("You crossed the mountain and found a treasure chest! You Win!")
    
    else:
        print("Not a valid option. Game Over.")

else:
    print("Invalid choice. Please choose 'left' or 'right'.")





