# pedir para o usuario inserir a senha
num = int(input("qual a senha? "))
# criar a variavel com a senha correta
senha = 2002
# se o numero inserido for igual a senha correta, liberar o acesso
if num==senha:
    print("Acesso permitido")
# se qualquer outro numero for inserido bloquear acesso
else:
    print("Senha invalida")
