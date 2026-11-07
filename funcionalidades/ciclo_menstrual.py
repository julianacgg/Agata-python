from datetime import datetime, timedelta
import json
import os
import random

# Códigos de color ANSI para la consola 
class Color:
    PURPURA = '\033[95m'
    AZUL = '\033[94m'
    ROSA_CHICLE = "\033[38;2;255;105;180m"
    ROSA_PASTEL = "\033[38;2;255;182;193m"
    ROJO = '\033[91m'
    RESET = '\033[0m'
    NEGRITA = '\033[1m'

MENSAJES_FASES = {
    "menstrual": [
        "Estás en fase menstrual: Es normal sentir cansancio o cólicos. Tu cuerpo se está desprendiendo del revestimiento uterino, descansa lo que necesites.",
        "Los niveles de energía bajan un poco hoy. Prioriza alimentos ricos en hierro para compensar la perdida de sangre y date el espacio para recargar energías.",
        "Mantenerte bien hidratada y usar una almohadilla térmica (o compresa caliente) son medidas naturales muy efectivas para el malestar."
    ],
    "folicular": [
        "La glándula pituitaria libera la hormona folículo estimulante (FSH), lo que estimula a los ovarios a desarrollar varios folículos que contienen óvulos.",
        "Los niveles de estrógeno comienzan a subir gradualmente. Esto ayuda a engrosar el revestimiento del útero y suele venir acompañado de un aumento notable en la energía física y la concentración."
    ],
    "ovulación": [
        "(A mitad de tu ciclo): Tu cuerpo libera un óvulo maduro. Estos son tus días más fértiles del mes, por lo que es clave si estás buscando un embarazo (o para cuidarte más).",
        "El óvulo vive solo entre 12 y 24 horas. Algunas mujeres sienten un pequeño pinchazo en un lado del vientre o notan que su temperatura sube un poquito."
    ],
    "lútea": [
        "El cuerpo se prepara por si hubo un embarazo. Si no es así, los niveles de hormonas empiezan a bajar poco a poco, avisándole al útero que se acerque el próximo periodo.",
        "La progesterona es la hormona principal en estos días. Tiene un efecto calmante, por lo que es normal que sientas ganas de bajar el ritmo, estar más en casa y buscar comidas que te den confort.",
        "Al bajar las hormonas al final de esta fase, llega el famoso Síndrome Premenstrual (SPM). Si sientes antojos, cambios de humor o el pecho un poco sensible, no te preocupes, ¡es tu cuerpo limpiándose y completando su ciclo!"
    ],
    "retraso": [
        "Tu ciclo actual supera los 35 días. Un retraso puntual puede deberse al estrés o cambios hormonales naturales. Escucha a tu cuerpo y descansa.",
        "Atención: Llevas más de 35 días en este ciclo. Recuerda que la variabilidad es normal, pero si persiste, considera consultar a un especialista."
    ]
}


