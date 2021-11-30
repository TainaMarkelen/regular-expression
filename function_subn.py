# Semelhante a função sub, mas essa é capaz de devolver o número de substiuições feitas
import re

print (re.subn('ub', '~*', 'Subject has Uber booked already'))
t = re.subn('ub', '~*', 'Subject has Uber booked already ub ub', flags = re.IGNORECASE)
print(t)
print(len(t))

# Dessa forma, devolve como se fosse um sub
print(t[0])