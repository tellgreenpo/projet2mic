import random

# Define AI with A B C how many sticks to subtract in game
AI10 = {
    "sticks_left": 10,
    "A": 1,
    "B": 1,
    "C": 1,
}

AI9 = {
    "sticks_left": 9,
    "A": 1,
    "B": 1,
    "C": 1,
}

AI8 = {
    "sticks_left": 8,
    "A": 1,
    "B": 1,
    "C": 1,
}

AI7 = {
    "sticks_left": 7,
    "A": 1,
    "B": 1,
    "C": 1,
}

AI6 = {
    "sticks_left": 6,
    "A": 1,
    "B": 1,
    "C": 1,
}

AI5 = {
    "sticks_left": 5,
    "A": 1,
    "B": 1,
    "C": 1,
}

AI4 = {
    "sticks_left": 4,
    "A": 1,
    "B": 1,
    "C": 1,
}

AI3 = {
    "sticks_left": 3,
    "A": 1,
    "B": 1,
    "C": 1,
}

AI2 = {
    "sticks_left": 2,
    "A": 1,
    "B": 1,
    "C": 1,
}

AI1 = {
    "sticks_left": 1,
    "A": 1,
    "B": 1,
    "C": 1,
}

# Create AI database, each key represent the number of sticks left in the game
AI_memory = {
    "1": AI1,
    "2": AI2,
    "3": AI3,
    "4": AI4,
    "5": AI5,
    "6": AI6,
    "7": AI7,
    "8": AI8,
    "9": AI9,
    "10": AI10,
}


player = {
    "sticks_left": 10
}


# Returns the current state of the AI depending on the number of sticks left
def ai_status(sticks):
    number = 0
    while number < (sticks + 1):
        number += 1
    return AI_memory["AI" + str(number)]


# Returns then number of the sticks the AI is gonna take
def choice(ai_currently):
    stick = ai_currently["sticks_left"]
    if ai_currently["A"] == 0 and ai_currently["B"] == 0:
        return 3
    elif ai_currently["A"] == 0 and ai_currently["C"] == 0:
        return 2
    elif ai_currently["B"] == 0 and ai_currently["C"] == 0:
        return 1
    elif ai_currently["A"] == 0:
        return random.choice[2, 3]
    elif ai_currently["B"] == 0:
        return random.choice[1, 3]
    elif ai_currently["C"] == 0:
        return random.choice[1, 2]
    else:
        return random.choice[1, 2, 3]


# Returns the letter which corresponding to the key of the taken sticks
def letter_choice(chosen_move):
    if chosen_move == 1:
        return "A"
    elif chosen_move == 2:
        return "B"
    elif chosen_move == 3:
        return "C"


# Returns a binary that modifies the weight of the AI choice
def modification_choice(win, ai_mem, ai_currently, move):
    if not win:
        ai_currently[letter_choice(move)] = 0
        ai_mem[str(ai_currently["sticks_left"])] = ai_currently


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


# The game between a human player and AI
def gameai(player1, ai):
    sticks = 10
    # infinite loop until someone wins
    while True:
        print("There are " + str(sticks) + " left in the game")
        print("Player1 how manny sticks do you want to take : 1, 2, 3 ?")
        turn1 = input()
        player1["sticks_left"] -= turn1
        sticks -= turn1
        # updates AI status of the game
        aicurrent = ai_status(sticks)
        # checks for a winner
        if winner_pvp(player1, aicurrent) != 0:
            print("AI wins")
            break
        else:
            turn2 = choice(aicurrent)
            sticks -= turn2
            if sticks <= 0:
                modification_choice(False, AI_memory, aicurrent, turn2)
                print("Player1 wins")
                break

