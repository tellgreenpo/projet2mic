import random


# definition object IA


class Ai:
    # Create AI database, each key represent the number of sticks left in the game
    # AI_memory = {
    # "1": {"sticks_left": 1, "A": 1, "B": 1, "C": 1},
    # "2": {"sticks_left": 2, "A": 1, "B": 1, "C": 1},
    # "3": {"sticks_left": 3, "A": 1, "B": 1, "C": 1},
    # "4": {"sticks_left": 4, "A": 1, "B": 1, "C": 1},
    # "5": {"sticks_left": 5, "A": 1, "B": 1, "C": 1},
    # "6": {"sticks_left": 6, "A": 1, "B": 1, "C": 1},
    # "7": {"sticks_left": 7, "A": 1, "B": 1, "C": 1},
    # "8": {"sticks_left": 8, "A": 1, "B": 1, "C": 1},
    # "9": {"sticks_left": 9, "A": 1, "B": 1, "C": 1},
    # "10": {"sticks_left": 10, "A": 1, "B": 1, "C": 1},
    # }

    def createdatabase(self):
        f = open("memoryai.txt", "w")
        f.write(str(
            {
                1: {"A": 1, "B": 1, "C": 1},
                2: {"A": 1, "B": 1, "C": 1},
                3: {"A": 1, "B": 1, "C": 1},
                4: {"A": 1, "B": 1, "C": 1},
                5: {"A": 1, "B": 1, "C": 1},
                6: {"A": 1, "B": 1, "C": 1},
                7: {"A": 1, "B": 1, "C": 1},
                8: {"A": 1, "B": 1, "C": 1},
                9: {"A": 1, "B": 1, "C": 1},
                10: {"A": 1, "B": 1, "C": 1},
            }
        ))
        f.close()

    def __init__(self, sticks):
        self.sticks = 10
        self.memory = {}

    def extract_memory(self): # peut etre modifier le code pour un parametre de l'object etant la memoire
        f = open("memoryai.txt", "r")
        # rajout de eval pour etre sur de recuperer ola bonne structure de donnees
        file = eval(f.read())
        f.close()
        return file
    # sinon utiliser ça
    # fp = open(filepath, 'r').read()


    # return letters equivalent of number of sticks taken
    def letterchoice(self, choice):
        if choice == 1:
            return "A"
        elif choice == 2:
            return "B"
        elif choice == 3:
            return "C"

    # changes the choice to 0 if it is a loss
    def modify_data(self, sticks, choice):
        self.memory[sticks][self.letterchoice(choice)] = 0

    # return the choice of the AI
    def choice(self, memory, sticks):
        # if every choice is a loss, nullifies the path to it
        current = memory[sticks]
        if current["A"] == 0 and current["B"] == 0 and current["C"] == 0:
            number = 1  # number of sticks variable
            while sticks - number >= 0 and number <= 3:  # limit of sticks is 3
                self.modify_data(sticks + number, self.letterchoice(number))  # sets the corresponding choice to null
                number = number + 1
            # chooses a random number for move according to "weights"
            move = random.randint(1, 3)
        elif current["A"] == 0 and current["B"] == 0:
            move = 3
        elif current["A"] == 0 and current["C"] == 0:
            move = 2
        elif current["B"] == 0 and current["C"] == 0:
            move = 1
        elif current["A"] == 0:
            move = random.choice([2, 3])
        elif current["B"] == 0:
            move = random.choice([1, 3])
        elif current["C"] == 0:
            move = random.choice([1, 2])
        else:
            move = random.randint(1, 3)
        return move
