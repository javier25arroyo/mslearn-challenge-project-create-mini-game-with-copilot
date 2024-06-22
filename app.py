# Crea un juego por medio de la consola de comandos el cual consiste en dibujar un tablero de 3x3 y que dos jugadores puedan jugar en el, el juego termina cuando un jugador completa una linea horizontal, vertical o diagonal.

# Importamos la libreria de tabulate para poder dibujar el tablero
from tabulate import tabulate

# Creamos una lista con los valores del tablero
tablero = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

# Creamos una variable para saber si el juego termino
juego_terminado = False

# Creamos una variable para saber si el jugador 1 es el ganador
jugador_1_ganador = False

# Creamos una variable para saber si el jugador 2 es el ganador
jugador_2_ganador = False

# Creamos una variable para saber si el jugador 1 es el que esta jugando
jugador_1 = True

# Creamos una variable para saber si el jugador 2 es el que esta jugando
jugador_2 = False

# Creamos una variable para saber si el juego termino en empate
empate = False

# Creamos una funcion para dibujar el tablero
def dibujar_tablero():
    print(tabulate(tablero, tablefmt="fancy_grid"))

# Creamos una funcion para verificar si el juego termino

def verificar_juego_terminado():
    

    # Verificamos si el jugador 1 es el ganador
    if tablero[0][0] == "X" and tablero[0][1] == "X" and tablero[0][2] == "X":
        global juego_terminado
        global jugador_1_ganador
        juego_terminado = True
        jugador_1_ganador = True
    elif tablero[1][0] == "X" and tablero[1][1] == "X" and tablero[1][2] == "X":
        juego_terminado = True
        jugador_1_ganador = True
    elif tablero[2][0] == "X" and tablero[2][1] == "X" and tablero[2][2] == "X":
        juego_terminado = True
        jugador_1_ganador = True
    elif tablero[0][0] == "X" and tablero[1][0] == "X" and tablero[2][0] == "X":
        juego_terminado = True
        jugador_1_ganador = True
    elif tablero[0][1] == "X" and tablero[1][1] == "X" and tablero[2][1] == "X":
        juego_terminado = True
        jugador_1_ganador = True
    elif tablero[0][2] == "X" and tablero[1][2] == "X" and tablero[2][2] == "X":
        juego_terminado = True
        jugador_1_ganador = True
    elif tablero[0][0] == "X" and tablero[1][1] == "X" and tablero[2][2] == "X":
        juego_terminado = True
        jugador_1_ganador = True
    elif tablero[0][2] == "X" and tablero[1][1] == "X" and tablero[2][0] == "X":
        juego_terminado = True
        jugador_1_ganador = True

    # Verificamos si el jugador 2 es el ganador
    if tablero[0][0] == "O" and tablero[0][1] == "O" and tablero[0][2] == "O":
        juego_terminado = True
        jugador_2_ganador = True
    elif tablero[1][0] == "O" and tablero[1][1] == "O" and tablero[1][2] == "O":
        juego_terminado = True
        jugador_2_ganador = True
    elif tablero[2][0] == "O" and tablero[2][1] == "O" and tablero[2][2] == "O":
        juego_terminado = True
        jugador_2_ganador = True
    elif tablero[0][0] == "O" and tablero[1][0] == "O" and tablero[2][0] == "O":
        juego_terminado = True
        jugador_2_ganador = True
    elif tablero[0][1] == "O" and tablero[1][1] == "O" and tablero[2][1] == "O":
        juego_terminado = True
        jugador_2_ganador = True
    elif tablero[0][2] == "O" and tablero[1][2] == "O" and tablero[2][2] == "O":
        juego_terminado = True
        jugador_2_ganador = True
    elif tablero[0][0] == "O" and tablero[1][1] == "O" and tablero[2][2] == "O":
        juego_terminado = True
        jugador_2_ganador = True
    elif tablero[0][2] == "O" and tablero[1][1] == "O" and tablero[2][0] == "O":
        juego_terminado = True
        jugador_2_ganador = True
    
    # Verificamos si el juego termino en empate 
    if tablero[0][0] != "1" and tablero[0][1] != "2" and tablero[0][2] != "3" and tablero[1][0] != "4" and tablero[1][1] != "5" and tablero[1][2] != "6" and tablero[2][0] != "7" and tablero[2][1] != "8" and tablero[2][2] != "9" and juego_terminado == False:
        juego_terminado = True
        empate = True

# Creamos un ciclo while para que el juego se ejecute mientras no haya terminado

while juego_terminado == False:
    dibujar_tablero()

    # Get the player's input
    if jugador_1:
        jugador = "1"
    else:
        jugador = "2"
    movimiento = input(f"Jugador {jugador}, elige una posición (1-9): ")

    # Update the game board
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == movimiento:
                if jugador_1:
                    tablero[i][j] = "X"
                    jugador_1 = False
                    jugador_2 = True
                else:
                    tablero[i][j] = "O"
                    jugador_1 = True
                    jugador_2 = False

    # Check if the game is over
    verificar_juego_terminado()

    # Por favor muestra un mensaje cuando uno de los jugadores gane

if jugador_1_ganador:
    dibujar_tablero()
    print("¡Felicidades jugador 1, has ganado!")
elif jugador_2_ganador:
    dibujar_tablero()
    print("¡Felicidades jugador 2, has ganado!")
elif empate:
    dibujar_tablero()
    print("¡Es un empate!")

# Por favor muestra un mensaje cuando el juego termine en empate

