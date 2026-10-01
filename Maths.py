import random
def Question():
    factor1 = random.randint (1, 100)  
    factor2 = random.randint (1, 100) 
    operator = random.randint (1, 3) 
    if operator == 1:
        Answer = factor1 + factor2
        Guess = input(f"what is {factor1} + {factor2}")
    if operator == 2:
            Answer = factor1 - factor2
    if operator == 3:
            Answer = factor1 * factor2

    Guess = Input(f"what is ")

Question()