""""
DocString
escrevo oq eu quiser entre as aspas e posso pular linha, o interpretador do python lê isso.
DOCSTRING NÃO É COMENTÁRIO

"""

''' DocString também, porém com aspas simples '''

# Permite escrever um comentário, somente na mesma linha


# \r\n -> CRLF
#\n -> LF

print(12, 34, 1011, sep="-", end='#')
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-', end='\n')