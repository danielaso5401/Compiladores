cadena = raw_input()
c1='\s'
c2=r'\t'
r=len(cadena)
i=0
while(i<r):
    if(cadena[i]==c1[0] and cadena[i+1]==c1[1]):
        print("aceptado\n")
    if(cadena[i]==c2[0] and cadena[i+1]==c2[1]):
        print("aceptado_2\n")
    if(cadena[i]==' '):
        print("aceptado_3\n")
    i=i+1
print("hola\nadie")