# To write a Python program to create a password, declare a string of numbers + uppercase + lowercase + special characters. Take a random sample of the string of a length given by the user:

import random
passlen = int(input("enter the length of password"))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(s,passlen ))
print(p)
