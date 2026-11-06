ROSA_PASTEL = "\033[38;2;255;182;193m"
ROSA_CHICLE = "\033[38;2;255;105;180m"
ROJO = "\033[38;2;255;50;50m"
VERDE = "\033[38;2;50;255;50m"
NEGRILLA = "\033[1m" #poner texto en negrilla
RESET       = "\033[0m" #variable para apagar el color o negrita
import random
DATOS_CURIOSOS = [
    "El ciclo menstrual promedio dura 28 días, pero se considera normal que dure entre 21 y 35 días.",
    "El primer día de sangrado se cuenta como el día 1 del ciclo menstrual.",
    "El ciclo menstrual tiene cuatro fases: menstrual, folicular, ovulatoria y lútea. Cada una trae cambios hormonales distintos.",
    "Una persona nace con todos los óvulos que tendrá en la vida: entre 1 y 2 millones al nacer y unos 300.000 al llegar a la pubertad.",
    "Normalmente, el ovario libera un solo óvulo por ciclo, y ese óvulo puede ser fecundado solo durante unas 12 a 24 horas.",
    "El útero es un músculo del tamaño aproximado de una pera, capaz de expandirse enormemente durante el embarazo.",
    "Los cólicos menstruales se deben a las prostaglandinas, sustancias que hacen que el útero se contraiga para desprender su revestimiento.",
    "La cantidad total de sangre perdida en una menstruación es de solo 30 a 40 ml en promedio, aunque hasta 80 ml se considera normal.",
    "La primera menstruación (menarquia) ocurre en promedio entre los 12 y 13 años.",
    "La menopausia llega en promedio alrededor de los 51 años y se confirma tras 12 meses seguidos sin menstruar.",
    "Después de la ovulación, la progesterona eleva la temperatura corporal basal entre 0,3 y 0,5 °C.",
    "Los cambios de estrógeno y progesterona durante el ciclo pueden influir en el estado de ánimo, la energía y el sueño.",
    "Alrededor de 3 de cada 4 mujeres experimentan algún síntoma premenstrual, como hinchazón, cansancio o cambios de humor.",
    "El estrés crónico eleva el cortisol y puede retrasar la ovulación o alterar la regularidad del ciclo.",
    "La endometriosis afecta aproximadamente a 1 de cada 10 mujeres en edad reproductiva y muchas veces tarda años en diagnosticarse.",
    "El síndrome de ovario poliquístico (SOP) afecta entre el 8 % y el 13 % de las mujeres en edad reproductiva.",
    "Por la pérdida de sangre menstrual, las mujeres adultas necesitan más hierro que los hombres: unos 18 mg diarios entre los 19 y los 50 años.",
    "Las enfermedades cardiovasculares son la primera causa de muerte en mujeres en el mundo, y sus síntomas pueden ser distintos a los de los hombres.",
    "Un infarto en mujeres puede manifestarse con fatiga extrema, náuseas o dolor en la mandíbula y la espalda, no solo con dolor de pecho.",
    "Cerca de 8 de cada 10 personas con enfermedades autoinmunes son mujeres.",
    "Tras la menopausia baja el estrógeno, lo que acelera la pérdida de masa ósea y aumenta el riesgo de osteoporosis.",
    "El ejercicio libera endorfinas y puede ayudar a aliviar los cólicos y mejorar el ánimo durante el ciclo.",
    "El cuerpo femenino necesita una cantidad mínima de grasa esencial (cerca del 10-13 %) para funcionar bien, incluidas las hormonas.",
    "Durante el embarazo, el volumen de sangre aumenta alrededor de un 40 a 50 % para nutrir al bebé.",
    "Los músculos del suelo pélvico sostienen la vejiga, el útero y el intestino, y se fortalecen con ejercicios como los de Kegel.",
    "En la fase lútea, la progesterona sube la temperatura corporal, y por eso muchas mujeres duermen peor antes de la menstruación.",
    "La perimenopausia, etapa previa a la menopausia, puede venir con insomnio, sofocos y cambios de ánimo por las fluctuaciones hormonales.",
    "La leche materna se adapta a lo que el bebé necesita: cambia su composición según la edad y hasta durante el día.",
    "Hasta 1993, en Estados Unidos no era obligatorio incluir mujeres en los ensayos clínicos, por eso mucho conocimiento médico se basó en cuerpos masculinos.",
    "Beber suficiente agua ayuda a reducir el dolor de cabeza y la hinchazón que algunas mujeres sienten durante la menstruación.",
    "Las hormonas no solo afectan al útero: los receptores de estrógeno están en el cerebro, el corazón, los huesos y la piel.",
]

def mostrar_dato_curioso (ultimo=None):
    opciones = [d for d in DATOS_CURIOSOS if d != ultimo] or DATOS_CURIOSOS
    dato = random.choice(opciones)
    print(f"{ROSA_PASTEL}{NEGRILLA} ⭐ Dato curioso de la semana ⭐ {RESET}\n")
    print(f"{ROSA_PASTEL}{dato}{RESET}\n")

    while True:
        entrada = input(f"{ROSA_CHICLE}Presiona enter para volver al menú principal...{RESET}")
        if entrada == "":
            break
        print (f"{ROJO}Error: Presiona enter para volver al menú principal.{RESET}")
    return dato

if __name__ == "__main__":
    print(f"{ROSA_PASTEL}{NEGRILLA} Total de datos curiosos: {len(DATOS_CURIOSOS)}{RESET}")
    mostrar_dato_curioso()