#Faz as perguntas, checa a respostas e checa se está no final do quiz.

class CerebroQuiz():
    def __init__(self, lista_de_questoes):
        self.lista_de_questoes = lista_de_questoes
        self.numero_pergunta = 0
        self.placar = 0 

    def ainda_tem_perguntas(self):
        return self.numero_pergunta < len(self.lista_de_questoes)


    def proxima_questao(self):
        pergunta_atual = self.lista_de_questoes[self.numero_pergunta]
        questao = pergunta_atual.texto
        self.numero_pergunta += 1
        resposta = input(f'Q.{self.numero_pergunta}: {questao} (true / false): ')
        if resposta.lower() == pergunta_atual.resposta.lower():
            print('Resposta Correta!')
            self.placar += 1 
        else:
            print('Resposta errada :/')
        
        print(f'A resposta correta era: {pergunta_atual.resposta}.' )
        print(f'Seu placar atual é: {self.placar}/{self.numero_pergunta}')
        print('')
        


    # def checar_resposta(self)
    #     if resposta == self.pergunta_atual.resposta:
    #         placar += 1
        
        

