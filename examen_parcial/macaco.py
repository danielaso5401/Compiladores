import ply.lex as lex

#tipod de datos
tokens = ('num','soma','sub','multi','div','pari','parf','cori','corf','llai',
          'llaf','id','val1','val2','val3','val4','val5','newline','comment','equal',
          'corr','may','men','maye','mene','val6','flutu','repet','si','sino', 'sinosi',
          'leer','imprimir','cuerpo','rec','dis','ret')


t_val1= r'intei'
t_val2= r'dupla'
t_val3= r'val'
t_val4= r'corrente'
t_val5= r'binar'
#funcio
t_val6= r'vaz'
t_ret=r'volta'
#operacios
t_soma = r'\+'
t_sub = r'-'
t_div = r'/'
t_multi = r'\*'

t_dis=r'\<>'

t_imprimir=r'mostre'
t_leer=r'ler'
t_cuerpo=r'corpo'

#condicionales
t_repet=r'enquanto'
t_si='sim'
t_sino='senao'
t_sinosi='senao sim'

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
def t_rec(t):
    r'verdade|falso'
    return t
    
def t_error(t):
	print ("caracter ilegal no declarado'%s'" % t.value[0])
	t.lexer.skip(1)
    
def t_id(t):
    r'[_][a-zA-Z0-9]*'
    return t

def t_newline(t):
    r'\s'
    return t
    #t.lexer.lineno += len(t.value)

def t_comment(t):
    r'\@'
    return t

def t_corr(t):
    r'[\'][a-zA-Z0-9@+(){}¿?¡! ]+[\']'
    return t

t_ignore  = ' \t'

lexer = lex.lex()
fp = open("example3.txt")
cadena = fp.read()
fp.close()

lexer.input(cadena)

while True:
 tok = lexer.token()
 if not tok: 
     break      # No more input
 print(tok)