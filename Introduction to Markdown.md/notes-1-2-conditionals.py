# Conditionals
# Author: Anthony
# 14 Feburary 2024

# Implement the flowchart from the notes

# Create two variables, x and y
x = 10000000
y = -5.2

# If x is greater than y, print that

# if x < y:
#     print("x is less than y ")
# if x > y:
#     print("x is greater than y")
# if x == y:
#     print("x equals to y")

if x < y:
    print("x is less than y ")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
else: 
    print("x is equal to y")

# If x is less than y, print that
    
# Is x is equal, print that

# Ask the user what their favourite fruit is
fave_fruit = input("What's your favourite fruit?")
# Ask the user how old they are
user_age = input("How old are you?")

# If they answer apple or orange
if fave_fruit == "orange" or fave_fruit == "apple": 
    print("Delicious choice!")
    
    # Delicious choices

# If they answer banana and they're 2 years old
if fave_fruit == "banana" and user_age == "2":
    print("Bananas are delicious!")