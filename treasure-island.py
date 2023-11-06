# This code prints a decorative ASCII art, welcoming the player to "Treasure Island."
# The player's mission is to find the treasure.

# User input to decide the direction to take at a crossroad.
choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()

# Check the first choice:
if choice1 == "left":
    # If the player chose "left," they are presented with another choice at a lake.
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    
    # Check the second choice:
    if choice2 == "wait":
        # If the player chose to "wait," they are now at an island with three doors.
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose? \n").lower()
        
        # Check the third choice:
        if choice3 == "red":
            # If the player chose the "red" door, they enter a room full of fire, and it's a game over.
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            # If the player chose the "yellow" door, they found the treasure, and they win the game.
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            # If the player chose the "blue" door, they enter a room with beasts, and it's a game over.
            print("You enter a room of beasts. Game Over.")
        else:
            # If the player chose an invalid door, it's a game over.
            print("You chose a door that doesn't exist. Game Over.")
    else:
        # If the player chose to "swim," they get attacked by an angry trout, and it's a game over.
        print("You get attacked by an angry trout. Game Over.")
else:
    # If the player chose "right," they fell into a hole, and it's a game over.
    print("You fell into a hole. Game Over.")
