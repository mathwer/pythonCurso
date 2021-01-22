from question_model import Question
from data import criar_questoes
from quiz_brain import QuizBrain
from ui import QuizInterface


questoes = criar_questoes()

quiz = QuizBrain(questoes)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

ui = QuizInterface(quiz)
