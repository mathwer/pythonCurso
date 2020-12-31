numeros = [1, 2, 3]
numeros_quadrado = [n**2 for n in numeros]
print(numeros_quadrado)

nome = 'Matheus'
letras = [letra for letra in nome]
print(letras)

dobrado_range = [i*2 for i in range(1, 5)]
print(dobrado_range)


# If na comprehension
nomes = ['Alex', 'Jorge', 'Maratania', 'João', 'Gabriel', 'Matheus', 'Bia']

nomes_pequenos = [nome for nome in nomes if len(nome) <= 4]
nomes_grandes_caps = [nome.upper() for nome in nomes if len(nome) > 4]
print(nomes_pequenos)
print(nomes_grandes_caps)
