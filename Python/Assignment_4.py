'''
- Create a variable grade holding an integer between 0 - 100

- Code if, elif, else statements to print the letter grade of the number grade variable

Grades:

A = 90 - 100

B = 80 - 89

C = 70-79

D = 60 - 69

F = 0 - 59


Example:

if grade = 87 then print('B') 
'''

grade = int(input("What is your grade? "))

if 90 <= grade <= 100:
    print('Your grade is A')

elif 80 <= grade <= 89:
    print('Your grade is B')

elif 70 <= grade <= 79:
    print('Your grade is C')

elif 60 <= grade <= 69:
    print('Your grade is D')

elif 0 <= grade <= 59:
    print('Your grade is F')

else:
    print('Grades must be between 0 and 100')

