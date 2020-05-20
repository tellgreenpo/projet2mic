import random
import ia_functions

player1 = {
    "sticks_left": 10
}

player2 = {
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

def winnerVsAi(ai,player):
    if ai.sticks <= 0:
        winner = 2
    elif player["sticks_left"] <= 0:
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

def iaGame(player):
    sticks = 10
    ai = ia_functions.Ai(10)
    ai.createdatabase()
    ai.memory = ai.extract_memory()
    while True:
        print("There are " + str(sticks) + " left in the game")
        print("Player1 how manny sticks do you want to take : 1, 2, 3 ?")
        turn1 = int(input())
        sticks = sticks - turn1
        player["sticks_left"] = sticks
        if winnerVsAi(ai, player) != 0:
            print("ai wins")
            break
        else:
            ai.the_chosen_one = ai.choice(ai.memory,sticks)
            print("The ai is taking "+str(ai.the_chosen_one)+" sticks")
            sticks -= ai.the_chosen_one
            ai.sticks = sticks
            player["sticks_left"] = sticks
            if winnerVsAi(ai,player) != 0:
                ai.modify_data(sticks+ai.the_chosen_one, ai.the_chosen_one)
                print("player wins")
                print(ai.memory)
                break

def training(length):
    ai = ia_functions.Ai(10)
    ai.createdatabase()
    ai.memory = ai.extract_memory()
    for times in range(length):
        sticks = 10
        while True:
            training_choice = random.choice([1,2,3])
            sticks -= training_choice
            if sticks <= 0:
                break
            ai.the_chosen_one = ai.choice(ai.memory, sticks)
            sticks -= ai.the_chosen_one
            ai.sticks = sticks
            if sticks <= 0:
                ai.modify_data(sticks + ai.the_chosen_one, ai.the_chosen_one)
                break
    f = open("training_result.txt", "w")
    f.write(str(ai.memory))
    f.close()