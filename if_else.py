print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))

if height >= 120:
    print("Can ride the rollercoaster")

    age = int(input("How old are you? "))

    if age >= 18:
        print("12$ Ticket")
    else:
        print("7$ Ticket")

else:
    print("Can't ride")


    # == -> equal to
    # != -> not equal to
