

# with open('./weather_data.csv') as data_tempo:
#     data = data_tempo.readlines()
#     tempo_formatado = []
#     for tempo in data:
#         tempo = tempo.strip()
#         tempo_formatado.append(tempo)

# print(tempo_formatado)

# import csv

# with open('weather_data.csv') as data_tempo:
#     data = csv.reader(data_tempo)
#     temperaturas = []
#     for linha in data:
#         if linha[1] != 'temp':
#             temperaturas.append(linha[1])
#
# print(temperaturas)

import pandas

data = pandas.read_csv('weather_data.csv')
print(data['temp'])

data_dict = data.to_dict()
print(data_dict)

temperaturas = data['temp'].to_list()
print(temperaturas)

#media = sum(temperaturas)/len(temperaturas)


# Não funciona usando a variável temperatura. Pois é uma lista e não um objeto Series do Pandas.
media = data['temp'].mean()
print(media)

temp_max = data['temp'].max()

# Pegando linhas inteira a partir de uma condição
print(data[data.temp == temp_max])

segunda_feira = data[data.day == 'Monday']
print(segunda_feira.temp)


# Create a Dataframe

data_dict = {
    'alunos': ['Ana', 'Bia', 'Joao', 'Lucas', 'Sofia', 'Vitor'],
    'notas': [8, 10, 9, 7, 6, 10]
}

data_alunos = pandas.DataFrame(data_dict)
print(data_alunos)

data_alunos.to_csv('data_alunos.csv')
# Se o arquivo não existe, ele será criado, como as funções read.
