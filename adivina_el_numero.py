import random

print("¡Adivina el numero entre 1 y 100!")

tirada = random.randint(1, 100)

while True:
    numero = input()
    if numero.isdigit():
        if int(numero) < tirada:
            print("mas alto")
        elif int(numero) > tirada:
            print("mas bajo")
        else:
            print("correcto")
            tirada = random.randint(1, 100)