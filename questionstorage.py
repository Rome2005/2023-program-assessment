from random import randint

class QuestionStorage:
    def __init__(self):
        self.questions = self.generate_easy_questions()

    def generate_easy_questions(self):
        questions = []
        for num1 in range(1, 11):  # Generate questions for 1 to 10
            for num2 in range(1, 13):  # Generate questions for 1 to 12 times tables
                question = f"{num1} x {num2}"
                answer = num1 * num2
                questions.append((question, answer))
        return questions

    def get_question(self):
        if len(self.questions) > 0:
            return self.questions.pop(0)
        else:
            return None

    def get_remaining_questions(self):
        return len(self.questions)
