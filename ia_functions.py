import random


class Ai:

    def createdatabase(self):
        f = open("memoryai.txt", "w")
        f.write(str(
            {
                1: {1: 1, 2: 1, 3: 1},
                2: {1: 1, 2: 1, 3: 1},
                3: {1: 1, 2: 1, 3: 1},
                4: {1: 1, 2: 1, 3: 1},
                5: {1: 1, 2: 1, 3: 1},
                6: {1: 1, 2: 1, 3: 1},
                7: {1: 1, 2: 1, 3: 1},
                8: {1: 1, 2: 1, 3: 1},
                9: {1: 1, 2: 1, 3: 1},
                10: {1: 1, 2: 1, 3: 1},
            }
        ))
        f.close()

    def __init__(self, sticks):
        self.sticks = 10
        self.playerposition = []
        self.memory = {}

    def extract_memory(self,filename): # peut etre modifier le code pour un parametre de l'object etant la memoire
        f = open(filename, "r")
        # rajout de eval pour etre sur de recuperer ola bonne structure de donnees
        file = eval(f.read())
        f.close()
        return file
    # sinon utiliser ça
    # fp = open(filepath, 'r').read()


    # changes the choice to 0 if it is a loss
    def modify_data(self,choice,sticks, playerposition):
        # Si on perd la partie, on va alors eviter de refaire les memes decisions
        number = 1
        self.memory[sticks][choice] = 0
        # Pour chaque position du joueur adverse annule le chemin a celle ci car il suceptible de gagner
        for num in playerposition:
            while number <= 3 and num+number <= 10:
                self.memory[num+number][number] = 0
                number += 1


    # return the choice of the AI
    def choice(self, memory, sticks):
        current = memory[sticks]
        if current[1] == 0 and current[2] == 0 and current[3] == 0:
            move = random.randint(1, 3)
        elif current[1] == 0 and current[2] == 0:
            move = 3
        elif current[1] == 0 and current[3] == 0:
            move = 2
        elif current[2] == 0 and current[3] == 0:
            move = 1
        elif current[1] == 0:
            move = random.choice([2, 3])
        elif current[2] == 0:
            move = random.choice([1, 3])
        elif current[3] == 0:
            move = random.choice([1, 2])
        else:
            move = random.randint(1, 3)
        return move
