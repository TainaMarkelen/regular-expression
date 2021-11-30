# se trata de substituição
import re

print(re.sub('ub', '~*' , 'Subject has Uber booked already', flags = re.IGNORECASE))
''' Substituimos sempre que aparece 'ub' por '~*', ignorando se é maiúscula ou minuscula '''

print(re.sub('ub', '~*' , 'Subject has Uber booked already'))
''' Aqui tratamos apenas as minúsculas, com a ausencia do flags = re.IGNORECASE '''

# As count has been given value 1, the maximum times replacement occurs is 1
print(re.sub('ub', '~*' , 'Subject has Uber booked already', count=1, flags = re.IGNORECASE))
''' Aqui pedimos para que a substituição seja feita apenas uma vez '''

# 'r' before the patter denotes RE, \s is for start and end of a String.
print(re.sub(r'\sAnd\s', ' & ', 'Baked Beans And Spam', flags = re.IGNORECASE))
''' Nesse caso, a gente delimita a string que deve ser substituída, apenas a palavra and, completa, vai ser substituida,
se ocorrer outro caso de and, no meio de alguma palavra, não ocorrerá a substituição, exemplo abaixo: '''
print(re.sub(r'\sEle\s', '#', ' ele foi eleito, mas protestei no elenao', flags = re.IGNORECASE))
''' Não houve substituição em 'elenao', uma observação é que nesse caso, 'ele' deve ter espaço antes e depois, para ser substituido '''

