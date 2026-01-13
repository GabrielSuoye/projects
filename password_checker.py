# Password Checker
def password_checker():
    password = str(input("Enter your password "))

    password_len = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_special = any(not char.isalnum() for char in password)
    has_number = any(char.isdigit() for char in password)

    if password_len >= 12 and has_upper is True and has_lower is True and has_special is True and has_number is True:
        print(f"Very strong password")
    elif 7 < password_len < 12 and has_upper is True and has_lower is True and has_special is True:
        print(f"strong password")
    else:
        print(f"Weak password")

    return
 
password_checker()    
