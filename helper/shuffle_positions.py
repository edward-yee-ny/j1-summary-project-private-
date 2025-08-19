import random

def shuffleListPositions(array):
    shuffledPositions = []
    for i in range(len(array)):
        shuffledPositions.append(i)
        
    random.shuffle(shuffledPositions)
    
    return shuffledPositions
   