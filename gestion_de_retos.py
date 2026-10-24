ROSA_PASTEL = "\033[38;2;255;182;193m"
ROSA_CHICLE = "\033[38;2;255;105;180m"
NEGRILLA = "\033[1m" #poner texto en negrilla
RESET       = "\033[0m" #variable para apagar el color o negrita

import json
import numpy as np

def mostrar_gestion_retos():

    #leer el json
    try:
        with open("datos.json", "r") as archivo:
            datos = json.load(archivo)
            dias_acumulados = datos.get("dias_acumulados", 0)
    except (FileNotFoundError, json.JSONDecodeError):
        # Si el archivo está vacío arranca en 0
        dias_acumulados = 0

    
    retos=np.zeros(4,dtype=object)
    nombre_retos=np.zeros(4,dtype=object)

    nombre_retos[0] = (f"\n{ROSA_PASTEL}{NEGRILLA}1. Desconexión digital{RESET}")
    nombre_retos[1] = (f"\n{ROSA_PASTEL}{NEGRILLA}2. Movimiento consciente{RESET}")
    nombre_retos[2] = (f"\n{ROSA_PASTEL}{NEGRILLA}3. Alimentación consciente{RESET}")
    nombre_retos[3] = (f"\n{ROSA_PASTEL}{NEGRILLA}4. Postura y ergonomía{RESET}")


    #retos en un vector
    retos[0] = (f"\n{ROSA_PASTEL}{NEGRILLA}1. 📲 Desconexión digital:{RESET} Evita pantallas una hora antes de dormir durante una semana para mejorar el descanso y la melatonina.")
    retos[1] = (f"\n{ROSA_PASTEL}{NEGRILLA}2. 🚶 Movimiento consciente:{RESET} Dedica 10 o 15 minutos al día a estiramientos suaves o movilidad articular")
    retos[2] = (f"\n{ROSA_PASTEL}{NEGRILLA}3. 🍓 Alimentación consciente:{RESET} Reemplaza los snacks empaquetados por una fruta o frutos secos toda la semana")
    retos[3] = (f"\n{ROSA_PASTEL}{NEGRILLA}4. 🦴 Postura y ergonomía:{RESET} Ajusta la postura de tu espalda durante las horas de estudio para cuidar las articulaciones y prevenir fatiga.")

    print(f"{ROSA_CHICLE}⭐🏆== GESTIÓN DE RETOS ==🏆⭐{RESET}")
    print("")

    for i in range(0,4,1):
        print(retos[i])

    eleccion=int(input("\nIngresa el reto que deseas activar: "))
    while eleccion <1 or eleccion > 4:
        eleccion=int(input("El número elegido no se encuentra dentro de las opciones, intentalo de nuevo: "))

    reto_activo= nombre_retos[eleccion-1]
    print(f"\nActivaste el reto {reto_activo} con exito!! ✅")


    respuesta= input("\n¿Cumpliste tu reto el día de hoy? (Si/No): ").strip().capitalize() #preguntar si cumplio el reto
    dias_acumulados=0
    while respuesta != "Si" and respuesta != "No":
        print("Respuesta no reconocida, intenta de nuevo.")
        respuesta = input("¿Cumpliste tu reto el día de hoy? (Si/No): ").strip().capitalize()
    if respuesta == "Si":
        dias_acumulados +=1
        print(f"{ROSA_CHICLE}¡Excelente trabajo! Progreso actual: {dias_acumulados}/7 días de avance a tu reto 🎯{RESET}") #imprimir dias acumulados
    elif respuesta == "No":
        print(f"{ROSA_CHICLE}No te preocupes, el camino del bienestar es constante ¡Mañana lo lograrás! 💗{RESET}")
    


    #definir checklist visual
    checklist=""
    for i in range(1,8): #cuenta los dias de la semana
        if i <= dias_acumulados:
            checklist += f"[ Día {i} ✅] "
        else:
            checklist += f"[ Día {i} ❌] "

    #imprimir checklist
    print(f"\n{ROSA_PASTEL}📋 TU CHECKLIST SEMANAL:{RESET}")
    print(checklist)

    #guardar en json
    datos_a_guardar = {"dias_acumulados": dias_acumulados}
    with open("datos.json", "w") as archivo:
        json.dump(datos_a_guardar, archivo, indent=4)

