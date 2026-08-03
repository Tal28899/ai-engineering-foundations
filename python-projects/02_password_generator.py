import string
import random 
passw_values = string.ascii_letters + string.digits +string.punctuation
passw_length = 12
my_passw = ""
for i in range(passw_length):
    my_passw += random.choice(passw_values)
print("My password is :",my_passw)    
