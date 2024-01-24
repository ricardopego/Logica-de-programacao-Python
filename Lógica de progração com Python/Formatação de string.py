"""
Interpolação de strings:

s - strings
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)
> - esquerda
< - direita
^ - centro
Sinal - + ou - 
Ex: 0> -100, 1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
