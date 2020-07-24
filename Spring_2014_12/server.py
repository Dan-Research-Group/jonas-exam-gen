import random, copy

def generate(data):
    multiplier = random.choice([1,2,3])
    randomWords = ["I", "Love", "BJC"]
    shuffledWords = random.sample(randomWords, k=len(randomWords))
    select3 = random.choices(shuffledWords, k=6)
    data['params']['multiplier'] = str(multiplier)
    data['params']['final'] = str(mystery1(select3, multiplier))
    data['correct_answers']['solution'] = select3

def mystery1(L , multiplier):
    DB = {}
    for word in L:
        if word in DB:
            DB[word] = DB[word] + multiplier
        else:
            DB[word] = 1
    return DB

    # # Sample two random integers between 5 and 10 (inclusive)
    # a = random.randint(5, 10)
    # b = random.randint(5, 10)
    #
    # # Put these two integers into data['params']
    # data['params']['a'] = a
    # data['params']['b'] = b
    #
    # # Compute the sum of these two integers
    # c = a + b
    #
    # # Put the sum into data['correct_answers']
    # data['correct_answers']['c'] = c
