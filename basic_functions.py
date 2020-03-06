import random

# Define AI with A B C how many sticks to substract in game

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

AI_current = {}

player = {
    "sticks_left": 10
}


def ai_status(sticks):
    number = 0
    while number < (sticks + 1):
        number += 1
    return AI_memory["AI" + str(number)]


def choice(ai_currently):
    stick = ai_currently["sticks_left"]
    if ai_currently["A"] == 0 and ai_currently["B"] == 0 and ai_currently["C"] == 0:
        ai_currently = ai_status(stick - 1)
        choice(ai_currently)
    elif ai_currently["A"] == 0 and ai_currently["B"] == 0:
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


def letter_choice(choosen_move):
    if choosen_move == 1:
        return "A"
    elif choosen_move == 2:
        return "B"
    elif choosen_move == 3:
        return "C"


def modification_choice(win, ai_mem, ai_currently, move):
    if not win:
        ai_currently[letter_choice(move)] = 0
        ai_mem[str(ai_currently["sticks_left"])] = ai_currently


def winner_pvp(player1, player2):
    if player1["sticks_left"] <= 0:
        print("Game finished")
        print("player2 won")
        return True
    elif player2["sticks_left"] <= 0:
        print("Game finished")
        print("player1 won")
        return True


def game_finished_player_vs_ai(player1, ai_currently):
    if player1["sticks_left"] <= 0:
        print("AI wins")
        print("Game finished")
        return True
    elif ai_currently["sticks_left"] <= 0:
        print("player wins")
        print("Game finished")
        return True
