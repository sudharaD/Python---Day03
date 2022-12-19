print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:
    print("Can ride the rollercoaster")

    age = int(input("How old are you? "))

    if age >= 45 and age <= 55:
        pass
    elif age >= 18:
        bill = 12
    elif age >= 12:
        bill = 7
    else:
        bill = 5

    wants_photo = input("Do you want a photo taken, Y or N. ")

    if wants_photo == "Y":
        bill += 3
    
    print(f"Pay {bill}$")

else:
    print("Can't ride")


    # == -> equal to
    # != -> not equal to
