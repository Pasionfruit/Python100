print("Welcome to Treasure Island.\nYour mission is to find the treasure.\nYou're at a cross road. Where do you want to go? Type \"left\" or \"right\"")
direction = input().lower()
if direction == "left":
    print("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.")
    lake = input().lower()
    if lake == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?")
        door = input().lower()
        if door == "yellow":
            print("You found the treasure! You win!")
        elif door == "red":
            print("It's a room full of fire. Game Over.")
        elif door == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
    