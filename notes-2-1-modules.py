# chatbot
# author: Anthony Zhang
# Mar 8, 2024

import random

def coin_flip():
    # return heads or tails or other?
    # heads is any number 0 to 0.49999999
    # tails is any number from 0.5 to 0.9999991
    # other is any number greater than 0.9999991
    roll = random.random()

    if roll < 0.5:
        return "heads"
    elif roll < 0.9999991:
        return "tails"
    else: 
        return "other?"
    
    def main():
        # repeat 100 times
       heads = 0
       tails = 0
       
    def main():
        for _ in range(100):
            if coin_flip() == "heads":
               heads = heads + 1 # isncrement
            elif coin_flip() == "tails":
               tails += 1 # increment
            else:
               other += 1

print()




main()
