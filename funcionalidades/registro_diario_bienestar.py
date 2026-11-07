ROSA_PASTEL = "\033[38;2;255;182;193m"
ROSA_CHICLE = "\033[38;2;255;105;180m"
ROJO = "\033[38;2;255;50;50m"
VERDE = "\033[38;2;50;255;50m"
NEGRILLA = "\033[1m" #poner texto en negrilla
RESET       = "\033[0m" #variable para apagar el color o negrita
import json
from datetime import date, datetime
ARCHIVO_DATOS = "registro_diario_bienestar.json"

ANIMOS = {
    1: "Muy mal",
    2: "Mal",
    3: "Normal",
    4: "Bien",
    5: "Muy bien",
}

def cargar_datos():
    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            if not isinstance(datos, dict):
                return {}
            return datos
    except FileNotFoundError:
        return {}
    except (json.JSONDecodeError, ValueError) as e:
        print (f"{ROJO}Error: El archivo {ARCHIVO_DATOS} está dañado.  " f" se iniciará un nuevo archivo.({e}){RESET}")
        return {}
    
def guardar_datos(datos):
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)


def pedir_numero (mensaje, minimo, maximo, entero=False):
    while True:
        texto = input(mensaje).strip().replace(",", ".")
        if texto == "":
            print(f"{ROJO}Error: No se ingresó ningún valor.{RESET}")
            continue
        try:
            valor = int(texto) if entero else float(texto)
        except ValueError:
            print(f"{ROJO}Error: No se ingresó un número válido.{RESET}")
            continue
        if valor < 0:
            print(f"{ROJO}Error: No se puede ingresar un número negativo.{RESET}")
            continue
        if valor < minimo or valor > maximo:
            print(f"{ROJO}Error: El número ingresado debe estar entre {minimo} y {maximo}.{RESET}")
            continue
        return valor

def pedir_comidas():
    while True:
        comidas = input("Ingrese las comidas del día separadas por comas: ").strip()
        if comidas == "":
            print(f"{ROJO}Error: No se ingresó ningún valor.{RESET}")
            continue
        if comidas.lower() == "ninguna":
            return []
        comidas_lista = [comida.strip() for comida in comidas.split(",") if comida.strip()]
        if not comidas_lista:
            print(f"{ROJO}Error: No se ingresó ninguna comida válida.{RESET}")
            continue
        return comidas_lista

def pedir_si_no(mensaje):
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta in ["si", "s", "sí"]:
            return True
        elif respuesta in ["no", "n"]:
            return False
        else:
            print(f"{ROJO}Error: Por favor, ingrese 'si' o 'no'.{RESET}")

def pedir_fecha(mensaje):
    while True:
        fecha_str = input(mensaje).strip()
        if fecha_str == "":
            print(f"{ROJO}Error: No se ingresó ningún valor.{RESET}")
            continue
        try:
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y").date()
            return fecha
        except ValueError:
            print(f"{ROJO}Error: La fecha ingresada no tiene el formato correcto (dd/mm/aaaa).{RESET}")

def mostrar_registro(registro):
    comidas = ", ".join(registro["comidas"]) if registro["comidas"] else "Ninguna"
    print (f"\n{ROSA_CHICLE}Registro del día {registro['fecha']}{RESET}")
    print(f"{NEGRILLA}Ánimo:{RESET} {ANIMOS[registro['animo']]}")
    print(f"{NEGRILLA}Comidas:{RESET} {comidas}")
    print(f"{NEGRILLA}Ejercicio:{RESET} {registro['ejercicio']} minutos")
    print(f"{NEGRILLA}Horas de sueño:{RESET} {registro['sueño']} horas")
    print(f"{NEGRILLA}agua:{RESET} {registro['agua']} litros")

