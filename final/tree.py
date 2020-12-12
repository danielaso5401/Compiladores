from collections import deque  
class Arbol:
    def __init__(self, elemento, sid, token=None):
          self.sid=sid
          self.elemento = elemento
          self.hijos = []
          self.token=token
          
    def ingresar_elemento(self,arbol,element,padre,i,tok=None):
        subarbol = buscarSubarbol(arbol, padre)
        subarbol.hijos.append(Arbol(element,i,tok))
      
def buscarSubarbol(arbol, e):
      if arbol.sid == e:
          return arbol
      for subarbol in arbol.hijos:
          arbolBuscado = buscarSubarbol(subarbol, e)
          if (arbolBuscado != None):
              return arbolBuscado
      return None
  
def profundidad(arbol):
    if len(arbol.hijos) == 0: 
        return 1
    return 1 + max(map(profundidad,arbol.hijos)) 

def grado(arbol):
      return max(map(grado, arbol.hijos) + [len(arbol.hijos)])

def ejecutarProfundidadPrimero(arbol):
    print(arbol.elemento)
    for hijo in arbol.hijos:
        ejecutarProfundidadPrimero(hijo)
        
def recorrido_arbol(arbol,pila):
    if(arbol.elemento==arbol.elemento.lower() and arbol.elemento !="e"):
        arbol.token=pila.pop(0)
    for subarbol in arbol.hijos:
        recorrido_arbol(subarbol,pila)
        
def ejecutarAnchoPrimero(arbol,cola = deque(),aux1=None):
    if aux1=="ret" and arbol.elemento=="VAL":
        return 1
    aux1=arbol.elemento
    
    if (len(arbol.hijos) > 0):
        cola.extend(arbol.hijos)
    if (len(cola) != 0):
        ejecutarAnchoPrimero(cola.popleft(), cola,aux1)   

def ret_elec(element):
    if element==element.lower():
        return element