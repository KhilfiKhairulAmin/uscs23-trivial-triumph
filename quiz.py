import random


def load_mcq_questions():
    f = open("mcq.txt")

    # Skip the first 6 lines which are the sample questions of the file
    for _ in range(6):
        next(f)  # Skip the line

    mcq = []
    for _ in f:
        question = next(f).strip()
        answers = []
        answers.append(f"A. {next(f).strip()}")
        answers.append(f"B. {next(f).strip()}")
        answers.append(f"C. {next(f).strip()}")
        answers.append(f"D. {next(f).strip()}")
        correct_answer = next(f).strip()
        mcq.append((question, answers, correct_answer))

    return mcq


def load_tf_questions():
    f = open("tf.txt")

    # Skip the first 2 lines which are the sample questions of the file
    for _ in range(2):
        next(f)  # Skip the line

    tf = []
    for _ in f:
        question = next(f).strip()
        correct_answer = "true" if next(f).strip() == "T" else "false"
        tf.append((question, correct_answer))

    return tf


questionsMCQ = load_mcq_questions()

questionsTF = load_tf_questions()


def quiz_Set1(questionsMCQ, questionsTF):
    score=0
    score+=Set1_MCQ(questionsMCQ, score)
    score+=Set1_TF(questionsTF, score)
    print("Quiz completed! Your score is:", score)
    
def Set1_MCQ(questionsMCQ, score):
    for count in range(1, 4, 1):
        questionsNo = random.choices(range(len(questionsMCQ)), k=3)
        for index in questionsNo:
            question, options, answer = questionsMCQ[index]
            print(count, ".", question)
            for option in options:
                print(option)
            userAnswer = input("\nEnter your answer <A, B, C, D>: ").upper()
            if userAnswer == answer:
                score += 2
                print("Correct!\n")
                break
            else:
                print("Incorrect.\n")
                break
    return score

def Set1_TF(questionsTF, score):
    print("\nTRUE OR FALSE QUESTIONS\n")
    for count in range(1, 4, 1):
        questionsNo=random.sample(range(len(questionsTF)), len(questionsTF))
        for index in questionsNo:
            question, answer = questionsTF[index]
            print(count, ".", question)
            userAnswer=input("Enter your answer <True/False>: ").lower()
            if userAnswer == answer:
                score += 2
                print("Correct!\n")
                break
            else:
                print("Incorrect.\n")
                break
    return score

quiz_Set1(questionsMCQ, questionsTF)

