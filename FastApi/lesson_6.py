# Dictionaries

# Example

user_dictionary = {
    "username" : "gabrielsuoye" ,
    "sex" : "male" ,
    "age" : 22
  }

user_dictionary["Marital Status"] = "Single"
print(user_dictionary)

# Use .pop() to delete individual attributes, .clear() to delete all attributes, del dictionary to delete the dictionary.

for x, y in user_dictionary.items():
    print(x, y)

user_dictionary2 = user_dictionary.copy() # Use copy() so that original dictionary is affected.
user_dictionary2.pop("sex")
print(user_dictionary)
