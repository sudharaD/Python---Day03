print("Welcome to the love Calculator!")

while True:
    try:
        name1 = input("What is your name? \n")
        name2 = input("What is their name? \n")

        combined_name = name1.lower() + name2.lower()

        first_number = str(combined_name.count("t") + combined_name.count("r") + combined_name.count("u") + combined_name.count("e"))
        second_number = str(combined_name.count("l") + combined_name.count("o") + combined_name.count("v") + combined_name.count("e"))

        str_percentage = first_number + second_number
        int_percentage = int(str_percentage)

        if int_percentage < 10 or int_percentage > 90:
            print(f"Your score is {int_percentage}, you go together like coke and mentos.")
        elif int_percentage <= 40 and int_percentage <= 50:
            print(f"Your score is {int_percentage}, you are alright together.")
        else:
            print(f"Your score is {int_percentage}") 

        break

    except:
        print("Something Wrong!")