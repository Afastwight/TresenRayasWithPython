import random
import os

def inicializar_juego():
    "Funcion que incializa los valores del juego"
    juego_en_curso = True
    jugadores = [[input("Jugador 1: "),"X"], [input("Jugador 2: "), "O"]]
    jugador_actual = random.randint(0,1)
    tablero = [["-","-","-"],["-","-","-"],["-","-","-"]]
    return juego_en_curso, jugadores, jugador_actual, tablero

def actualizar_tablero(jugador,coordenada_fila,coordenada_columna,tablero_actual):
    """Actualiza el tablero con la accion del jugador actual"""
    tablero_actual[coordenada_fila - 1][coordenada_columna -1] = jugador[1]
    return tablero_actual

def tablero_completo(tablero_actual):
    """Comprueba si el tablero esta completo, devuelve True o False"""
    for linea in tablero_actual:
        for celda in linea:
            if celda == '-':
                return False
    return True

def comprobar_ganador(jugador,tablero_actual):
    """Comprueba si ha ganado el jugador actual, devuelve True o False"""
    #Comprobando por filas
    for i in range(3):
        ganador = True
        for x in range(3):
            if tablero_actual[i][x] != jugador[1]:
                ganador = False
                break
        if ganador:
            return ganador
        
    #Comprobando por columnas
    for i in range(3):
        ganador = True
        for x in range(3):
            if tablero_actual[x][i] != jugador[1]:
                ganador = False
                break
        if ganador:
            return ganador
    
    #Comprobando por diagonales
    ganador = True
    for i in range(3):
        if tablero_actual [i][i] != jugador[1]:
            ganador = False
            break
    if ganador:
        return ganador
        
    #No hay ganador
    ganador = True
    for i in range(3):
        if tablero_actual[i][3 - 1- i] != jugador[1]:
            ganador = False
            break
    if ganador:
        return ganador
    
    return False

juego_en_curso, jugadores, jugador_actual, tablero = inicializar_juego()


while juego_en_curso:
    if tablero_completo(tablero):
        juego_en_curso = False
        os.system("cls")
        print("Fin del juego. no hay ganador")
        break
    
    os.system("cls")
    #Nuevo turno
    print("Turno de: " + jugadores[jugador_actual][0])
    
    #Dibujar Tablero
    print ("0 1 2 3")
    coordenadas_vertical = 1
    for linea in tablero:
        print(coordenadas_vertical, linea[0], linea[1], linea[2])
        coordenadas_vertical += 1
        
    #Pide datos al usuario
    """def pide_datos():
        coordenada_fila = int(input("Introduce la coordenada de fila (entre 0 y 2): "))
        coordenada_columna = int(input("Introduce la coordenada de columna (entre 0 y 2): "))
        return coordenada_fila, coordenada_columna"""
    #Comprobacion de datos
    """Def comprobar_datos(datos):
        if 0 <= datos <= 2 and 0 <= datos <= 2:
            return True
        else:
            print("¡Coordenadas invalidas! Deben estar entre 0 y 2.")"""
    #Seleccion de casilla
    coordenada_fila,coordenada_columna = list(map(int, input("Elige coordenadas: ")))
    
    #Actualizar tablero
    tablero = actualizar_tablero(jugadores[jugador_actual], coordenada_columna, coordenada_fila, tablero)
    
    #Comprobamos si ha ganado
    if comprobar_ganador(jugadores[jugador_actual], tablero):
        juego_en_curso = False
        
        #Dibujar tablero
        os.system("cls")
        print("0 1 2 3")
        coordenadas_vertical = 1
        for linea in tablero:
            print(coordenadas_vertical, linea[0], linea[1], linea [2])
            coordenadas_vertical +=1
            
        print("Ganador: ", jugadores[jugador_actual][0])
        
    #Cambio de jugador
    jugador_actual = 1 if jugador_actual == 0 else 0 
        