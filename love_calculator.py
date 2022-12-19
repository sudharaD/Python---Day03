print("Welcome to the love Calculator!")

while True:
    try:
        name1 = input("What is your name? \n")
        name2 = input("What is their name? \n")

        combined_name = name1.lower() + name2.lower()

        first_number = str(combined_name.count("t") + combined_name.count("r") + combined_name.count("u") + combined_name.count("e"))
        second_number = str(combined_name.count("l") + combined_name.count("o") + combined_name.count("v") + combined_name.count("e"))

        love_percentage = int(first_number + second_number)

        if (love_percentage < 10) or (love_percentage > 90):
            print(f"Your score is {love_percentage}, you go together like coke and mentos.")
        elif (love_percentage >= 40) and (love_percentage <= 50):
            print(f"Your score is {love_percentage}, you are alright together.")
        else:
            print(f"Your score is {love_percentage}") 

        break

    except:
        print("Something Wrong!")