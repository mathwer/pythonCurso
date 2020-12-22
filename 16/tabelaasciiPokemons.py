from prettytable import PrettyTable

tabela = PrettyTable()

tabela.add_column('Pokemons', ['Pikachu', 'Charmander', 'Squirtle', 'Bulbasaur'])
tabela.add_column('Tipo', ['Elétrico', 'Fogo', 'Agua', 'Planta'])
tabela.align = 'c'

print(tabela)
