"""
Write a Python program that can do the following:

 You have $50

 You buy an item that is $15, that has a 3% tax

 Using the print()  Print how much money you have left, after purchasing the item.
"""

money = 50
item_price = 15
tax = (3 / 100) * item_price

money_left = money - item_price - tax
print(f"Money left is ${money_left}")
