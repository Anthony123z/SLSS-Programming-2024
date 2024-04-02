# chatbot
# Anthony Zhang
# March 8, 2024

import random

user_input = input("Hello there, whats your name?")


print(f"It's nice to meet you {user_input}")
user_response = input("How was your day so far?")

good_possible_resp = ["I'm really happy for you!", "Thats really good news", "Thats awsome"]
if user_response == "good":
    chosen_response = random.choice(good_possible_resp)
    print(chosen_response)


elif user_response == "bad":
    print("Aww, I hope your day will get better soon!")

print("goodbye, user!")