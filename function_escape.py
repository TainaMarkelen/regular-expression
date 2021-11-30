import re
# escape() returns a string with BackSlash '\', before every Non-Alphanumeric Character

# coloca barra sempre que há um simbolo que não é alfanumerico

# In 1st case only ' ', is not alphanumeric
print (re.escape("Isto é incrível demais"))
# In 2nd case, ' ', caret '^', '-', '[]', '\' are not alphanumeric
print (re.escape("I Asked what is this [a-9], he said \t ^WoW")) # \t devolve a tecla tab