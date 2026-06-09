'''
- Create a function that takes in 3 parameters(firstname, lastname, age) and

returns a dictionary based on those values
'''

firstname = str(input('What is your firstname? '))
lastname = str(input('What is your lastname? '))
age = int(input('How old are you? '))

def dict(firstname, lastname, age):
    user_info = {
        'firstname': firstname,
        'lastname': lastname,
        'age': age
      }
    
    for x, y in user_info.items():
        print(x, y)

    return

dict(firstname, lastname, age)
