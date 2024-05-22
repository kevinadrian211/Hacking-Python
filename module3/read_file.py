def imprimir_linea_especifica(numero_linea, contenido_linea):
    with open("estudiantes.txt", "r") as file:
        for i, line in enumerate(file, start=1):
            if i == numero_linea:
                print(f"Línea {i}: {contenido_linea} - {line.strip()}")
                break
        else:
            print("Número de línea no encontrado.")

numero_linea = 4
contenido_linea = "Name"
imprimir_linea_especifica(numero_linea, contenido_linea)
