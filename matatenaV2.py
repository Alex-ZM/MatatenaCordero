
    #####################################
    ####     MATATENA DEL CORDERO    ####
    #####################################

import numpy as np
import time
import os

iaTablero = np.zeros((3,3),np.int8)  
plTablero = np.zeros((3,3),np.int8)
tablero = np.zeros((2,3,3),np.int8)

########################################################################################################################
def display(u,roll, pos):

    ## Según el valor de u, se juega en un lado u otro del tablero
    v = np.abs(u-1)  # Si u=1, v=0; si u=0, v=1

    ## Se coloca el dado en la posición elegida
    if tablero[v,0,pos]==0:
        tablero[v,0,pos] = roll
    elif tablero[v,1,pos]==0:
        tablero[v,1,pos] = roll
    else:
        tablero[v,2,pos] = roll

    ## Se muestra el estado del tablero durante un instante
    os.system('cls' if os.name=='nt' else 'clear')
    print("  ┌┐     ┌┐     ┌┐     ┌┐")

    for i in range(2,-1,-1):
        if tablero[v,i,0]==0:
            num1 = "   "
        else:
            num1 = " "+str(tablero[v,i,0])+" "
        if tablero[v,i,1]==0:
            num2 = "   "
        else:
            num2 = " "+str(tablero[v,i,1])+" "
        if tablero[v,i,2]==0:
            num3 = "   "
        else:
            num3 = " "+str(tablero[v,i,2])+" "

        print("  ││ "+num1+" ││ "+num2+" ││ "+num3+" ││")
        
    print("  │├─────┤├─────┤├─────┤│")
    for i in range(3):
        if tablero[u,i,0]==0:
            num1 = "   "
        else:
            num1 = " "+str(tablero[u,i,0])+" "
        if tablero[u,i,1]==0:
            num2 = "   "
        else:
            num2 = " "+str(tablero[u,i,1])+" "
        if tablero[u,i,2]==0:
            num3 = "   "
        else:
            num3 = " "+str(tablero[u,i,2])+" "
        
        print("  ││ "+num1+" ││ "+num2+" ││ "+num3+" ││")

    print("  └┘     └┘     └┘     └┘\n")

    if u==0:
        time.sleep(1.5)

    ## Se eliminan los dados iguales en toda la columna (en ambas matrices):
    eliminacion = False  # Para tener en cuenta si se ha eliminado algún dado o no
    for i in range(3):
        if tablero[u,i,pos]==roll:
            tablero[u,i,pos] = 0
            eliminacion = True

    ## Se reordenan los dados si ha habido alguna eliminación:
    if eliminacion==True:
        col = tablero[u,:,pos]
        no_nulos = col[col!=0]
        nulos = col[col==0]
        colReordenada = np.concatenate((no_nulos,nulos))
        tablero[u,:,pos] = colReordenada

    # Si se elimina, hay que borrar el dado que se acaba de colocar
    if eliminacion==True:  
        if tablero[v,2,pos]!=0:
            tablero[v,2,pos] = 0
        elif tablero[v,1,pos]!=0:
            tablero[v,1,pos] = 0
        else:
            tablero[v,0,pos] = 0

    os.system('cls' if os.name=='nt' else 'clear')
    print("  ┌┐     ┌┐     ┌┐     ┌┐")

    for i in range(2,-1,-1):
        if tablero[v,i,0]==0:
            num1 = "   "
        elif tablero[v,i,0]==tablero[v,(i+1)%3,0] or tablero[v,i,0]==tablero[v,(i+2)%3,0]:
            num1 = "░"+str(tablero[v,i,0])+"░"
        else:
            num1 = " "+str(tablero[v,i,0])+" "

        if tablero[v,i,1]==0:
            num2 = "   "
        elif tablero[v,i,1]==tablero[v,(i+1)%3,1] or tablero[v,i,1]==tablero[v,(i+2)%3,1]:
            num2 = "░"+str(tablero[v,i,1])+"░"
        else:
            num2 = " "+str(tablero[v,i,1])+" "

        if tablero[v,i,2]==0:
            num3 = "   "
        elif tablero[v,i,2]==tablero[v,(i+1)%3,2] or tablero[v,i,2]==tablero[v,(i+2)%3,2]:
            num3 = "░"+str(tablero[v,i,2])+"░"
        else:
            num3 = " "+str(tablero[v,i,2])+" "

        print("  ││ "+num1+" ││ "+num2+" ││ "+num3+" ││")
        
    print("  │├─────┤├─────┤├─────┤│")
    for i in range(3):
        if tablero[u,i,0]==0:
            num1 = "   "
        elif tablero[u,i,0]==tablero[u,(i+1)%3,0] or tablero[u,i,0]==tablero[u,(i+2)%3,0]:
            num1 = "░"+str(tablero[u,i,0])+"░"
        else:
            num1 = " "+str(tablero[u,i,0])+" "
        if tablero[u,i,1]==0:
            num2 = "   "
        elif tablero[u,i,1]==tablero[u,(i+1)%3,1] or tablero[u,i,1]==tablero[u,(i+2)%3,1]:
            num2 = "░"+str(tablero[u,i,1])+"░"
        else:
            num2 = " "+str(tablero[u,i,1])+" "
        if tablero[u,i,2]==0:
            num3 = "   "
        elif tablero[u,i,2]==tablero[u,(i+1)%3,2] or tablero[u,i,2]==tablero[u,(i+2)%3,2]:
            num3 = "░"+str(tablero[u,i,2])+"░"
        else:
            num3 = " "+str(tablero[u,i,2])+" "
        
        print("  ││ "+num1+" ││ "+num2+" ││ "+num3+" ││  <")

    print("  └┘     └┘     └┘     └┘\n")

    ## Se comprueba si la partida ha acabado (acaba cuando se llena el tablero)
    if np.count_nonzero(tablero[v])==9:
        return True
    else: 
        return False

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
        if tablero[0,2,j]==0:
            if tablero[0,0,j]==iaRoll or tablero[0,1,j]==iaRoll:
                iaDuo = [iaRoll,j]

            if tablero[0,0,j]==tablero[0,1,j] and iaDuo[0]==iaRoll:
                iaTrio = [iaRoll,j]

    ## Se comprueba si el jugador tiene algún duo o trio:
    for j in range(3):
        if tablero[0,2,j]==0:  # La IA sólo debe comprobar una columna si en su parte del tablero queda hueco en la misma
            if tablero[1,0,j]==tablero[1,1,j]:
                plDuo = [tablero[1,0,j],j]
            elif tablero[1,0,j]==tablero[1,2,j]:
                plDuo = [tablero[1,0,j],j]
            elif tablero[1,1,j]==tablero[1,2,j]:
                plDuo = [tablero[1,1,j],j]
        
            if plDuo!=0 and tablero[1,0,j]==tablero[1,1,j] and tablero[1,1,j]==tablero[1,2,j]:
                plTrio = [tablero[1,0,j],j]
    
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
        while tablero[0,2,j]!=0 and fin==False:
            j = np.random.randint(0,3)
        return [iaRoll,j]
    
