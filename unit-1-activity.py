# unit 1 activity
# author: Anthony Zhang
# March 4 2024

def say_hello(name):
    print(f"Hello {name}")


say_hello("User")


def main():
    dollars = dollars_to_float(input("How much was the last meal you paid for in a restaurant? "))
    percent = percent_to_float(input("What percentage did you tip? "))
    tip = dollars * percent
    # Note: This is one way to round a number to two decimal places
    print(f"I left ${round(tip, 2)}")
def dollars_to_float(d: str):
    # Converts string dollars to a decimal float
    #    Returns the result
    return float(d)
def percent_to_float(p):
    # Converts percent to a decimal float
    #    Returns the result
    return float(p) / 100
main()


user_answer = int(input("Anyways I'm curious, how much can you bench press in pounds?"))

if   user_answer < 100:
    print("thats lightweight")
elif user_answer < 200:
    print("thats mid")
elif user_answer < 300:
    print("alright thats not bad")
elif user_answer < 1000:
    print("😱")
else:
    print("liar🫵")


