import random
digits = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
length = int(input("¿Cuántos digitos quiere que sea su contraseña"))
password = ""
for i in range(length):
    password += random.choice(digits)
print("La contraseña elegida para ti es:", password)
