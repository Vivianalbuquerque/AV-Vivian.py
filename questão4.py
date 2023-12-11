# pedir DDD
ddd = int(input("Qual o DDD você quer detectar? "))
# comparando o numero inserido com os DDDs da tabela
if ddd == 61:
    print("O DDD 61 é de Brasilia ")
elif ddd == 71:
    print("O DDD 71 é de Salvador ")
elif ddd == 11:
    print("O DDD 11 é de Sâo paulo ")
elif  ddd == 21:
    print("O DDD 21 é de Rio de Janeiro ")
elif  ddd == 32:
    print("O DDD 32 é de Juiz de Fora ")
elif  ddd == 19:
    print("O DDD 19 é de Campinas ")
elif  ddd == 27:
    print("O DDD 27 é de Vitoria ")
elif  ddd == 31:
    print("O DDD 31 é de Belo Horizonte ")
# se o DDD inserido não ser igual a nem um da tabela, exibir não detectado
else:
    print("DDD não detectado")
# fim do programa