while True:
    try:
        year = int(input("Which year do you need to check? "))

        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year.")
            else:
                print(f"{year} not a leap year.")
        elif year % 4 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} not a leap year.")
        
        break1989

    except:
        print("Enter valid year")