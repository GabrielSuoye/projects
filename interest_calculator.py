# Compound Interest Calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle cannot be less than or equal to zero")

while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest rate cannot be less than or equal to zero")

while time <= 0:
    time = float(input("Enter how long in years: "))
    if time <= 0:
        print("time cannot be less than or equal to zero")

#simple_interest = principle * time * rate/100
#print(f"The simple interest is {simple_interest}")

Amount = principle * (1 + rate/100)**time
print(f"Your amount after {time}years is ${Amount:.2f}")
