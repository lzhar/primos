#6

import re


print("""Digite a data no modelo informado
            02/12/2024 informe dia/mes/ano""")

validacao_data = re.compile(r"(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/[0-9]{4}")

minha_data = input("digite aqui a data: ")

if validacao_data.match(minha_data):
    print("Data valida!")
else:
    print("Data não valida")