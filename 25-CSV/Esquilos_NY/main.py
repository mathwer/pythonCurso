import pandas

esquilos = pandas.read_csv(
    '2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

esquilos_marrons = esquilos[esquilos['Primary Fur Color'] == 'Cinnamon']
esquilos_pretos = esquilos[esquilos['Primary Fur Color'] == 'Black']
esquilos_cinza = esquilos[esquilos['Primary Fur Color'] == 'Gray']

esquilos_dict = {
    'Cor dos Esquilos': ['Marrom', 'Preto', 'Cinza'],
    'Quantidade': [len(esquilos_marrons), len(esquilos_pretos), len(esquilos_cinza)]
}

esquilos_data = pandas.DataFrame(esquilos_dict)

esquilos_data.to_csv('Quantidade_por_cor.csv')
