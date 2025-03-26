# Random Password Generatori
import random
import string

def generate_password(lenght=10):
    a=string.ascii_letters+string.digits+string.octdigits

    password=''.join(random.choice(a)for _ in range(lenght))
    return password

password_length=int(input("Enter Password Length:"))

print("pass is",generate_password(password_length))