# Module Regular Expressions(RE) specifies a set of strings(pattern) that matches it

# Importando o módulo de expressões regulares
import re

# Function compile(), Regular expressions are compiled into pattern objects
de_a_ate_e = re.compile('[a-e]') # a, b, c, d, e
# findall(), vai buscar na frase seguinte tudo o que contem em de_a_ate_e, veja
contem = de_a_ate_e.findall("Aye, said Mr. Gibenson Stark")
print(contem)

'''There are a total of 14 metacharacters and will be discussed as they follow into functions'''
''' Um deles é \, usado para baixar o significado especial do caracter, e é seguido dele, exemplos'''

# \d is equivalent to [0-9]
zero_a_nove = re.compile('\d')
print (zero_a_nove.findall("I went to him at 11 A.M. on 4th July 1886")) # printa todos os numeros contidos de 0 a 9 na frase

# \d+ will match a group on [0-9], group of one or greater size
grupos_de_numeros = re.compile('\d+')
print (grupos_de_numeros.findall("I went to him at 11 A.M. on 4th July 1886")) # printa os conjuntos contidos com numeros de 0 a 9

# \w is equivalent to [a-zA-Z0-9_]
todos_numeros_letras = re.compile('\w')
print (todos_numeros_letras.findall("He said * in some_lang.")) # printa todos os numeros, letras e o sinal de _

# \w+ matches to group of alphanumeric character
grupos_numeros_letras = re.compile('\w+')
print(grupos_numeros_letras.findall("I went to him at 11 A.M., he said *** in some_language.")) # printa os grupos, com letras e numeros

# \W matches to non alphanumeric characters
so_simbolo = re.compile('\W')
print(so_simbolo.findall("he said *** in some_language.")) # Encontra todos os simbolos, exceto _

# '*' replaces the no. of occurrence of a character
ocorre = re.compile('ab*') # o a é acompanhado por algum número de b's, começando por 0
print(ocorre.findall("ababbbabbaaby")) # vai printar sempre que aparecer a sozinho ou a acompanhado de b, seja quantos for

