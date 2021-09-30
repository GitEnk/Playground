#TODO asking questions
#TODO Checking if answer is correct
#TODO check if we are at the end of the quiz

class QuizBrain:
    question_number = 0
    question_list = []
    user_score = 0

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.user_score += 1
            print("Right!")
        else:
            print(f"Wrong, correct answer is {correct_answer}")

        print(f"Your score is {self.user_score}/{len(self.question_list)}")
