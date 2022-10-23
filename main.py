import sys, pygame
import numpy as np

with open('matriz.txt','r') as f:
    datos = ''.join(f.readlines()).replace('\n',';')

m = np.matrix(datos)
class Nodo:
 
 def __init__(self,estado, padre,operador, profundidad, costo):
  self._estado=estado;
  self._padre=padre;
  self.operador=operador;
  self.profundidad=profundidad;
  self.costo=costo;

 def verEstado(self):
    return self._estado.copy()

 def moverDer(self,ubiMariox,ubiMarioy):
   self._estado[ubiMariox,ubiMarioy]=0
   self._estado[ubiMariox,ubiMarioy+1]=2
   return self;

 def moverIz(self,ubiMariox,ubiMarioy):
   self._estado[ubiMariox,ubiMarioy]=0
   self._estado[ubiMariox,ubiMarioy-1]=2
   return self;
   

 def moverAb(self,ubiMariox,ubiMarioy):
   self._estado[ubiMariox,ubiMarioy]=0
   self._estado[ubiMariox+1,ubiMarioy]=2
   return self;

 def moverAr(self,ubiMariox,ubiMarioy):
   self._estado[ubiMariox,ubiMarioy]=0
   self._estado[ubiMariox-1,ubiMarioy]=2
   return self;

 def profundidad(self):
     print("La profundidad del nodo es " + self.profundidad);
  

 def operador(self):
     print("El operador usado para llegar a este nodo fue " + self.operador);
  
 def buscarMario(self):
    arr = []
    arr3 = self._estado
    for i in range (10):
        for j in range (10):
            if(arr3[i,j]==2):
                arr.append(i)
                arr.append(j)
                return arr
 def esmeta(self,i,j):
    if(j+1<9):
        if(self._estado[i,j+1]==6):
            return True
    if(i-1>0):
        if(self._estado[i-1,j]==6):
            return True
    if(i+1<9):
        if(self._estado[i+1,j]==6):
            return True
    if(j-1):
        if(self._estado[i,j-1]==6):
            return True
    #if(self._estado[i,j+1]==6 or self._estado[i-1,j]==6 or self._estado[i+1,j]==6 or self._estado[i,j-1]==6):
    #    return True
    else:
        return False

nodoActual = Nodo(m,None," ",0,0)
arr2 = nodoActual.buscarMario()
arr= []
arr.append(nodoActual)

x=0

while(not (arr[0].esmeta(arr2[0], arr2[1]))):
 if(not(arr2[1]+1 >9) and arr[0].verEstado()[arr2[0],arr2[1]+1] != 1 ): #ver si lado derecho esta sin obstaculos
    #print("si1")
    hijo = Nodo(arr[0].verEstado(), arr[0].verEstado(), "derecha", arr[0].profundidad +1 , arr[0].costo +1)
    hijo.moverDer(arr2[0], arr2[1])
    arr.append(hijo)

 if(not(arr2[1]-1 <0) and arr[0].verEstado()[arr2[0],arr2[1]-1] != 1): #ver si lado izquiero esta sin obstaculos
    #print("si2")
    hijo = Nodo(arr[0].verEstado(), arr[0].verEstado(), "izquierda", arr[0].profundidad +1 , arr[0].costo +1)
    hijo.moverIz(arr2[0], arr2[1])
    arr.append(hijo)

 if(not(arr2[0]+1>9) and arr[0].verEstado()[arr2[0]+1,arr2[1]] != 1 ): #ver si lado abajo esta sin obstaculos
      #print("si3")
      hijo = Nodo(arr[0].verEstado(), arr[0].verEstado(), "abajo", arr[0].profundidad +1 , arr[0].costo +1)
      hijo.moverAb(arr2[0], arr2[1])
      arr.append(hijo)

 if( not(arr2[0]-1<0) and arr[0].verEstado()[arr2[0]-1,arr2[1]] != 1 ): #ver si lado arriba esta sin obstaculos
      #print("si4")
      hijo = Nodo(arr[0].verEstado(), arr[0].verEstado(), "arriba", arr[0].profundidad +1 , arr[0].costo +1)
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