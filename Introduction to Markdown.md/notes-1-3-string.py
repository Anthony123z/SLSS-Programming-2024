# Methods - String Methods
# Author: Anthony Zhang
# 21 February 2024

# ask the user what the weather is
user_reply = input("what is the weather like?")

# if they answer rainy, say
# bring an umbrella
if user_reply.strip(" !.?,").lower() == "rainy": 
    print("bring an umbrella")

else:
    print("sorry I didn't understand")