import pandas

nato = pandas.read_csv(
    '26-List_Comprehension/nato_phonetic_alphabet.csv')


# dict_nato = nato.set_index('letter')['code'].to_dict()

dict_nato = {codigo[0]: codigo[1]
             for (indice, codigo) in nato.iterrows()}

print(dict_nato)


def para_nato():
    palavra = input('Diga uma palavra: ').upper()
    try:
        lista_nato = [dict_nato[letra] for letra in palavra]

    except KeyError:
        print('Desculpe, apenas letras do alfabeto, por favor')
        para_nato()

    else:
        print(lista_nato)


para_nato()
