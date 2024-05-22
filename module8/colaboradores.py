def read_collaborators(filename='colaboradores.txt'):
    try: return [line.strip() for line in open(filename)]
    except FileNotFoundError: return []

def show_collaborators(collaborators, amount=5):
    print("Colaboradores:"); [print(c) for c in collaborators[:amount]]

def add_collaborator(collaborators, name, filename='colaboradores.txt'):
    if len(collaborators) >= 15: return print("Límite alcanzado.")
    if name in collaborators: return print(f"{name} ya está en la lista.")
    open(filename, 'a').write(name + '\n'); collaborators.append(name)
    print(f"{name} añadido a la lista."); return collaborators

def main():
    collaborators = read_collaborators()
    while True:
        option = input("\n1. Mostrar colaboradores\n2. Agregar colaborador\n3. Salir\nElige: ")
        if option == '1': show_collaborators(collaborators, int(input("¿Cuántos? (Enter para 5): ") or 5))
        elif option == '2': collaborators = add_collaborator(collaborators, input("Nombre: "))
        elif option == '3': break

if __name__ == "__main__": main()
