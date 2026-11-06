from gestion_de_retos import mostrar_gestion_retos
from kit_autocuidado_personal import mostrar_kit_autocuidado
from ciclo_menstrual import mostrar_ciclo_menstrual
from datos_curiosos import mostrar_dato_curioso
from registro_diario_bienestar import menu_bienestar

#PALETA DE COLORES
ROSA_PASTEL = "\033[38;2;255;182;193m"
ROSA_CHICLE = "\033[38;2;255;105;180m"
RESET       = "\033[0m" #variable para apagar el color

def mostrar_menu(): #llamar funcion cada vez para mostrar el menú
    print (f"{ROSA_CHICLE}🌸🌸 == ÁGATA BIENESTAR FEMENINO == 🌸🌸{RESET}")
    print(f"{ROSA_PASTEL}!Bienvenida! Selecciona en tu teclado el número de la opción que desees ver (1-7): {RESET}")
    print("")
    print("1. ☀️ Registro diario bienestar") #johan
    print("2. 🏆 Gestión de retos") #juliana
    print("3. 🌜 Seguimiento del ciclo menstrual") #valerie
    print("4. 🌼 Kit autocuidado personal ") #juliana
    print("5. ⭐ Datos curioso de la semana") #johan
    print("6. 🚪 Salir") #
    

while True:
    mostrar_menu()
    opcion = (input("Ingrese cualquier opción del menú (1-7): "))
    if opcion == "1":
        menu_bienestar()
        input("\nPresiona Enter para continuar...") 
    elif opcion == "2":
        mostrar_gestion_retos()
        input("\nPresiona Enter para continuar...")
    elif opcion == "3":
        mostrar_ciclo_menstrual()
        input("\nPresiona Enter para continuar...")
    elif opcion == "4":
        mostrar_kit_autocuidado()
        input("\nPresiona Enter para continuar...")
    elif opcion == "5":
        mostrar_dato_curioso()
        
    elif opcion == "6":
        print ("Saliendo del programa !Hasta luego!")
        break
    else:
        print("Opción inválida, ingresa un número del 1 al 7")
        input("\nPresiona Enter para continuar...")