def registrar_dia():
    datos = cargar_datos()
    bienestar = datos.setdefault("bienestar", {})
    hoy = date.today().strftime("%d/%m/%Y")
    print(f"\n{ROSA_PASTEL} === Registro del día {hoy} === {RESET}")
    if hoy in bienestar:
        print(f"{ROSA_PASTEL}Ya existe un registro para el día de hoy ({hoy}).{RESET}")
        mostrar_registro(bienestar[hoy])
        if not pedir_si_no("¿Desea sobrescribir el registro existente? (si/no): "):
            print (f"{ROSA_PASTEL}Se conservó el registro anterior.{RESET}")
            return
    print(f"\n{ROSA_CHICLE}Registro del día {hoy}{RESET}")
    print(f"\n ¿Cómo estuvo tu ánimo hoy?")
    for numero, descripcion in ANIMOS.items():
        print(f"   {numero}. {descripcion}")
    animo = pedir_numero("Ingrese su ánimo (1-5): ", 1, 5, entero=True)
    comidas = pedir_comidas()
    ejercicio = pedir_numero("Ingrese la cantidad de minutos de ejercicio realizados: ", 0, 1440, entero=True)
    sueno = pedir_numero("Ingrese las horas de sueño: ", 0, 24)
    agua = pedir_numero("Ingrese la cantidad de agua consumida (en litros): ", 0, 10)
    bienestar[hoy] = {
        "fecha": hoy,
        "animo": animo,
        "comidas": comidas,
        "ejercicio": ejercicio,
        "sueño": sueno,
        "agua": agua,
    }
    guardar_datos(datos)
    print(f"{VERDE}Registro guardado exitosamente.{RESET}")    

def consultar_registro():
    bienestar = cargar_datos().get("bienestar", {})
    if not bienestar:
        print(f"{ROSA_PASTEL}No hay registros de bienestar disponibles.{RESET}")
        return
    fecha = pedir_fecha("Ingrese la fecha del registro que desea consultar (dd/mm/aaaa): ")
    fecha_str = fecha.strftime("%d/%m/%Y")
    if fecha_str in bienestar:
        mostrar_registro(bienestar[fecha_str])
    else:
        print(f"{ROSA_PASTEL}No se encontró un registro para la fecha {fecha_str}.{RESET}")

def ver_historial():
    bienestar = cargar_datos().get("bienestar", {})
    if not bienestar:
        print(f"{ROSA_PASTEL}No hay registros de bienestar disponibles.{RESET}")
        return
    print(f"\n{ROSA_CHICLE}=== Historial de registros de bienestar ==={RESET}")
    for fecha in sorted(bienestar, key=lambda f: datetime.strptime(f, "%d/%m/%Y")):
        registro = bienestar[fecha]
        ejercicio = f"{registro['ejercicio']} minutos"
        comidas = len(registro.get("comidas", []))
        print(
            f"{ROSA_PASTEL}Fecha: {fecha}{RESET} | "
            f"Agua: {registro['agua']} L | "
            f"Sueño: {registro['sueño']} h | "
            f"Ejercicio: {ejercicio} | "
            f"Ánimo: {ANIMOS[registro['animo']]} | "
            f"{comidas} comidas"
        )

def menu_bienestar():
    while True:
        print(f"\n{ROSA_PASTEL}=== Registro diario de Bienestar ==={RESET}")
        print("1. Registrar mi día")
        print("2. Consultar un registro hecho")
        print("3. Ver historial completo de registros")
        print("4. Salir al menú principal")
        opcion = input("Seleccione una opción (1-4): ").strip()
        if opcion == "1":
            registrar_dia()
        elif opcion == "2":
            consultar_registro()
        elif opcion == "3":
            ver_historial()
        elif opcion == "4":
            print(f"{ROSA_PASTEL}Saliendo del menú de bienestar...{RESET}")
            return
        else:
            print(f"{ROJO}Error: Opción no válida. Por favor, seleccione una opción del 1 al 4.{RESET}")

if __name__ == "__main__":
    menu_bienestar()

