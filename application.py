import random

# Gera uma lista de 1 milhão de números inteiros aleatórios
num_integers = 1000000
random_integers = [random.randint(1, 1000000) for _ in range(num_integers)]

# Nome do arquivo a ser criado
file_name = "milhao_de_inteiros.txt"

# Escreve os números inteiros no arquivo
with open(file_name, "w") as file:
    for num in random_integers:
        file.write(str(num) + "\n")

print(f"Arquivo '{file_name}' criado com sucesso com {num_integers} inteiros.")
