#12

tabela_de_votos_da_marca = {"Design 1" : 1334, "Design 2" : 982, "Design 3" : 1751,
                            "Design 4" : 210, "Design 5" : 1811}


lista_de_votos = []
lista_de_nome = []

for chave, valor in tabela_de_votos_da_marca.items():
    lista_de_nome.append(chave)
    lista_de_votos.append(valor)

index_do_mais_votado = lista_de_votos.index(max(lista_de_votos))


print(f"O produto mais votado foi o produto {lista_de_nome[index_do_mais_votado]} com {max(lista_de_votos)} votos")


lista_de_porcentagens = []
for i in range(len(lista_de_nome)):
    lista_de_porcentagens.append(f"O produto {lista_de_nome[i]} representou {(lista_de_votos[i] * 100) / sum(lista_de_votos):.2f}%")


print(lista_de_porcentagens)