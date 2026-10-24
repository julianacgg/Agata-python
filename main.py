from gestion_de_retos import mostrar_gestion_retos
#PALETA DE COLORES
ROSA_PASTEL = "\033[38;2;255;182;193m"
ROSA_CHICLE = "\033[38;2;255;105;180m"
RESET       = "\033[0m" #variable para apagar el color

def mostrar_menu(): #llamar funcion cada vez para mostrar el menú
    print (f"{ROSA_CHICLE}🌸🌸 == ÁGATA BIENESTAR FEMENINO == 🌸🌸{RESET}")
    print(f"{ROSA_PASTEL}!Bienvenida! Selecciona en tu teclado el número de la opción que desees ver{RESET}")
    print("")
    print("1. ☀️ Registro diario bienestar") #johan
    print("2. 📅 Ver resumenes semanales") #valerie
    print("3. 🏆 Gestión de retos") #juliana
    print("4. 🌜 Seguimiento del ciclo menstrual") #valerie
    print("5. 🎯 Gestión de habitos") #juliana
    print("6. ⭐ Datos curioso de la semana") #johan
    print("7. 🚪 Salir")

while True:
    mostrar_menu()
    opcion = int(input("Ingrese cualquier opción del menú (1-7)"))
    if opcion ==1:
        print(" OPCION 1 EN DESARROLLO") #reemplazar luego por cada pestaña
        input("\nPresiona Enter para continuar...") 
    elif opcion == 2:
        print("OPCION 2 EN DESARROLLO")
        input("\nPresiona Enter para continuar...")
    elif opcion == 3:
        mostrar_gestion_retos()
        input("\nPresiona Enter para continuar...")
    elif opcion == 4:
        print("OPCION 4 EN DESARROLLO")
        input("\nPresiona Enter para continuar...")
    elif opcion ==5:
        print("OPCION 5 EN DESARROLLO")
        input("\nPresiona Enter para continuar...")
    elif opcion == 6:
        print("OPCION 6 EN DESARROLLO")
        input("\nPresiona Enter para continuar...")
    elif opcion == 7:
        print ("Saliendo del programa !Hasta luego!")
        break
    else:
        print("Opción inválida, ingresa un número del 1 al 7")
        input("\nPresiona Enter para continuar...")