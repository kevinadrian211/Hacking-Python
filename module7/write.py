with open ('archivo.txt', 'w') as archivo:
archivo.write('Hola, Mundo!\n')

with open ('archivo.txt', 'a') as archivo:
    archivo.write ('Esta es una nueva línea.\n')