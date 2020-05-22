import random
import ia_functions

#player1 = {
#    "sticks_left": 10
#}

#player2 = {
#    "sticks_left": 10
#}


# The game itself between 2 human players
def game(player1, player2):
    sticks = 10
    while True:
        print("There are " + str(sticks) + " left in the game")
        print("Player1 how manny sticks do you want to take : 1, 2, 3 ?")
        turn1 = int(input())
        sticks = sticks - turn1
        player1["sticks_left"] = sticks
        if sticks <= 0:
            print("Player2 wins")
            break
        else:
            print("There are " + str(sticks) + " left in the game")
            print("Player2 how manny sticks do you want to take : 1, 2, 3 ?")
            turn2 = int(input())
            sticks = sticks - turn2
            player2["sticks_left"] = sticks
        if sticks <= 0:
            print("Player1 wins")
            break

def iaGame(player):
    sticks = 10
    ai = ia_functions.Ai(10)
    ai.memory = ai.extract_memory("training_result.txt")
    while True:
        print("There are " + str(sticks) + " left in the game")
        print("Player1 how manny sticks do you want to take : 1, 2, 3 ?")
        turn1 = int(input())
        ai.playerposition.append(sticks)
        sticks = sticks - turn1
        player["sticks_left"] = sticks
        if sticks <= 0:
            print("ai wins")
            break
        else:
            the_chosen_one = ai.choice(ai.memory,sticks)
            print("The ai is taking "+str(the_chosen_one)+" sticks")
            sticks -= the_chosen_one
            ai.sticks = sticks
            player["sticks_left"] = sticks
            if sticks <= 0:
                print("test")
                ai.modify_data(the_chosen_one, sticks+the_chosen_one, ai.playerposition)
                print("player wins")
                print(ai.memory)
                break

def training(length):
    ai = ia_functions.Ai(10)
    ai.createdatabase("memoryai.txt")
    ai.memory = ai.extract_memory("memoryai.txt")
    for times in range(length):
        sticks = 10
        while True:
            ai.playerposition.append(sticks)
            training_choice = random.choice([1,2,3])
            sticks -= training_choice
            if sticks <= 0:
                ai.playerposition.clear()
                break
            the_chosen_one = ai.choice(ai.memory, sticks)
            sticks -= the_chosen_one
            ai.sticks = sticks
            if sticks <= 0:
                ai.modify_data(the_chosen_one,sticks+the_chosen_one, ai.playerposition)
                ai.playerposition.clear()
                break
    f = open("training_result.txt", "w")
    f.write(str(ai.memory))
    f.close()


player = {'sticks_left' : 10}
training(5000000)
iaGame(player)