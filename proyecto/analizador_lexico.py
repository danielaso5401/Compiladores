import ply.lex as lex
import ply.yacc as yacc
#tipod de datos
tokens = ('num','soma','sub','multi','div','pari','parf','cori','corf','llai',
          'llaf','id','intei','dupla','val','corrente','binar','comment','equal',
          'corr','may','men','maye','mene','vaz','enquanto','sin','senao', 'senaosi',
          'ler','mostre','corpo','rec','dif','ret','coma','saida','dama')


t_intei= r'intei'
t_dupla= r'dupla'
t_val= r'val'
t_corrente= r'corrente'
t_binar= r'binar'
#funcio
t_vaz= r'vaz'
t_ret=r'volta'
#operacios
t_soma = r'\+'
t_sub = r'-'
t_div = r'/'
t_multi = r'\*'
t_coma = r','
t_dif=r'\<>'

t_mostre=r'mostre'
t_ler=r'ler'
t_corpo=r'corpo'
t_saida='saida'
t_dama='dama'
#condicionales
t_enquanto=r'enquanto'
t_sin='sin'
t_senao='senao'
t_senaosi='senao sim'

#comentarios
#t_com = r'\@'

#parentesis
t_pari = r'\('
t_parf = r'\)'
t_cori = r'\['
t_corf = r'\]'
t_llai = r'\{'
t_llaf = r'\}'
t_equal = r'\='
t_may=r'\>'
t_men=r'\<'
t_maye=r'\<='
t_mene=r'\>='


def t_num(t):
    r'[+-]?([1-9]\d*(\.\d*[1-9])?|0\.\d*[1-9]+)|\d+(\.\d*[1-9])?'
    t.value = float(t.value)    
    return t

    
def t_error(t):
	print ("caracter ilegal no declarado'%s'" % t.value[0])
	t.lexer.skip(1)
    
def t_id(t):
    r'[_][a-zA-Z0-9]*'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comment(t):
    r'\@'
    return t

    
def t_corr(t):
    r'[\'][a-zA-Z0-9@+(){}¿?¡! ]+[\']'
    return t

t_ignore  = ' \t'

def camb(cadena):
    listi=[]
    fp = open("example4.txt")
    cadena = fp.read()
    fp.close()
    lexer=lex.lex()
    lexer.input(cadena)
    while True:
     tok = lexer.token()
     if not tok: 
         break      # No more input
     listi.append(tok)
    return listi


lexer = lex.lex()
fp = open("example4.txt")
cadena = fp.read()
fp.close()


lexer.input(cadena)
cadena3=[]
cadena2=[]
while True:
 tok = lexer.token()
 if not tok: 
     break      # No more input
 cadena3.append(tok)
 cadena2.append(tok.type)



