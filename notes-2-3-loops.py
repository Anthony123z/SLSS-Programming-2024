# loops and iteration
# author: Anthony Zhang
# April 5 2024

# print "something" 10 times
for _ in range(10):
    print("something")

# print out every item in my grocery list
grocery_list = [
    "dishwasher tabs",
    "aluminum foil",
    "blueberry muffins",
    "bananas",
]

# stop if we reach blueberry muffins
for item in grocery_list:
    print("----")
    print(item)

    if item == "blueberry muffins":
        break

    # count from 0 to 9
    for i in range(1000):
        print(i)
        
        # modulo
        if i / 2 == 0:
            print(f"{i} is an even number")

        # rewrite the above for loop as a while loop
        counter = 0

        while counter < 1000:
            
            print(counter)

            # increment counter by 1
            # counter = counter +1
            counter += 1

