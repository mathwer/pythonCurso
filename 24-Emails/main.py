# TODO: Create a letter using starting_letter.docx
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./24-Emails/Input/Names/invited_names.txt") as lista_nomes:
    convidados = lista_nomes.readlines()

with open("./24-Emails/Input/Letters/starting_letter.docx") as convite_inicial:
    conteudo = convite_inicial.read()

    for nome in convidados:
        nome_strip = nome.strip()
        convite_novo = conteudo.replace('[name]', nome_strip)

    # Como a princípio, os arquivos não existem, eles serão criados peloo python
        with open(f'./24-Emails/Output/ReadyToSend/convite_{nome_strip}.docx', 'w') as convite_final:
            convite_final.write(convite_novo)
