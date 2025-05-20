#5

numero_digitado = int(input("Digite até que número quer verificar os primos: "))



contador = 1

contador_de_divisiveis_final = []

while contador <= numero_digitado:

    contador_de_divisiveis = []

    outro_contador = 1 
    while outro_contador <= numero_digitado:
        if contador % outro_contador == 0:
            contador_de_divisiveis.append(outro_contador)
            outro_contador += 1
        else:
            outro_contador+=1
            
    if contador_de_divisiveis == [1, contador]:
        contador_de_divisiveis_final.append(contador)

    contador+=1

print(contador_de_divisiveis_final)

