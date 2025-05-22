#9

import random as rd


dict_de_candidatos = {1 : "Fulano", 2 : "ciclano", 3 : "beltrano", 4 : "zezin"}

votos_do_fulano = 0
votos_do_ciclano = 0
votos_do_beltrano = 0
votos_do_zezin = 0
votos_em_branco = 0
votos_em_nulo = 0


qtd_de_votos = 0

print("Nossos candidatos são os listados abaixo")
for chave, valor in dict_de_candidatos.items():
    print(f"{valor} número do candidato-> {chave}")

print("Para branco digite 5 e para nulo 6")

while qtd_de_votos < 100:
    voto = rd.randint(1, 6)
    if voto == 1:
        votos_do_fulano += 1
        qtd_de_votos += 1
    elif voto == 2:
        votos_do_ciclano += 1
        qtd_de_votos += 1
    elif voto == 3:
        votos_do_beltrano += 1
        qtd_de_votos += 1
    elif voto == 4:
        votos_do_zezin += 1
        qtd_de_votos += 1
    elif voto == 5:
        votos_em_branco += 1
        qtd_de_votos += 1
    elif voto == 6:
        votos_em_nulo += 1
        qtd_de_votos += 1
       
       
print(qtd_de_votos)



print(f"Fulano -> {votos_do_fulano}")

print(f"Ciclano -> {votos_do_ciclano}")

print(f"Beltrano -> {votos_do_beltrano}")

print(f"zezin -> {votos_do_zezin}")

print(f"branco -> {votos_em_branco}")

print(f"nulo -> {votos_em_nulo}")


porcentagem_de_votos_fulano = (votos_do_fulano / 100) * 100
porcentagem_de_votos_ciclano = (votos_do_ciclano / 100) * 100
porcentagem_de_votos_beltrano = (votos_do_beltrano / 100) * 100
porcentagem_de_votos_zezin = (votos_do_zezin / 100) * 100
porcentagem_de_votos_em_branco = (votos_em_branco / 100) * 100
porcentagem_de_votos_em_nulo = (votos_em_nulo / 100) * 100

print()
print(f"{porcentagem_de_votos_fulano:.2f}% -> porcentagem de votos do fulano ")
print(f"{porcentagem_de_votos_ciclano:.2f}% -> porcentagem de votos de ciclano ")
print(f"{porcentagem_de_votos_beltrano:.2f}% -> porcentagem de votos de beltrano ")
print(f"{porcentagem_de_votos_zezin:.2f}% -> porcentagem de votos em zezi ")
print(f"{porcentagem_de_votos_em_branco:.2f}% -> porcentagem de votos em branco ")
print(f"{porcentagem_de_votos_em_nulo:.2f}% -> porcentagem de votos em nulo ")
