
while True:

    try:

        height = float(input("Enter your height in m: "))
        weight = float(input("Enter your weight in kg: "))

        bmi = int(weight / height ** 2)

        if bmi < 18.5:
            message = "underweight"
        elif bmi < 25:
            message = "normal weight"
        elif bmi < 30:
            message = "overweight"
        elif bmi < 35:
            message = "obese"
        else:
            message = "clinically obese"

        bmi = str(bmi)

        print("Your BMI is: " + bmi)

        print(f"And you are {message}")

        break

    except:

        print("Please enter values in Integers")