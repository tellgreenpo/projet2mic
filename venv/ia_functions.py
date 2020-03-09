import random

class  Ai:
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

    