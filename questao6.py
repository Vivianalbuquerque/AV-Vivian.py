#crio uma lista e uma lista para numeros positivos
lista = []
positivos = []
#para não perder tempo usei um range para repitir
for i in range(0,7):
    val = float(input("Digite um valor: "))
    #adiciono os valores a lista 
    lista.append(val)
#identifico os positivos
for val in lista:
    if val > -1 :
        #adiciono a variavel
        positivos.append(val)
#uso a função len pra mostrar a quantidade de numeros positivos]
quantidade= len (positivos)
 
# divido e obtenho a media dos numeros positivos 
media = (sum(positivos)) / quantidade

#exibo o resultado da media e quantidade de numeros positivos
print(f"tem {quantidade}numeros\n valores positivos{positivos}")
print(f"A media dos numeros positivos é {media}")


