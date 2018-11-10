import string, random

def generarPassword():
    base_string = string.ascii_letters + string.digits
    password = ''
    for i in range(0, 8):
        password += random.choice(base_string)
    return password