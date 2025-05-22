#9 

gabarito = {1 : "D", 2 : "A", 3 : "C", 4 : "B", 5 : "A", 6 : "D",
           7 : "C", 8 : "C", 9 : "A", 10 : "B"}


gabarito_do_aluno = []

contador = 1
while contador <= 10: 
    questao_respondida = input(f"Ola digite aqui a opçãoq que marco na questão {contador}")
    questao_respondida = questao_respondida.upper()
    if questao_respondida == "A" or questao_respondida == "B" or questao_respondida == "C" or questao_respondida == "D":
        gabarito_do_aluno.append(questao_respondida)
        contador+=1
    else:
        print("Digite um valor válido de A a D")
        continue


pontuacao_aluno = 0
questoes_erradas = 0
for i in range(len(gabarito_do_aluno)):
    if gabarito_do_aluno[i] == gabarito.__getitem__(i+1):
        pontuacao_aluno += 1
    else:
        questoes_erradas += 1



print(f"aluno voce tirou {pontuacao_aluno}, errou {questoes_erradas} questoes")