#Esse modo utiliza um banco de perguntas já criadas pelo curso.

from question_model import Questao
from data import question_data
from quiz_brain import CerebroQuiz

banco_perguntas = []

for pergunta in question_data:
    texto_pergunta = pergunta['text']
    resposta_pergunta = pergunta['answer']
    pergunta_nova = Questao(texto_pergunta, resposta_pergunta)
    banco_perguntas.append(pergunta_nova)

quiz = CerebroQuiz(banco_perguntas)

while quiz.ainda_tem_perguntas():
    quiz.proxima_questao()
    
else:
    print("Você terminou o quiz!")
    print(f'Seu placar final foi {quiz.placar}/{quiz.numero_pergunta}')

