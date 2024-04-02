# ask if you want fries with your meal
user_reply = input("do you want fries with your meal?")

# if they answers yes, say
# alright I'll add fries to your meal
if user_reply.strip(" !.?,").lower() == "yes": 
    print("alright I'll add fries to your meal")

# if they answers no, say
# alright I won't add fries to your meal
if user_reply.strip(" !.?,").lower() == "no": 
    print("alright I won't add fries to your meal then")

# if they answer with anything else, say you do not understand
else:
    print("sorry I do not understand")
