temperature = float(input("What is the temperature in Celcius: "))
is_raining = input("Is it raining, Yes or No[y/N]: ")

if is_raining == "y":
    is_raining = True
elif is_raining == "N":
    is_raining = False
else:
    print("Invalid statement, type y or N")

if 15 <= temperature <= 35:
    if is_raining == False:
        print("The outdoor event is still scheduled")
else:
    print("The outdoor event is cancelled")

