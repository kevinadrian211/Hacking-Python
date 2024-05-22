import random

def adivinar_numero():
    numero_secreto = random.randint(1, 10)
    intentos = 0
    
    print("¡Bienvenido al juego de adivinar el número!")
    print("Tienes que adivinar un número entre 1 y 10.")
    
    while True:
        intento = int(input("Introduce tu adivinanza: "))
        intentos += 1
        
        if intento < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("Demasiado alto. Intenta de nuevo.")
        else:
            print(f"¡Felicidades! ¡Has adivinado el número en {intentos} intentos!")
            break

adivinar_numero()
