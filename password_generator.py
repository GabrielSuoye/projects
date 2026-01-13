import secrets
import string

def generate_password():
    characters = string.ascii_letters + string.digits
    secure_password = ''.join(secrets.choice(characters) for _ in range(12))

    print(secure_password)
    return

generate_password()

