# unit 2 activity
# Anthony Zhang
# April 10 2024

# This code performs the function that counts the number of vowels in a word. 

def count_vowels(word):
    """
    Count the number of vowels in a given word.
    """
    vowels = "aeiouAEIOU"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

def main():
    while True:
        word = input("Enter a word (type 'exit' to quit): ")
        if word.lower() == "exit":
            print("Exiting the program.")
            break
        num_vowels = count_vowels(word)
        print(f"The word '{word}' has {num_vowels} vowels.")

if __name__ == "__main__":
    main()


 

 




