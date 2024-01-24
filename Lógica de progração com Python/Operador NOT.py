senha = input('Senha: ')

# not é usado para dizer que se o usuário não digitar nada ele executa o if mesmo assim.
# Ele troca o valor da variável ex: (not True será igual a False).
if not senha:
    print('Senha incorreta')