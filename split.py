# Usando split em conjunto com \W+
# Vai separar as strings sempre que houver a ocorrencia de um simbolo e vai remove_lo
from re import split

print(split('\W+', 'Words, words , Words'))
print(split('\W+', "Word's words Words"))
print(split('\W+', 'On 12th Jan 2016, at 11:02 AM'))

# Splitting occurs at '12', '2016', '11', '02' only
print(split('\d+', 'On 12th Jan 2016, at 11:02 AM')) # separa quando há ocorrencia de um numero ou grupos de numeros de 0 a 9

import re
# Splitting will occurs only once, at '12', returned list will have length 2
print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM', 1))
''' Como se sabe o split devolve uma lista, aqui pedimos que a lista tenha tamanho 2, assim, ele faz a primeira separação
e o restante permanece junto, para que não passe do limite pedido'''

# 'Boy' and 'boy' will be treated same when flags = re.IGNORECASE
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here', flags = re.IGNORECASE))
''' Aqui a separação ocorre somente quando existem grupos ou uma letra de a até f, que sao removidas, incluindo maiusculas e minusculas,
fora isso, tudo é mantido junto, inclusive espaços em branco e sinais '''

print(re.split('[a-f]+', 'Aey, Boy oh boy, come here'))
''' Aqui somente as minusculas de a até f foram levadas em conta'''
