#password generator
import string
import random
password=""
up=string.ascii_uppercase
low=string.ascii_lowercase
numbers=string.digits
symbols=string.punctuation
password+=up
password+=low
password+=numbers
password+=symbols
final_pass=""
final_pass=final_pass.join(random.sample(password, 8))
print(final_pass)