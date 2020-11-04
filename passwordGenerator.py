import random
import string


alphabet = string.ascii_letters
numbers = string.digits
punctuation = string.punctuation

password = []

password_length = int(input("How long should the password be? Please tell me in numbers. "))
password_characters = string.ascii_letters + string.digits + string.punctuation

password = []

for x in range(password_length):
    password.append(random.choice(password_characters))

print (''.join(password))