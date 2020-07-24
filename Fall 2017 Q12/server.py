import random, copy, math
import numpy as np

def generate(data):
    wordBank = ["Oski", "California", "Berkeley", "Moffitt", "Stacks", "Campanile", "Sather", "Sproul", "Boba"]

    randomThree = random.sample(wordBank, 3)
    chooseWord = random.randint(0,2)
    data['params']['List1'] = "\'" + randomThree[0] + "\'"
    data['params']['List2'] = "\'" + randomThree[1] + "\'"
    data['params']['List3'] = "\'" + randomThree[2] + "\'"
    data['params']['one'] = chooseWord
    selectedWord = randomThree[chooseWord]
    randomFirstLetter = random.sample(range(0, len(selectedWord)), 2)
    while ((abs(randomFirstLetter[0]-randomFirstLetter[1]) == 1) or (randomFirstLetter == range(0,len(selectedWord)))):
        randomFirstLetter = random.sample(range(0, len(selectedWord)), 2)

    if (randomFirstLetter[0] > randomFirstLetter[1]):
        randomFirstLetter = [randomFirstLetter[1], randomFirstLetter[0]]
    data['params']['two'] = randomFirstLetter[0]
    data['params']['twofive'] = randomFirstLetter[1]

    solution = randomThree[chooseWord][randomFirstLetter[0]:randomFirstLetter[1]] #answer
    data['correct_answers']['solution'] = "\'" + solution + "\'"
