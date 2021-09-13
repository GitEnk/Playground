#TODO asking questions
#TODO Checking if answer is correct
#TODO check if we are at the end of the quiz

class QuizBrain:
    questionNumber = 0
    questionList = []

    def __init__(self, questionList):
        self.questionNumber = 0
        self.questionList = questionList


    def next_question(self):
        nq_index = self.questionNumber+1
        nq = self.questionList[self.questionNumber]
        nq_text = nq.text
        nq_str = f"Q.{nq_index}: {nq_text} (True/False)?: "
        self.questionNumber+=1
        return nq_str