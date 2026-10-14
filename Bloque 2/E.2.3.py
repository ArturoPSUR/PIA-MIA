"""“””E2.3 · Agenda: diccionario de contactos con alta, baja, búsqueda
y listado ordenado, en un bucle de menú."""

def mostrar_menu():
    print("\n--- Agenda de contactos ---")
    print("1. Añadir contacto")
    print("2. Eliminar contacto")
    print("3. Buscar contacto")
    print("4. Listar contactos")
    print("5. Salir")

def gestionar_agenda():
    contactos = {}
    
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ")
        
        if opcion == "1":
            nombre = input("Introduce el nombre del contacto: ")
            telefono = input("Introduce el teléfono: ")
            contactos[nombre] = telefono
            print("Contacto guardado con éxito.")
            
        elif opcion == "2":
            nombre = input("Introduce el nombre del contacto a eliminar: ")
            if nombre in contactos:
                del contactos[nombre]
                print("Contacto eliminado.")
            else:
                print("El contacto no existe en la agenda.")
                
        elif opcion == "3":
            nombre = input("Introduce el nombre a buscar: ")
            if nombre in contactos:
                print(f"{nombre}= {contactos[nombre]}")
            else:
                print("No se encontró ningún contacto con ese nombre.")
                
        elif opcion == "4":
                print("\nListado de contactos: ")
                for nombre in sorted(contactos.keys()):
                    print(f"{nombre}= {contactos[nombre]}")
                    
        elif opcion == "5":
            print("Cerrando agenda.")
            break


gestionar_agenda()
