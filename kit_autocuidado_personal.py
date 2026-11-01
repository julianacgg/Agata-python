ROSA_PASTEL = "\033[38;2;255;182;193m"
ROSA_CHICLE = "\033[38;2;255;105;180m"
NEGRILLA = "\033[1m" #poner texto en negrilla
RESET       = "\033[0m" #variable para apagar el color o negrita

def registrar_elemento(): # funcion opcion 1
    print(f"\n{ROSA_CHICLE}=== ✏️ REGISTRAR NUEVO ELEMENTO ✏️ ==={RESET}")
    print("")
    nombre = input(f"Ingrese el nombre del producto: ")
    tipo = input("Ingrese el tipo (Medicina - Bienestar): ")
    precio = input("Ingrese el precio: ")
    cantidad = input("Ingrese la cantidad de unidades: ")

    archivo = open("kit_autocuidado.txt", "a", encoding="utf-8") #abrir archivo
    archivo.write(f"{nombre};{tipo};{precio};{cantidad}\n") #escribir sobre el archivo en orden
    archivo.close() #cerrar archivo

    print(f"\n{ROSA_CHICLE}¡{nombre} se registro con éxito en el kit de autocuidado! ✅{RESET}")
    input("\nPresiona Enter para volver al menú...")



while True: #bloque de codigo que muestra el menú
    print(f"{ROSA_CHICLE} 💌 === KIT AUTOCUIDADO PERSONAL === 💌{RESET}")
    print("")
    print(f"1. ✏️  {ROSA_PASTEL}Registrar elemento{RESET}")
    print(f"2. 🔍 {ROSA_PASTEL}Consultar elementos{RESET}")
    print(f"3. ⬆️  {ROSA_PASTEL}Actualizar elementos{RESET}")
    print(f"4. ❌ {ROSA_PASTEL}Eliminar elemento{RESET} ")
    print(f"5. 🚪 {ROSA_PASTEL}Salir{RESET}")

    opcion = (input(f"\nSelecciona en tu teclado el número de la opción que desees ver (1-5): "))
    if opcion == "1":
        registrar_elemento()
    elif opcion == "2":
        print("opcion de consultar en proceso")
        input("\nPresiona Enter para continuar...")
    elif opcion == "3":
        print("opcion de actualizar en proceso")
        input("\nPresiona Enter para continuar...")
    elif opcion == "4":
        print("opcion de eliminar en proceso")
        input("\nPresiona Enter para continuar...")
    elif opcion == "5":
        print("Saliendo del kit de autocuidado ¡Nos vemos pronto!")
        break
    else: 
        print("❌ Opción inválida, intentalo de nuevo")
        input("\nPresiona Enter para continuar...")



