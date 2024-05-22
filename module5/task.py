def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        print("Tareas pendientes:")
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea}")

def agregar_tarea(tareas, tarea):
    tareas.append(tarea)
    print(f"Tarea '{tarea}' agregada.")

def eliminar_tarea(tareas, indice):
    if indice >= 1 and indice <= len(tareas):
        tarea_eliminada = tareas.pop(indice - 1)
        print(f"Tarea '{tarea_eliminada}' eliminada.")
    else:
        print("Índice de tarea inválido.")

def main():
    # Leer tareas desde el archivo
    try:
        with open("tasks.txt", "r") as file:
            tareas = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tareas = []

    while True:
        print("\n1. Mostrar tareas")
        print("2. Agregar tarea")
        print("3. Eliminar tarea")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            tarea_nueva = input("Ingrese la nueva tarea: ")
            agregar_tarea(tareas, tarea_nueva)
        elif opcion == "3":
            indice_tarea = int(input("Ingrese el índice de la tarea a eliminar: "))
            eliminar_tarea(tareas, indice_tarea)
        elif opcion == "4":
            print("Guardando tareas en el archivo...")
            with open("tasks.txt", "w") as file:
                for tarea in tareas:
                    file.write(tarea + "\n")
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
