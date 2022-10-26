import sys, pygame
import numpy as np
import node

with open('matriz.txt','r') as f:
    datos = ''.join(f.readlines()).replace('\n',';')

m = np.matrix(datos)

nodoActual = node.Nodo(m,None," ",0,0)
arr2 = nodoActual.buscarMario()
arr= []
arr.append(nodoActual)



while(not (arr[0].esmeta(arr2[0], arr2[1]))):
 if(not(arr2[1]+1 >9) and arr[0].verEstado()[arr2[0],arr2[1]+1] != 1 ): #ver si lado derecho esta sin obstaculos
    #print("si1")
    hijo = node.Nodo(arr[0].verEstado(), arr[0].verEstado(), "derecha", arr[0].profundidad +1 , arr[0].costo +1)
    hijo.moverDer(arr2[0], arr2[1])
    arr.append(hijo)

 if(not(arr2[1]-1 <0) and arr[0].verEstado()[arr2[0],arr2[1]-1] != 1): #ver si lado izquiero esta sin obstaculos
    #print("si2")
    hijo = node.Nodo(arr[0].verEstado(), arr[0].verEstado(), "izquierda", arr[0].profundidad +1 , arr[0].costo +1)
    hijo.moverIz(arr2[0], arr2[1])
    arr.append(hijo)

 if(not(arr2[0]+1>9) and arr[0].verEstado()[arr2[0]+1,arr2[1]] != 1 ): #ver si lado abajo esta sin obstaculos
      #print("si3")
      hijo = node.Nodo(arr[0].verEstado(), arr[0].verEstado(), "abajo", arr[0].profundidad +1 , arr[0].costo +1)
      hijo.moverAb(arr2[0], arr2[1])
      arr.append(hijo)

 if( not(arr2[0]-1<0) and arr[0].verEstado()[arr2[0]-1,arr2[1]] != 1 ): #ver si lado arriba esta sin obstaculos
      #print("si4")
      hijo = node.Nodo(arr[0].verEstado(), arr[0].verEstado(), "arriba", arr[0].profundidad +1 , arr[0].costo +1)
      hijo.moverAr(arr2[0], arr2[1])
      arr.append(hijo)
 arr.pop(0)
 nodoActual1 = arr[0] 
 arr2 = nodoActual1.buscarMario()
 
print(arr[0]._padre)
print(arr[0].verEstado())

""""
pygame.init()

size = width, height = 600, 600
speed = [2, 2]
black = 0, 0, 0 

screen = pygame.display.set_mode(size)

ball = pygame.image.load("mario.png")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()"""