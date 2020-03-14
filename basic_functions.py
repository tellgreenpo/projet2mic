import random
import ia_functions

player = {
    "sticks_left": 10
}


# Returns if a game is finished and print who is the winner between 2 players
def winner_pvp(player1, player2):
    if player1["sticks_left"] <= 0:
        winner = 2
    elif player2["sticks_left"] <= 0:
        winner = 1
    else:
        winner = 0
    return winner


# The game itself between 2 human players
def game(player1, player2):
    sticks = 10
    while True:
        print("There are " + str(sticks) + " left in the game")
        print("Player1 how manny sticks do you want to take : 1, 2, 3 ?")
        turn1 = int(input())
        sticks = sticks - turn1
        player1["sticks_left"] = sticks
        if winner_pvp(player1, player2) != 0:
            print("Player2 wins")
            break
        else:
            print("There are " + str(sticks) + " left in the game")
            print("Player2 how manny sticks do you want to take : 1, 2, 3 ?")
            turn2 = int(input())
            sticks = sticks - turn2
            player2["sticks_left"] = sticks
        if winner_pvp(player1, player2) != 0:
            print("Player1 wins")
            break

