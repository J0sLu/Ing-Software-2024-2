import random

"""
 Función Marcador que simula un partido de tenis, se le pasan 
 las variables A y B que son los nombres de los jugadores.
"""
def Marcador(A, B):

    sacador = random.choice([A, B])
    while True:
        try:
            NroPartidos = int(input("¿Cuántos sets se van jugar? "))
            if NroPartidos > 0 and NroPartidos % 2 == 1:
                break
            else:
                print("Ingresa un número mayor a 0 e impar")

        except ValueError:
            print("Ingresa un número")

    Sets = {'A': 0, 'B': 0}
    i = 1
    #Ciclo que ejecuta todos los sets del partido
    while Sets["A"] <= NroPartidos//2 and Sets["B"] <= NroPartidos//2:
        Juegos = {'A': 0, 'B': 0}
        print("")
        print(">>> Inicio del set ", i, " <<<")
        print("Número de sets ganados por jugador: ", A, " ", Sets["A"], " - ", B, " ", Sets["B"])
        NroJuegos = 1
        finSet = False
        #Ciclo que ejecuta todos los juegos de un set
        while not finSet:
            Puntos = {'A': 0, 'B': 0}
            Adv = {'A': False, 'B': False}
            Tiempo = 1
            print("")
            print("------")
            print("Juego ", NroJuegos)
            if NroJuegos % 2 == 1 and not i == 1:
                print("*Cambio de cancha*")
            print("El jugador ", sacador, " saca")
            print("")
            #Ciclo de un juego que termina cuando alguien en estado de adv marca un punto
            while True:
                #Registrar al que marcó punto
                while True:
                    ganador = input("¿Qué jugador marcó punto? ")
                    if ganador not in ["A", A, "B", B]:
                        print("Escribe el nombre del jugador que ganó o con letras (A o B)")
                    else:
                        break
                if ganador == "A":
                    Nganador = A
                if ganador == "B":
                    Nganador = B
                if Puntos[ganador] in [0, 15]:
                    Puntos[ganador] += 15
                    Adv["A"] = False
                    Adv["B"] = False
                elif Puntos[ganador] == 30:
                    Puntos[ganador] += 10
                    Adv["A"] = False
                    Adv["B"] = False
                    Adv[ganador] = True
                elif Adv[ganador] == True:
                    print("El ganador del juego es:", Nganador)
                    NroJuegos += 1
                    if sacador == A:
                        sacador = B
                    else:
                        sacador = A
                    Juegos[ganador] += 1
                    Tiempo = 3
                    break
                elif Puntos[ganador] == 40:
                    if ganador == A or ganador == "A":
                        Adv["A"] = True
                        Adv["B"] = False
                        Tiempo = 2.1
                    else:
                        Adv["A"] = False
                        Adv["B"] = True
                        Tiempo = 2.2
                if Tiempo == 1:
                    print("Puntuaciones actuales:", A, " ", Puntos["A"], " - ", B, " ", Puntos["B"])
                elif Tiempo == 2.1:
                    print("Puntuaciones actuales:", A, " ", "Adv", " - ", B, " ", Puntos["B"])
                elif Tiempo == 2.2:
                    print("Puntuaciones actuales:", A, " ", Puntos["A"], " - ", B, " ", "Adv")
                print("")

            print("")
            print("- > Juegos ganados < -")
            print(A, ": ", Juegos["A"])    
            print(B, ": ", Juegos["B"])    
            #Checamos si algún jugador ya ganó el set (Al ganar 6 juegos)
            if (abs(Juegos["A"] - Juegos["B"]) > 1 and (Juegos["A"] > 5 or Juegos["B"] > 5)):
                finSet = True
                print("")
                if Juegos["A"] > Juegos["B"]:
                    Sets["A"] += 1
                    print("Fin del set ", i, ", el jugador ", A, "gana")
                elif Juegos["B"] > Juegos["A"]:
                    Sets["B"] += 1
                    print("Fin del set ", i, ", el jugador ", B, "gana")
                i += 1
        if Sets["A"] > NroPartidos//2:
            print("")
            print("¡El jugador ", A, " es el ganador del partido de tenis!")
        elif Sets["B"] > NroPartidos//2:
            print("")
            print("¡El jugador ", B, " es el ganador del partido de tenis!")
    print(A, " ", Sets["A"], " - ", B, " ", Sets["B"])
                    

A = input("Escribe el nombre del jugador A ")
B = input("Escribe el nombre del jugador B ")
Marcador(A,B)