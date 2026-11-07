ROSA_PASTEL = "\033[38;2;255;182;193m"
ROSA_CHICLE = "\033[38;2;255;105;180m"
ROJO = "\033[38;2;255;50;50m"
VERDE = "\033[38;2;50;255;50m"
NEGRILLA = "\033[1m" #poner texto en negrilla
RESET       = "\033[0m" #variable para apagar el color o negrita

def registrar_elemento(): # FUNCION REGISTRAR 1
    print(f"\n{ROSA_CHICLE}=== ✏️ REGISTRAR NUEVO ELEMENTO ✏️ ==={RESET}")
    print("")
    nombre = input(f"Ingrese el nombre del producto: ").strip().upper()
    categorias_validas = ["MEDICINA", "HIGIENE", "RELAJACION"]

    tipo = input("Ingrese el tipo (Medicina - Higiene - Relajacion): ").strip().upper()
    while tipo not in categorias_validas: #para validar q la usuaria escriba la categoria que es
        print(f"{ROJO} ❌ Categoría no válida. Debe ser: medicina, higiene o relajación{RESET}")
        tipo = input("Intente de nuevo: ").strip().upper()

    precio = input("Ingrese el precio: ").strip()
    while not precio.isdigit():
        print(f"{ROJO} ❌ Debe ingresar un valor númerico, intentelo de nuevo.{RESET}")
        precio = input("Ingrese el precio nuevamente: ").strip()

    cantidad = input("Ingrese la cantidad de unidades: ").strip().upper()
    while not cantidad.isdigit():
        print(f"{ROJO} ❌ Debe ingresar un valor númerico, intentelo de nuevo.{RESET}")
        cantidad = input("Ingrese la cantidad nuevamente: ").strip()
    

    archivo = open("kit_autocuidado.txt", "a", encoding="utf-8") #abrir archivo
    archivo.write(f"{nombre};{tipo};{precio};{cantidad}\n") #escribir sobre el archivo en orden
    archivo.close() #cerrar archivo

    print(f"\n{ROSA_CHICLE}¡{nombre} se registro con éxito en el kit de autocuidado! ✅{RESET}")
    input(f"\n{ROSA_PASTEL}Presiona Enter para volver al menú...{RESET}")



def consultar_elementos(): #FUNCION CONSULTAR 2
    print(f"\n{ROSA_CHICLE} === 📒🔍 CONSULTAR ELEMENTOS 🔍📒 ==={RESET}")

    try:
        with open("kit_autocuidado.txt", "r", encoding="utf-8") as archivo: 
            lineas = archivo.readlines()

            if not lineas:
                print("😔 El kit de autocuidado esta vacío actualmente")
            else:
                print(f"\n{ROSA_PASTEL}{"NOMBRE":<15} | {"TIPO":<15} | {"PRECIO":<10} | {"CANTIDAD":<8}{RESET}") #titulos de la tabla
                print(f"{ROSA_CHICLE}-{RESET}" * 55) #division de la tabla

                for linea in lineas:
                    datos = linea.strip().split(";")
                    if len(datos) == 4:
                       nombre, tipo, precio, cantidad = datos
                       print(f"{nombre:<15} {ROSA_CHICLE}|{RESET} {tipo:<15} {ROSA_CHICLE}|{RESET} ${precio:<9} {ROSA_CHICLE}|{RESET} {cantidad:<8}") #mostrar los datoa guardados

    except FileNotFoundError:
        print("⚠️ Aún no existe un registro de los elementos guardados. Tienes que registrar un elemento primero")
    input(f"\n{ROSA_PASTEL}Presiona Enter para volver al menú...{RESET}")

                    

