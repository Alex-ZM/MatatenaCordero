
    #####################################
    ####     MATATENA DEL CORDERO    ####
    #####################################

import numpy as np
import os

iaTablero = np.zeros((3,3),np.int8)  
plTablero = np.zeros((3,3),np.int8)


########################################################################################################################
def iaDisplay(iaRoll, iaPos):

    ## Se eliminan los dados iguales en toda la columna (en ambas matrices):
    eliminacion = False  # Para tener en cuenta si se ha eliminado algún dado o no
    for i in range(3):
        if plTablero[i,iaPos]==iaRoll:
            plTablero[i,iaPos] = 0
            eliminacion = True

    ## Se reordenan los dados si ha habido alguna eliminación:
    if eliminacion==True:
        col = plTablero[:,iaPos]
        no_nulos = col[col!=0]
        nulos = col[col==0]
        colReordenada = np.concatenate((no_nulos,nulos))
        plTablero[:,iaPos] = colReordenada

    ## Se modifica la matriz iaTablero según la mano de la IA:
    if eliminacion==False:  # Si se elimina, no hay que poner el dado
        if iaTablero[0,iaPos]==0:
            iaTablero[0,iaPos] = iaRoll
        elif iaTablero[1,iaPos]==0:
            iaTablero[1,iaPos] = iaRoll
        else:
            iaTablero[2,iaPos] = iaRoll

    os.system('cls' if os.name=='nt' else 'clear')
    print("  ┌┐     ┌┐     ┌┐     ┌┐")

    for i in range(2,-1,-1):
        if iaTablero[i,0]==0:
            num1 = "   "
        else:
            num1 = " "+str(iaTablero[i,0])+" "
        if iaTablero[i,1]==0:
            num2 = "   "
        else:
            num2 = " "+str(iaTablero[i,1])+" "
        if iaTablero[i,2]==0:
            num3 = "   "
        else:
            num3 = " "+str(iaTablero[i,2])+" "

        print("  ││ "+num1+" ││ "+num2+" ││ "+num3+" ││")
        
    print("  │├─────┤├─────┤├─────┤│")
    for i in range(3):
        if plTablero[i,0]==0:
            num1 = "   "
        else:
            num1 = " "+str(plTablero[i,0])+" "
        if plTablero[i,1]==0:
            num2 = "   "
        else:
            num2 = " "+str(plTablero[i,1])+" "
        if plTablero[i,2]==0:
            num3 = "   "
        else:
            num3 = " "+str(plTablero[i,2])+" "
        
        print("  ││ "+num1+" ││ "+num2+" ││ "+num3+" ││")

    print("  └┘     └┘     └┘     └┘\n")


########################################################################################################################
def plDisplay(plRoll, plPos):
    
    ## Se eliminan los dados iguales en toda la columna (en ambas matrices):
    eliminacion = False  # Para tener en cuenta si se ha eliminado algún dado o no
    for i in range(3):
        if iaTablero[i,plPos]==plRoll:
            iaTablero[i,plPos] = 0
            eliminacion = True

    ## Se reordenan los dados si ha habido alguna eliminación:
    if eliminacion==True:
        col = iaTablero[:,plPos]
        no_nulos = col[col!=0]
        nulos = col[col==0]
        colReordenada = np.concatenate((no_nulos,nulos))
        iaTablero[:,plPos] = colReordenada

    ## Se modifica la matriz iaTablero según la mano de la IA:
    if eliminacion==False:  # Si se elimina, no hay que poner el dado
        if plTablero[0,plPos]==0:
            plTablero[0,plPos] = plRoll
        elif plTablero[1,plPos]==0:
            plTablero[1,plPos] = plRoll
        else:
            plTablero[2,plPos] = plRoll

    os.system('cls' if os.name=='nt' else 'clear')
    print("  ┌┐     ┌┐     ┌┐     ┌┐")

    for i in range(2,-1,-1):
        if iaTablero[i,0]==0:
            num1 = "   "
        else:
            num1 = " "+str(iaTablero[i,0])+" "
        if iaTablero[i,1]==0:
            num2 = "   "
        else:
            num2 = " "+str(iaTablero[i,1])+" "
        if iaTablero[i,2]==0:
            num3 = "   "
        else:
            num3 = " "+str(iaTablero[i,2])+" "

        print("  ││ "+num1+" ││ "+num2+" ││ "+num3+" ││")
        
    print("  │├─────┤├─────┤├─────┤│")
    for i in range(3):
        if plTablero[i,0]==0:
            num1 = "   "
        else:
            num1 = " "+str(plTablero[i,0])+" "
        if plTablero[i,1]==0:
            num2 = "   "
        else:
            num2 = " "+str(plTablero[i,1])+" "
        if plTablero[i,2]==0:
            num3 = "   "
        else:
            num3 = " "+str(plTablero[i,2])+" "
        
        print("  ││ "+num1+" ││ "+num2+" ││ "+num3+" ││")

    print("  └┘     └┘     └┘     └┘\n")
        
