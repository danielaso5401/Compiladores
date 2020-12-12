import parser2
import numpy as np
from collections import deque  
class simbolo:
    def __init__(self, t, lex, tp, pos, lin, scope):
        self.token = t
        self.lexema = lex
        self.tipo = tp
        self.posicion = pos
        self.linea = lin
        self.scope = scope

class tipos:
    def __init__(self, t, lex, tp, pos, lin,atributo, scope):
        self.token = t
        self.lexema = lex
        self.tipo = tp
        self.posicion = pos
        self.linea = lin
        self.scope = scope
        self.atributo = atributo


n = 0
es_yoyo = False
tabla_de_simbolos = []
tabla_de_atributos = []
#parser2.tree.ejecutarProfundidadPrimero(parser2.arbolito)
funcion_actual = None
funcion_actual_aux = None


        


def insertar_parametros(arbol):
    if arbol.elemento == "PAR":
        tabla_de_simbolos.append(
            simbolo(arbol.hijos[1].token, arbol.hijos[1].token.value, "variable", arbol.hijos[1].token.lexpos,
                    arbol.hijos[1].token.lineno, funcion_actual))
    elif arbol.elemento == "FUN_S":
        tabla_de_simbolos.append(
            simbolo(arbol.hijos[1].token, arbol.hijos[1].token.value, "vaz", arbol.hijos[1].token.lexpos,
                    arbol.hijos[1].token.lineno, funcion_actual))
    elif arbol.elemento=="PARAM_DEF" and arbol.hijos[0].elemento!="e":
        tabla_de_simbolos.append(
            simbolo(arbol.hijos[2].token, arbol.hijos[2].token.value, "variable", arbol.hijos[2].token.lexpos,
                    arbol.hijos[2].token.lineno, funcion_actual))
    elif arbol.elemento=="VAL_S" and  arbol.hijos[0].elemento!="TYPE":
        tabla_de_simbolos.append(
            simbolo(arbol.hijos[0].token, arbol.hijos[0].token.value, "ret_asi", arbol.hijos[0].token.lexpos,
                    arbol.hijos[0].token.lineno, funcion_actual))
    elif arbol.elemento=="VAL_S" and  arbol.hijos[0].elemento=="TYPE":
        tabla_de_simbolos.append(
            simbolo(arbol.hijos[1].token, arbol.hijos[1].token.value, "variable", arbol.hijos[1].token.lexpos,
                    arbol.hijos[1].token.lineno, funcion_actual))
    
    for x in arbol.hijos:
        insertar_parametros(x)

def repetido(r):
    for i in reversed(r):
        if i.tipo=="ret_asi":
            for j in reversed(tabla_de_simbolos):
                if i.tipo == "variable" and i.lexema==j.lexema:
                    return True
def comp():
    arr=[]
    for x in reversed(tabla_de_simbolos):
        if x.tipo == "ret_asi":
            arr.append(x)
    parser2.ver_error(1)
    
                    
def comprobar_existencia_llamada():

    for x in reversed(tabla_de_simbolos):
        if x.tipo == "ret_asi":
            for y in reversed(tabla_de_simbolos):
                if y.tipo=="variable" and y.lexema==x.lexema:
                    print("correcto")
                """"elif repetido(y.lexema)==0:
                    print("error") #tenemos que arreglarlo
"""

                    

     

def insertar_tipo(arbol):
    
    if arbol.elemento == "PAR":
        tabla_de_atributos.append(
            tipos(arbol.hijos[1].token, arbol.hijos[1].token.value, "variable", arbol.hijos[1].token.lexpos,
                    arbol.hijos[1].token.lineno,arbol.hijos[0].hijos[0].token.value ,funcion_actual))
    elif arbol.elemento=="PARAM_DEF" and arbol.hijos[0].elemento!="e":
        tabla_de_atributos.append(
            tipos(arbol.hijos[2].token, arbol.hijos[2].token.value, "variable", arbol.hijos[2].token.lexpos,
                    arbol.hijos[2].token.lineno,arbol.hijos[1].hijos[0].token.value ,funcion_actual))
    elif arbol.elemento=="VAL_S" and  arbol.hijos[0].elemento!="TYPE" and parser2.tree.ejecutarAnchoPrimero(parser2.arbolito)!=1:
        tabla_de_atributos.append(
            tipos(arbol.hijos[0].token, arbol.hijos[0].token.value, "ret_asi", arbol.hijos[0].token.lexpos,
                    arbol.hijos[0].token.lineno,"asignacion/retorno" ,funcion_actual))
    elif arbol.elemento=="VAL_S" and  arbol.hijos[0].elemento=="TYPE":
        tabla_de_atributos.append(
            tipos(arbol.hijos[1].token, arbol.hijos[1].token.value, "variable", arbol.hijos[1].token.lexpos,
                    arbol.hijos[1].token.lineno,arbol.hijos[0].hijos[0].token.value,funcion_actual))
    elif arbol.elemento=="ASI_S" and arbol.hijos[0].elemento=="equal":
        tabla_de_atributos.append(
            tipos(arbol.hijos[1].hijos[0].hijos[0].hijos[0].token, arbol.hijos[1].hijos[0].hijos[0].hijos[0].token.value, "asigna_variables", arbol.hijos[1].hijos[0].hijos[0].hijos[0].token.lexpos,
                    arbol.hijos[1].hijos[0].hijos[0].hijos[0].token.lineno,"asignacion",funcion_actual))
        
    for x in arbol.hijos:
        insertar_tipo(x)
