import pandas
from random import randint  # Será usado na parte de dicionários


numeros = [1, 2, 3]
numeros_quadrado = [n**2 for n in numeros]
# print(numeros_quadrado)

nome = 'Matheus'
letras = [letra for letra in nome]
# print(letras)

dobrado_range = [i*2 for i in range(1, 5)]
# print(dobrado_range)


# If na comprehension
nomes = ['Alex', 'Jorge', 'Maratania', 'João', 'Gabriel', 'Matheus', 'Bia']

nomes_pequenos = [nome for nome in nomes if len(nome) <= 4]
nomes_grandes_caps = [nome.upper() for nome in nomes if len(nome) > 4]
# print(nomes_pequenos)
# print(nomes_grandes_caps)


# ------ Dictionaries Comprehension -------------
# Funciona de forma parecida com a da lista
#  dict = {new_key:new_value, for (key, value) in dict.items() if test} -> É a forma mais completa, mas pode ser feito com listas, tuplas, range.

nomes = ['Alex', 'Jorge', 'Maratania', 'João', 'Gabriel', 'Matheus', 'Bia']


notas = {nome: randint(60, 100) for nome in nomes}

# print(notas)

nota_a = {nome: valor for (nome, valor) in notas.items() if valor >= 90}
# print(nota_a)

# ----------  Como iterar sobre um DataFrame do Pandas
nomes = ['Alex', 'Jorge', 'Maratania', 'João', 'Gabriel', 'Matheus', 'Bia']

alunos_dict = {
    'Nome': nomes,
    'Nota': [randint(60, 100) for i in range(len(nomes))]
}
notas_dataframe = pandas.DataFrame(alunos_dict)
print(notas_dataframe)

# Loop pelas linhas do DataFrame

for (indice, linha) in notas_dataframe.iterrows():
    print(linha.Nome)
