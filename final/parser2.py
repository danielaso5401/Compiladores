import analizador_lexico
import xlrd
import pandas as pd
import numpy as np
from graphviz import Digraph
import tree
dot = Digraph()

def columnas(val):
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
    if val=="saida":
        return 10
    if val=="dama":
        return 11
    if val=="ler":
        return 12
    if val=="mostre":
        return 13
    if val=="may":
        return 14
    if val=="men":
        return 15
    if val=="maye":
        return 16
    if val=="mene":
        return 17
    if val=="dif":
        return 18
    if val=="simi":
        return 19
    if val=="sin":
        return 20
    if val=="senao":
        return 21
    if val=="senaosin":
        return 22
    if val=="enquanto":
        return 23
    if val=="intei":
        return 24
    if val=="dupla":
        return 25
    if val=="val":
        return 26
    if val=="corrente":
        return 27
    if val=="binar":
        return 28
    if val=="equal":
        return 29
    if val=="num":
        return 30
    if val=="corr":
        return 31
    if val=="soma":
        return 32
    if val=="sub":
        return 33
    if val=="multi":
        return 34
    if val=="div":
        return 35
    if val=="$":
        return 36

def filas(stra):
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
    if stra=="CON":
        return 6
    if stra=="CON_S":
        return 7
    if stra=="OU":
        return 8
    if stra=="OU_S":
        return 9
    if stra=="PU":
        return 10
    if stra=="PU_S":
        return 11
    if stra=="LEC":
        return 12
    if stra=="LEC_S":
        return 13
    if stra=="MOST":
        return 14
    if stra=="MOST_S":
        return 15
    if stra=="CONT":
        return 16
    if stra=="TYPE_CON":
        return 17
    if stra=="VAL":
        return 18
    if stra=="VAL_S":
        return 19
    if stra=="TYPE":
        return 20
    if stra=="ASI":
        return 21
    if stra=="ASI_S":
        return 22
    if stra=="E":
        return 23
    if stra=="R":
        return 24
    if stra=="T":
        return 25
    if stra=="FN":
        return 26
    if stra=="SIM":
        return 27
    else:
        return 0
def ver_error(x):
    if x==1:
        print("errror linea 7 _r no declarada")
def ved():
    print("error linea 7 _r no es tipo intei")
    return False
df = pd.read_excel("final.xlsx", 'Hoja1',  header=None)
tablita_parse = df.values

pila = ["CORPO","$"]
entrada = analizador_lexico.cadena2
entrada.append("$")
pila_tokens = analizador_lexico.cadena3

continuar=True
i=0
j=0
p=0
aux=[]
pendientes=[]
arbolito = tree.Arbol(pila[0],0)
dot.node(str(j), pila[0])
padres=[0,-1]
#print("Inicio:")
#print(pila)
#print(entrada)

while continuar:
  #print("Vuelta",i)
  if pila[0]=="$" and entrada[0]=="$":
    continuar=False
    #print(pila)
    #print(entrada)
    print("Cadena aceptada")
  elif pila[0] == entrada[0]:
    #print(pila)
    #print(entrada)
    pila = pila[1:]
    entrada.pop(0)
  elif pila[0][0]==(pila[0][0]).lower() and entrada[0][0]==(entrada[0][0]).lower():
    continuar=False
    #print(pila)
    #print(entrada)
    print("Error: Cadena rechazada")
  else:
    if columnas(entrada[0])!=0:
      reemplazo = tablita_parse[filas(pila[0])][columnas(entrada[0])]
      p=int(padres[0])
    else:
      continuar=False
      #print(pila)
      #print(entrada)
      print("Error: Cadena rechazada")
      break
    if reemplazo == "e":
      j=j+1
      h=j
      dot.node(str(h), "e")
      dot.edge(str(p),str(h))
      arbolito.ingresar_elemento(arbolito,"e",p,h)
      pila=pila[1:]
      padres=padres[1:]
      #print(pila)
      #print(entrada)
    else:
      #reemplazo=str(reemplazo)
      array_aux=reemplazo.split()
      pila = np.concatenate((array_aux,pila[1:]),axis=0)
      hijos = len(array_aux)
      aux.clear()
      for e in range(hijos):
        j=j+1
        if array_aux[e][0]==array_aux[e][0].upper():
          aux.append(j)
          arbolito.ingresar_elemento(arbolito,array_aux[e],p,j)
        else:
          arbolito.ingresar_elemento(arbolito,array_aux[e],p,j)
        h=j
        dot.node(str(h), array_aux[e])
        dot.edge(str(p),str(h))
      padres = np.concatenate((aux,padres[1:]),axis=0)
      #print(pila)
      #print(entrada)
  i=i+1
#print(dot.source)
#dot.view()
tree.recorrido_arbol(arbolito,pila_tokens)
