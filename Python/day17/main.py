from quiz_brain import QuizBrain
from question_model import Question
from data import question_data


ql = []
for q in question_data:
    qo = Question(q["text"], q["answer"])
    ql.append(qo)


qb = QuizBrain(ql)
while qb.still_has_questions():
    qb.next_question()