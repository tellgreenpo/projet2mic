import random

class  Ai:
    # Create AI database, each key represent the number of sticks left in the game
    AI_memory = {
        "1": {"sticks_left": 1, "A": 1, "B": 1, "C": 1},
        "2": {"sticks_left": 2, "A": 1, "B": 1, "C": 1},
        "3": {"sticks_left": 3, "A": 1, "B": 1, "C": 1},
        "4": {"sticks_left": 4, "A": 1, "B": 1, "C": 1},
        "5": {"sticks_left": 5, "A": 1, "B": 1, "C": 1},
        "6": {"sticks_left": 6, "A": 1, "B": 1, "C": 1},
        "7": {"sticks_left": 7, "A": 1, "B": 1, "C": 1},
        "8": {"sticks_left": 8, "A": 1, "B": 1, "C": 1},
        "9": {"sticks_left": 9, "A": 1, "B": 1, "C": 1},
        "10": {"sticks_left": 10, "A": 1, "B": 1, "C": 1},
    }


    def createdatabase(self):
        f= open("memoryai.txt", "w")
        f.write(str(AI_memory))
        f.close()


    def __init__(self, sticks):
        self.sticks = sticks

    # returns current state of the AI
    def extract_data(self):
        # extract stored data from a txt file
        f= open("memoryai.txt", "r")
        memory = f.read()
        # Return state by the number of sticks
        current = memory.get(str(self.sticks))
        return current

    # changes the choice to 0 if it is a loss
    def modify_data(self, sticks, memory, win, choice):
        if not win :
            memory["AI" + str(sticks)][str(choice)] = 0

    # return the choice of the AI
    def choice(self, memory, current, sticks):
        # if every choice is a loss, nullifies the path to it
        if current["A"] == 0 and current["B"] == 0 and current["C"] == 0 :
            number = 1
            while sticks-number >= 0 and number <= 3 :
                Ai.modify_data(Ai, sticks - number, memory, False, number)
                number = number + 1
            #chooses a random number for move according to "weights"
            move = random.randint(1, 3)
        elif current["A"] == 0 and current["B"] == 0 :
            move = 3
        elif current["A"] == 0 and current["C"] == 0 :
            move = 2
        elif current["B"] == 0 and current["C"] == 0 :
            move = 1
        elif current["A"] == 0 :
            move = random.choice([2,3])
        elif current["B"] == 0 :
            move = random.choice([1,3])
        elif current["C"] == 0 :
            move = random.choice([1,2])
        else:
            move = random.randint(1,3)
        return move

