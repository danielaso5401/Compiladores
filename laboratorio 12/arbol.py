import pandas as pd 
from graphviz import Digraph
import numpy as np


conte=[]
conte2=[]
mejorado=[]
dot = Digraph()
a=pd.read_csv('macaco_max.csv', header=None)
lista= []

with open('macaco_max.csv') as data_file:
      for line in data_file:
         lista.append(line.strip().split(','))

def comp_terminal(val):
    if val=="corpo":
        return 1
    if val=="llai":
        return 2
    if val=="llaf":
        return 3
    if val=="vaz":
        return 4
    if val=="id":
        return 5
    if val=="pari":
        return 6
    if val=="parf":
        return 7
    if val=="ret":
        return 8
    if val=="coma":
        return 9
    if val=="ler":
        return 10
    if val=="corr":
        return 11
    if val=="mostre":
        return 12
    if val=="may":
        return 13
    if val=="men":
        return 14
    if val=="maye":
        return 15
    if val=="mene":
        return 16
    if val=="dif":
        return 17
    if val=="simi":
        return 18
    if val=="sin":
        return 19
    if val=="senao":
        return 20
    if val=="senaosin":
        return 21    
    if val=="enquanto":
        return 22
    if val=="intei":
        return 23
    if val=="dupla":
        return 24
    if val=="val":
        return 25
    if val=="corrente":
        return 26
    if val=="binar":
        return 27
    if val=="equal":
        return 28
    if val=="num":
        return 29
    if val=="soma":
        return 30
    if val=="sub":
        return 31
    if val=="multi":
        return 32
    if val=="div":
        return 33
    if val=="$":
        return 34
    else:
        return 0

def comp_noterminal(stra):
    if stra=="CORPO":
        return 1
    if stra=="FUN":
        return 2
    if stra=="FUN_S":
        return 3
    if stra=="PAR":
        return 4
    if stra=="PARAM_DEF":
        return 5
    if stra=="LEC":
        return 6
    if stra=="LEC_S":
        return 7
    if stra=="MOST":
        return 8
    if stra=="MOST_S":
        return 9
    if stra=="CON":
        return 10
    if stra=="CON_S":
        return 11
    if stra=="CONT":
        return 12
    if stra=="TYPE_CON":
        return 13
    if stra=="VAL":
        return 14
    if stra=="VAL_S":
        return 15
    if stra=="TYPE":
        return 16
    if stra=="ASI":
        return 17
    if stra=="ASI_S":
        return 18
    if stra=="E":
        return 19
    if stra=="R":
        return 20
    if stra=="T":
        return 21
    if stra=="FN":
        return 22
    if stra=="SIM":
        return 23
    else:
        return 0
cadena = "corpo llai dupla id equal num llaf"

#cadena ="vaz id pari intei id coma dupla id parf llai intei id equal num ret id llaf corpo llai intei id equal num llaf"

cadena = cadena.split(' ')
cadena.append("$")
tam = len(cadena)
action=[]
stack = ["CORPO","$"]
continuar=True
aux1=0
aux2=0
aux=[]
dot.node(str(aux1), stack[0])
#conte.append(str(aux1))
conte.append(stack[0])
padres=[0,-1]
#print(stack)
#print(cadena)
while continuar:
  if stack[0]=="$" and cadena[0]=="$":
    continuar=False
    #print(stack)
    #print(cadena)
    print("Cadena aceptada")
  elif stack[0] == cadena[0]:
    #print(stack)
    #print(cadena)
    stack = stack[1:]
    cadena.pop(0)
  elif stack[0][0]==(stack[0][0]).lower() and cadena[0]==(cadena[0]).lower():
    continuar=False
    #print(stack)
    #print(cadena)
    print("Error: Cadena rechazada")
  else:
    if comp_terminal(cadena[0])!=0:
        reemplazo = lista[comp_noterminal(stack[0])][comp_terminal(cadena[0])]
        aux2=int(padres[0])
    else:
      continuar=False
      #print(stack)
      #print(cadena)
      print("Error: Cadena rechazada")
      break
    if reemplazo == "e":
      aux1=aux1+1
      h=aux1
      #dot.node(str(h), "e")
      #dot.edge(str(aux2),str(h))
      stack=stack[1:]
      padres=padres[1:]
      #print(stack)
      #print(cadena)
    else:

      array_aux=reemplazo.split()
      stack = np.concatenate((array_aux,stack[1:]),axis=0)
      hijos = len(array_aux)
      aux.clear()
      

      for e in range(hijos):
        aux1=aux1+1
        if array_aux[e][0]==array_aux[e][0].upper():
          aux.append(aux1)
        aux3=aux1
        conte.append(array_aux[e])
        #print(str(aux3), array_aux[e])
        #print('-')
        #mejorado.append(conte[aux2])
        #mejorado.append(conte[aux3])
        conte2.append(aux2)
        conte2.append(aux3)

        #print(str(aux2),str(aux3))
        #print('/')
        dot.node(str(aux3), array_aux[e])
        dot.edge(str(aux2),str(aux3))
      padres = np.concatenate((aux,padres[1:]),axis=0)
      #print(stack)
      #print(cadena)

#print(dot.source)
i=0


while i<len(conte2)-4:
    mejorado.append(conte[conte2[i]])
    mejorado.append(conte[conte2[i+1]])
    i=i+2
  
class Arbol:
  def __init__(self, elemento):
          self.hijos = []
          self.elemento = elemento
def agregarElemento(arbol, elemento, elementoPadre):
      subarbol = buscarSubarbol(arbol, elementoPadre);
      subarbol.hijos.append(Arbol(elemento))
def buscarSubarbol(arbol, elemento):
      if arbol.elemento == elemento:
          return arbol
      for subarbol in arbol.hijos:
          arbolBuscado = buscarSubarbol(subarbol, elemento)
          if (arbolBuscado != None):
              return arbolBuscado
      return None
def profundidad(arbol):
    if len(arbol.hijos) == 0: 
        return 1
    return 1 + max(map(profundidad,arbol.hijos)) 

def grado(arbol):
      return max(map(grado, arbol.hijos) + [len(arbol.hijos)])

def ejecutarProfundidadPrimero(arbol, funcion):
    funcion(arbol.elemento)
    for hijo in arbol.hijos:
        ejecutarProfundidadPrimero(hijo, funcion)

def printElement(element):
    print(element)
def ret_elec(element):
    if element==element.lower():
        return element
    
arbol = Arbol(mejorado[0])
i=0
while i<len(mejorado)-1:
  if mejorado[i]!=mejorado[i+1]:
    agregarElemento(arbol, mejorado[i+1], mejorado[i])
    #print(mejorado[i]+"->"+mejorado[i+1])
  i=i+2
ejecutarProfundidadPrimero(arbol, printElement)

def identi(arbol):
   d=buscarSubarbol(arbol, "corpo")
   if d==None:
       d=buscarSubarbol(arbol, "vaz")
       if d!=None:
           return "vaz"
   else:
       return "corpo"

print(identi(arbol))
def comprobar_existencia(arbol):
    micro=[]
    micro.append(ejecutarProfundidadPrimero(arbol, ret_elec))
    return micro
mast=comprobar_existencia(arbol)
print(mast)