def actualizar_elemento(): #FUNCION ACTUALIZAR 3
    print(f"{ROSA_CHICLE}\n=== ⬆️  ACTUALIZAR ELEMENTO DEL KIT ⬆️ ==={RESET}")
    print("")
    nombre_buscar = input("Ingrese el nombre del producto a actualizar: ").strip().upper()

    try:
        archivo = open("kit_autocuidado.txt","r", encoding="utf-8")
        lineas = archivo.readlines()
        archivo.close()

        encontrado = False
        nuevas_lineas = []

        for linea in lineas:
            datos = linea.strip().split(";")
            if len(datos) == 4:
                nombre, tipo, precio, cantidad = datos

                if nombre.upper() == nombre_buscar:
                    print(f"{VERDE}💡 ¡PRODUCTO ENCONTRADO! Tipo actual: {tipo} | Precio: ${precio} | Cantidad: {cantidad}{RESET}")

                    categorias_validas = ["MEDICINA", "HIGIENE", "RELAJACION"]
                    nuevo_tipo = input("\nIngrese el nuevo tipo (Medicina - Higiene - Relajación): ").strip().upper()
                    while nuevo_tipo not in categorias_validas:
                        print(f"{ROJO}❌ Categoría no válida. Inténtelo de nuevo.{RESET}")
                        nuevo_tipo = input("Ingrese el tipo nuevamente: ").strip().upper()

                    nuevo_precio = input("\nIngrese el nuevo precio: ").strip()
                    while not nuevo_precio.isdigit():
                        print(f"{ROJO}❌ Debe ingresar un valor numérico.{RESET}")
                        nuevo_precio = input("Ingrese el precio nuevamente: ").strip()

                    nueva_cantidad = input("\nIngrese la nueva cantidad: ").strip()
                    while not nueva_cantidad.isdigit():
                        print(f"{ROJO}❌ Debe ingresar un valor numérico.{RESET}")
                        nueva_cantidad = input("Ingrese la cantidad nuevamente: ").strip()

                    linea_modificada = f"{nombre};{nuevo_tipo};{nuevo_precio};{nueva_cantidad}\n"
                    nuevas_lineas.append(linea_modificada)
                    encontrado = True
                else:
                    nuevas_lineas.append(linea)
        if encontrado:
            archivo = open("kit_autocuidado.txt", "w", encoding="utf-8")
            archivo.writelines(nuevas_lineas)
            archivo.close()
            print(f"{VERDE}✅ ¡Elemento actualizado con éxito!{RESET}")
        else:
            print(f"{ROJO}❌ No se encontró ningún producto con ese nombre en el kit.{RESET}")
    except FileNotFoundError:
        print("⚠️ Aún no hay un archivo de kit de autocuidado creado. Registra algo primero")
    input(f"\n{ROSA_PASTEL}Presiona Enter para volver al menú...{RESET}")


def eliminar_elemento(): #FUNCION ELIMINAR 4
    print(f"\n{ROSA_CHICLE}=== ❌ ELIMINAR ELEMENTO DEL KIT ==={RESET}")
    print("")
    nombre_buscar = input("Ingrese el nombre del producto que desea eliminar: ").strip().upper()

    try:
        archivo = open("kit_autocuidado.txt","r", encoding="utf-8")
        lineas = archivo.readlines()
        archivo.close()

        encontrado = False
        eliminado = False
        nuevas_lineas = []

        for linea in lineas:
            datos = linea.strip().split(";")
            if len(datos) == 4:
                nombre, tipo, precio, cantidad = datos

                if nombre.strip().upper() == nombre_buscar:
                    print(f"\n{VERDE} Producto encontrado y marcado para eliminar:{RESET}")
                    print(f"{ROSA_PASTEL}Tipo: {tipo} | Precio: ${precio} | Cantidad: {cantidad}\n{RESET}")

                    confirmacion = input("¿Estás segura de eliminar este elemento? (Si/No): ").strip().upper()
                    if confirmacion == "SI":
                        eliminado = True
                        encontrado = True
                    else:
                        print(f"\n{VERDE}Eliminación cancelada{RESET}")
                        print("")
                        nuevas_lineas.append(linea)
                        encontrado = True
                    break
                else: 
                    nuevas_lineas.append(linea)

        if encontrado:
            if eliminado:
                archivo = open("kit_autocuidado.txt", "w", encoding="utf-8")
                archivo.writelines(nuevas_lineas)
                archivo.close()
                print(f"\n{VERDE}✅ ¡Elemento eliminado con éxito del kit!{RESET}")
        else:
            print(f"\n{ROJO}❌ No se encontró ningún producto con ese nombre en el kit.{RESET}")

    except FileNotFoundError:
        print("⚠️ Aún no hay un archivo de kit de autocuidado creado. Registra algo primero")
        input(f"\n{ROSA_PASTEL}Presiona Enter para volver al menú...{RESET}")


def mostrar_kit_autocuidado():
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
            consultar_elementos()
        elif opcion == "3":
            actualizar_elemento()
        elif opcion == "4":
            eliminar_elemento()
        elif opcion == "5":
            print(f"{ROSA_CHICLE}Saliendo del kit de autocuidado ¡Nos vemos pronto! 👋{RESET}")
            break
        else: 
            print("❌ Opción inválida, intentalo de nuevo")
            input("\nPresiona Enter para continuar...")