########################################################################################################################
def player():

    ## El jugador tira su dado:
    plRoll = np.random.randint(1,7)
    print("--> Tiras un dado y sacas: " + str(plRoll))

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
    fin = display(0,iaPlay[0],iaPlay[1])

    if fin==False:
        # Turno del jugador
        plPlay = player()
        fin = display(1,plPlay[0],plPlay[1])
        
## Se muestra el estado final del tablero:
os.system('cls' if os.name=='nt' else 'clear')
print("  ┌┐     ┌┐     ┌┐     ┌┐")
for i in range(2,-1,-1):
    if tablero[1,i,0]==0:
        num1 = "   "
    elif tablero[1,i,0]==tablero[1,(i+1)%3,0] or tablero[1,i,0]==tablero[1,(i+2)%3,0]:
        num1 = "░"+str(tablero[1,i,0])+"░"
    else:
        num1 = " "+str(tablero[1,i,0])+" "

    if tablero[1,i,1]==0:
        num2 = "   "
    elif tablero[1,i,1]==tablero[1,(i+1)%3,1] or tablero[1,i,1]==tablero[1,(i+2)%3,1]:
        num2 = "░"+str(tablero[1,i,1])+"░"
    else:
        num2 = " "+str(tablero[1,i,1])+" "

    if tablero[1,i,2]==0:
        num3 = "   "
    elif tablero[1,i,2]==tablero[1,(i+1)%3,2] or tablero[1,i,2]==tablero[1,(i+2)%3,2]:
        num3 = "░"+str(tablero[1,i,2])+"░"
    else:
        num3 = " "+str(tablero[1,i,2])+" "

    print("  ││ "+num1+" ││ "+num2+" ││ "+num3+" ││")
    
print("  │├─────┤├─────┤├─────┤│")
for i in range(3):
    if tablero[0,i,0]==0:
        num1 = "   "
    elif tablero[0,i,0]==tablero[0,(i+1)%3,0] or tablero[0,i,0]==tablero[0,(i+2)%3,0]:
        num1 = "░"+str(tablero[0,i,0])+"░"
    else:
        num1 = " "+str(tablero[0,i,0])+" "
    if tablero[0,i,1]==0:
        num2 = "   "
    elif tablero[0,i,1]==tablero[0,(i+1)%3,1] or tablero[0,i,1]==tablero[0,(i+2)%3,1]:
        num2 = "░"+str(tablero[0,i,1])+"░"
    else:
        num2 = " "+str(tablero[0,i,1])+" "
    if tablero[0,i,2]==0:
        num3 = "   "
    elif tablero[0,i,2]==tablero[0,(i+1)%3,2] or tablero[0,i,2]==tablero[0,(i+2)%3,2]:
        num3 = "░"+str(tablero[0,i,2])+"░"
    else:
        num3 = " "+str(tablero[0,i,2])+" "
    
    print("  ││ "+num1+" ││ "+num2+" ││ "+num3+" ││  <")

print("  └┘     └┘     └┘     └┘\n")


## Se calcula la puntuación final:
def puntuacion(u):
    punt = 0
    for j in range(3):
        if tablero[u,0,j]==tablero[u,1,j] and tablero[u,0,j]==tablero[u,2,j]:
            punt += tablero[u,0,j]**3
        elif tablero[u,0,j]==tablero[u,1,j]:
            punt += tablero[u,0,j]**2+tablero[u,2,j]
        elif tablero[u,0,j]==tablero[u,2,j]:
            punt += tablero[u,0,j]**2+tablero[u,1,j]
        elif tablero[u,1,j]==tablero[u,2,j]:
            punt += tablero[u,1,j]**2+tablero[u,0,j]
        else:
            punt += tablero[u,0,j]+tablero[u,1,j]+tablero[u,2,j]
    return punt

print("--> PUNTUACIÓN:     Tú - "+str(puntuacion(0))+" || "+str(puntuacion(1))+" - PC")