class RastreadorCiclo:
    def __init__(self, ruta_datos="datos/ciclo_menstrual.json"):
        self.ruta_datos = ruta_datos
        self.datos = self.cargar_datos()

    def cargar_datos(self):
        if not os.path.exists(self.ruta_datos):
            os.makedirs(os.path.dirname(self.ruta_datos), exist_ok=True)
            return {"ciclos": []}
        try:
            with open(self.ruta_datos, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except json.JSONDecodeError:
            return {"ciclos": []}

    def guardar_datos(self):
        with open(self.ruta_datos, "w", encoding="utf-8") as archivo:
            json.dump(self.datos, archivo, indent=4, ensure_ascii=False)
    
    def registrar_ciclo(self):
        print(f"\n{Color.PURPURA}{Color.NEGRITA}--- REGISTRO DE CICLO MENSTRUAL ฅ ^>⩊<^ ฅ ---{Color.RESET}")
        print(f"{Color.ROSA_PASTEL}ingresa los periodos anteriores q recuerdes para llegar al periodo actual˙ . ꒷ 🍰 . 𖦹˙—.{Color.RESET}")

        while True:
           #validar si ya hay ciclos y si el último ya está cerca de la fecha actual
            ciclos_actuales = self.datos.get("ciclos", [])
            if ciclos_actuales:
                ultimo = ciclos_actuales[-1]
                try:
                    f_inicio_ult = datetime.strptime(ultimo["inicio"], "%Y-%m-%d")
                    if (datetime.now() - f_inicio_ult).days <= 35:
                        print(f"{Color.ROSA_CHICLE} has registrado hasta el periodo actual en curso.{Color.RESET}")
                        break
                except ValueError:
                    pass

            num_ciclo = len(ciclos_actuales) + 1
            print(f"\n{Color.AZUL}--- Registrando Ciclo {num_ciclo} ---{Color.RESET}")

            inicio_str = input(f"{Color.AZUL}Ingresa la fecha de inicio del ciclo (YYYY-MM-DD): {Color.RESET}").strip()
            try:
                fecha_inicio = datetime.strptime(inicio_str, "%Y-%m-%d")
            except ValueError:
                print(f"{Color.ROJO} fecha invalida. Usa YYYY-MM-DD.{Color.RESET}")
                continue
            
            fin_str = input(f"{Color.AZUL}Ingresa la fecha de fin (YYYY-MM-DD): {Color.RESET}").strip()
            duracion = None
            if fin_str:
                try:
                    fecha_fin = datetime.strptime(fin_str, "%Y-%m-%d")
                    if fecha_fin <= fecha_inicio:
                        print(f"{Color.ROJO} ERROR: La fecha de fin debe ser posterior a la fecha de inicio.{Color.RESET}")
                        continue
                    duracion = (fecha_fin - fecha_inicio).days + 1
                except ValueError:
                    print(f"{Color.ROJO}  fecha inválido. Usa YYYY-MM-DD.{Color.RESET}")
                    continue
            else:
                print(f"{Color.ROJO} ERROR: Debes ingresar una fecha de fin para este registro.{Color.RESET}")
                continue

            #confirmción
            confirmacion_valida = False
            while not confirmacion_valida:
                confirmar = input(f"{Color.ROSA_PASTEL} ¿Estás segura de estas fechas? Después no podrás cambiarlas (si/no): {Color.RESET}").strip().lower()
                
                if confirmar in ['s', 'si', 'sí', 'SI']:
                    confirmacion_valida = True
                elif confirmar in ['n', 'no', 'NO']:
                    print(f"{Color.ROSA_PASTEL} Entendido, vuelve a ingresar las fechas de este ciclo.{Color.RESET}\n")
                    confirmacion_valida = "repetir"
                    break
                else:
                    print(f"{Color.ROJO} no vale. Por  favor ingresa 'si' o 'no'.{Color.RESET}\n")

            if confirmacion_valida == "repetir":
                continue

            sintomas_input = input(f"{Color.AZUL}ingresa síntomas presentados (separados por coma, ej: colicos, acne): {Color.RESET}").strip()
            lista_sintomas = [s.strip() for s in sintomas_input.split(",")] if sintomas_input else []

            nuevo_ciclo = {
                "id": num_ciclo,
                "inicio": inicio_str,
                "fin": fin_str,
                "duracion_dias": duracion,
                "sintomas": lista_sintomas
            }

            self.datos["ciclos"].append(nuevo_ciclo)
            self.guardar_datos()
            print(f"{Color.ROSA_CHICLE}ciclo guardado con éxito en el historial{Color.RESET}")

            # Preguntar si desea registrar el siguiente ciclo o si ya llegó al actual
            dias_desde_inicio = (datetime.now() - fecha_inicio).days
            if dias_desde_inicio <= 35:
                print(f"{Color.ROSA_CHICLE} Has alcanzado el periodo actual{Color.RESET}")
                break
            else:
                continuar = input(f"{Color.ROSA_PASTEL}¿Deseas registrar el siguiente ciclo para acercarte al actual? (si/no): {Color.RESET}").strip().lower()
                if continuar not in ['s', 'si', 'sí', 'SI']:
                    break

    def consultar_historial(self):
        ciclos = self.datos.get("ciclos", [])
        if not ciclos:
            print(f"\n{Color.ROSA_PASTEL} No hay ciclos registrados en el historial.{Color.RESET}")
            return

        print(f"\n{Color.PURPURA}{Color.NEGRITA}────۶ৎ────-----------------------------{Color.RESET}")
        print(f"{Color.PURPURA}{Color.NEGRITA}     ₍^. .^₎Ⳋ  HISTORIAL DE CICLOS MENSTRUALES     {Color.RESET}")
        print(f"{Color.PURPURA}{Color.NEGRITA}=========================================={Color.RESET}")

        duraciones_completas = []

        #todos los ciclos registrados por la usuaria
        for ciclo in ciclos:
            print(f"\n{Color.AZUL}🔹 Ciclo: {ciclo['id']}{Color.RESET}")
            print(f"   Inicio   : {ciclo['inicio']}")
            print(f"   Fin      : {ciclo['fin']}")

            if ciclo['duracion_dias']:
                print(f"  •⩊• duracion de tu periodo : {ciclo['duracion_dias']} días")
                duraciones_completas.append(ciclo['duracion_dias'])

            sintomas_txt = ", ".join(ciclo['sintomas']) if ciclo['sintomas'] else "Ninguno"
            print(f"   Síntomas : {sintomas_txt}")

        # Evaluar el estado de hoy basado en el último ciclo registrado
        ultimo_ciclo = ciclos[-1]
        try:
            fecha_inicio_ultimo = datetime.strptime(ultimo_ciclo['inicio'], "%Y-%m-%d")
            dias_transcurridos = (datetime.now() - fecha_inicio_ultimo).days + 1
            if dias_transcurridos < 1:
                dias_transcurridos = 1

            if dias_transcurridos > 35:
                fase = "retraso"
            elif 1 <= dias_transcurridos <= 5:
                fase = "menstrual"
            elif 6 <= dias_transcurridos <= 13:
                fase = "folicular"
            elif 14 <= dias_transcurridos <= 16:
                fase = "ovulación"
            else:
                fase = "lútea"

            mensaje = random.choice(MENSAJES_FASES[fase])
            print(f"\n{Color.PURPURA}---------------------------------------------{Color.RESET}")
            print(f"  {Color.NEGRITA}ESTADO DE HOY ⚞^. .^⚟ (Ciclo actual):{Color.RESET}")
            print(f" ୭ ᵎᵎ 🧁 Día del ciclo : {Color.ROSA_PASTEL}Día {dias_transcurridos}{Color.RESET}")
            print(f"  ݁ ˖Ი𐑼⋆ fase biológica: {Color.ROSA_PASTEL}{fase.capitalize()}{Color.RESET}")
            print(f"   mensaje de apoyo: {Color.ROSA_CHICLE}\"{mensaje}\"{Color.RESET}")
        except ValueError:
            pass

        print(f"\n{Color.PURPURA}---------------------------------------------{Color.RESET}")
        if duraciones_completas:
            promedio = sum(duraciones_completas) / len(duraciones_completas)
            print(f"Promedio de duración del ciclo: {Color.ROSA_CHICLE}{Color.NEGRITA}{promedio:.1f} días{Color.RESET}")
        else:
            print(f"promedio: {Color.ROSA_PASTEL}Se necesita al menos 1 ciclo completado para calcular el promedio.{Color.RESET}")


# prueba local
if __name__ == "__main__":
    rastreador = RastreadorCiclo()
    print(f"{Color.ROSA_CHICLE}⋆˚☆˖°⋆｡° ✮˖ ࣪ ⊹⋆.˚MÓDULO DE CICLO MENSTRUAL CARGADO CORRECTAMENTE ⋆˚☆˖°⋆｡° ✮˖ ࣪ ⊹⋆.˚{Color.RESET}")
    print(f"{Color.ROSA_CHICLE}⋆˚☆˖°⋆｡° ✮˖ ࣪ ⊹⋆.˚ ⋆˚☆˖°⋆｡° ✮˖ ࣪ ⊹⋆.˚{Color.RESET}")
    rastreador.registrar_ciclo()
    rastreador.consultar_historial()

def mostrar_ciclo_menstrual():
    rastreador = RastreadorCiclo()
    rastreador.registrar_ciclo()
    rastreador.consultar_historial()