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