########################################################################################################################
## La IA estudia el tablero y devuelve como resultado el vector [número a jugar (1-6), columna en la que lo coloca]
def ia():

    ## La IA tira su dado
    iaRoll = np.random.randint(1,7)

    ## Aquí se almacena la información de los duos y trios 
    # Formato: [valor del dado, columna en la que se encuentra]
    iaTrio = [0,0]
    plTrio = [0,0]
    iaDuo = [0,0]
    plDuo = [0,0]

    ## Se comprueba si la IA puede formar algún duo o trio con el dado que ha obtenido
    for j in range(3):
        if iaTablero[2,j]==0:
            if iaTablero[0,j]==iaRoll:
                iaDuo = [iaRoll,j]

            if iaTablero[0,j]==iaTablero[1,j] and iaDuo[0]==iaRoll:
                iaTrio = [iaRoll,j]

    ## Se comprueba si el jugador tiene algún duo o trio:
    for j in range(3):
        if iaTablero[2,j]==0:  # La IA sólo debe comprobar una columna si en su parte del tablero queda hueco en la misma
            if plTablero[0,j]==plTablero[1,j]:
                plDuo = [plTablero[0,j],j]
            elif plTablero[0,j]==plTablero[2,j]:
                plDuo = [plTablero[0,j],j]
            elif plTablero[1,j]==plTablero[2,j]:
                plDuo = [plTablero[1,j],j]
        
            if plDuo!=0 and plTablero[0,j]==plTablero[1,j] and plTablero[1,j]==plTablero[2,j]:
                plTrio = [plTablero[0,j],j]
    
    # La IA decide qué hacer:
    if iaTrio!=[0,0]:
        return iaTrio
    elif plTrio!=[0,0] and iaRoll==plTrio[0]:
        return plTrio
    elif iaDuo!=[0,0]:
        return iaDuo
    elif plDuo!=[0,0] and iaRoll==plDuo[0]:
        return plDuo
    else:  # Si no hay ninguna jugada favorable, la IA coloca en una fila aleatoria
        j = np.random.randint(0,3)
        while iaTablero[2,j]!=0:
            j = np.random.randint(0,3)
        return [iaRoll,j]
    
########################################################################################################################
def player():

    ## El jugador tira su dado:
    plRoll = np.random.randint(1,7)
    print("Tiras un dado y sacas: " + str(plRoll))

    ## El jugador elige en qué columna colocar su dado:
    plPos = 0
    while int(plPos)<1 or int(plPos)>3:
        plPos = input("¿En qué columna quieres colocar el dado? (1, 2 ó 3): ")
    return [plRoll,int(plPos)-1]

########################################################################################################################

## Bucle de juego
fin = False
while fin==False:
    # Turno de la IA
    iaPlay = ia()
    iaDisplay(iaPlay[0],iaPlay[1])

    # Turno del jugador
    plPlay = player()
    plDisplay(plPlay[0],plPlay[1])

# TO-DO: 
#  1) Parar la partida cuando acabe
#  2) Hacer el recuento de puntos y decir el ganador