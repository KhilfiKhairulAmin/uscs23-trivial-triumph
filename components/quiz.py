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


def load_matching_questions():
    f = open("matching.txt")
        
    for _ in range(3):
        next(f)

    matchings = []
    for _ in f:  # Read three questions and answers
        m = []
        for _ in range(3):
            question, correct_answer = next(f).strip().split(" -> ")
            m.append((question, correct_answer))
        matchings.append(m)

    return matchings


def load_FIB_questions():
    f = open("FIB.txt")

    for _ in range (2):
        next(f)

    FIB = []
    for _ in f:
        question = next(f).strip()
        correct_answers = next(f).strip().split(",")
        FIB.append((question, correct_answers))

    return FIB


def load_sub_questions():
    f = open("sub.txt")

    for _ in range (2):
        next(f)

    sub = []
    for _ in f:
        question = next(f).strip()
        correct_answer = next(f).strip()
        sub.append((question, correct_answer))

    return sub



questionsMCQ = load_mcq_questions()
questionsTF = load_tf_questions()
questionsMatch = load_matching_questions()
questionsFIB = load_FIB_questions()
questionsSub = load_sub_questions()



def quizEasy(questionsMCQ, questionsTF, questionsMatch, questionsFIB, questionsSub):
    score=0
    score+=quizEasy_MCQ(questionsMCQ, score)
    score+=quizEasy_TF(questionsTF, score)
    score+=quizEasy_Match(questionsMatch, score)

    if score>9:
        print("\nHARD MODE  (5marks)\n")
        score+=quizHard_FIB(questionsFIB, score)
        score+=quizHard_Sub(questionsSub, score)
    else:
        score+=quizEasy2_MCQ(questionsMCQ, score)
        score+=quizEasy2_TF(questionsTF, score)
        
    
    print("Quiz completed! Your score is:", score)

    
def quizEasy_MCQ(questionsMCQ, score):
    print("\nMutiple Choice Questions\n")
    
    for count in range(1, 4):                    
        questionsNo=random.choices(range(len(questionsMCQ)), k=3)
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

            del questionsMCQ[index]        #doesnt same question repeated at next set
            break

    return score

def quizEasy_TF(questionsTF, score):
    print("\nTRUE OR FALSE QUESTIONS\n")
    
    for count in range(1, 4, 1):
        questionsNo=random.choices(range(len(questionsTF)), k=3)
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

            del questionsTF[index]        
            break
        
    return score

def quizEasy_Match(questionsMatch, score):   
    print("\nMatching Questions\n")
    print("Match the statements <1,2,3> correctly to their answers <A,B,C>.")
    
    for count in range (1, 4, 1):
        questionsNo=random.choices(range(len(questionsMatch)), k=3)
        for index in questionsNo:
            question, answer = questionsMatch[index]
            print(question, count, answer)
            userAnswer=input("Answer: ").upper()
            if userAnswer == answer:
                score+=2
                print("Correct!")
                break
            else:
                print("Incorrect.")
                break

            del questionsMatch[index]        
            break
        
    return score


def quizHard_FIB(questionsFIB, score):
    print("\nFill in the blanks.\n")

    for count in range (1, 4):
        questionsNo=random.choices(range(len(questionsFIB)), k=3)
        for index in questionsNo:
            question, answer = questionsFIB[index]
            print(count, ".", question)
            userAnswer = input("Answer: ").lower()
            if userAnswer == answer:
                score+=5
                print("Correct!!")
                break
            else:
                print("Incorrect.")
                break

            del questionsFIB[index]        
            break
        
    return score

def quizHard_Sub(questionsSub, score):
    print("\nSubjective Questions\n")

    for count in range (1, 4):
        questionsNo = random.choices(range(len(questionsSub)), k=3)
        for index in questionsNo:
            question, answer = questionsSub[index]
            print(count, ".", question)
            userAnswer = input("Answer: ").lower()
            if userAnswer == answer:
                score+=5
                print("Correct!!")
                break
            else:
                print("Incorrect.")
                break

            del questionsSub[index]        
            break
        
    return score


def quizEasy2_MCQ(questionsMCQ, score):
    print("\nMutiple Choice Questions\n")
    
    for count in range(1, 3):                    
        questionsNo=random.choices(range(len(questionsMCQ)), k=2)
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

def quizEasy2_TF(questionsTF, score):
    print("\nTRUE OR FALSE QUESTIONS\n")
    
    for count in range(1, 3):
        questionsNo=random.choices(range(len(questionsTF)), k=2)
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

            

quizEasy(questionsMCQ, questionsTF, questionsMatch, questionsFIB, questionsSub)