def comprobar_asignacion():
    for x in reversed(tabla_de_atributos):
        if x.tipo == "asignacion/retorno":
            for y in reversed(tabla_de_atributos):
                if y.tipo=="variable" and y.lexema==x.lexema:
                    print("correcto")
                """else:
                    print("error")""" #tenemos que arreglarlo
        
insertar_parametros(parser2.arbolito)
for i in range(len(tabla_de_simbolos)):    
   print(tabla_de_simbolos[i].token,tabla_de_simbolos[i].tipo)
comprobar_existencia_llamada()
#comp()
insertar_tipo(parser2.arbolito)
for i in range(len(tabla_de_atributos)):    
   print(tabla_de_atributos[i].token,tabla_de_atributos[i].atributo)

comprobar_asignacion()
marca=False
def chek_val():
   for i in range(len(tabla_de_atributos)):
       if tabla_de_atributos[i].atributo=="asignacion":
           var=tabla_de_atributos[i-1].lexema
           for j in range(len(tabla_de_atributos)):
               if var==tabla_de_atributos[j].lexema and tabla_de_atributos[j].atributo!="asignacion retorno":
                   if tabla_de_atributos[i].token=="num" and tabla_de_atributos[j].atributo=="intei":
                       print("accion correcta")
                       marca=True
                   if tabla_de_atributos[i].token=="corrente" and tabla_de_atributos[j].atributo=="corrente":
                       print("accion correcta")
                       marca=True
                   if tabla_de_atributos[i].token=="dupla" and tabla_de_atributos[j].atributo=="dupla":
                       print("accion correcta")
                       marca=True
                   else:
                       print("error el dato asignado no es del tipo")
contenedor_asig=[]
contenedor_mostar=[]

def conte_valores(arbol):

    if arbol.elemento=="MOST_S":
        contenedor_mostar.append(arbol.hijos[2].hijos[0].token.value)
    #if arbol.elemento=="ASI_S":
        #contenedor_asig.append(arbol.hijos[1].hijos[0].hijos[0].hijos[0].token.value)
    for x in arbol.hijos:
        conte_valores(x)                 

if(marca!=True):
    chek_val()
    
def almacenar(x):
  temp = type(x)is int
  return temp
    
print("---------------------")
for i in range(len(tabla_de_atributos)):
    if tabla_de_atributos[i].atributo=="asignacion/retorno" and  tabla_de_atributos[i+1].atributo=="asignacion":
        pair=(tabla_de_atributos[i].lexema,tabla_de_atributos[i+1].lexema)
        contenedor_asig.append(pair)

conte_valores(parser2.arbolito)
print("---------------------")
print(contenedor_asig)
print(contenedor_mostar)
      
f = open ("code.s", "w")
f.write(".data\n")
if len(contenedor_mostar)>0:
    for i in range(len(contenedor_mostar)):
        f.write("out_string"+str(i))
        f.write(": .asciiz") 
        f.write(r'"')
        f.write(str(contenedor_mostar[i]))
        f.write(r'"')
        f.write("\n")
f.write(".text\n")
f.write("main:\n")
if len(contenedor_mostar)>0:
    for i in range(len(contenedor_mostar)):
        f.write("li $v0, 4 \n")
        f.write("la $a0, out_string"+str(i)+"\n") 	
        f.write("syscall \n")
if len(contenedor_asig)>0:
    for i in range(len(contenedor_asig)):

        f.write("li " +"$t"+str(i+1)+", "+str(int(contenedor_asig[i][1])) +"\n")

f.write("jr $ra\n")
f.close()
f=open("code.s")
f.read()          