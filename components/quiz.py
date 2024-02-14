import random

questionsMatch=[("What is the scientific term for the “little brain” at the base of the brain that coordinates movement and balance?", "cerebellum"),
                ("What is the chemical symbol for the element mercury?", "hg"),
                ("What is the official animal of Scotland?", "unicorn"),
                ("What animal is known to laugh and has been proven to have a sense of humor?", "rats"),
                ("What animal’s milk is pink?", "hippopotamus")
]

questionsFIB=[("Q", "Modern", "family"),
              ("Q", "Gilmore", "girls"),
              ("Q", "The Big Bang", "theory"),
              ("Q", "Mission:", "impossible")
              ("Q", "Grey's", "anatomy")
]

questionsSub=[("What is the only food that can never go bad?", "honey"),
              ("Who is Barbie’s little sister?", "skipper"),
              ("Anna, Elsa Kristoff and Olaf are all characters in what animated movie?", "frozen"),
              ("Which popular condiment was once sold as a medicinal cure for diarrhea?", "ketchup"),
              ("Which country do cities of Perth, Adelade & Brisbane belong to?", "australia"),
]


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
        correct_answer = next(f).strip()
        tf.append((question, correct_answer))

    return tf


def load_FIB_questions():
    f = open("FIB.txt")

    for _ in range (2):
        next(f)

    fib = []
    for _ in f:
        question = next(f).strip()
        correct_answer =                    #??????
        FIB_append((question, correct_answer))


questionsMCQ = load_mcq_questions()
questionsTF = load_tf_questions()



def quizEasy_Set1(questionsMCQ, questionsTF, questionMatch, questionsFIB, questionsSub):
    score=0
    score+=Set1_MCQ(questionsMCQ, score)
    score+=Set1_TF(questionsTF, score)
    score+=Set1_Match(questionsMatch, score)

    if score>9:
        score+=quizHard_FIB(questionsFIB, score)
        score+=quizHard_Sub(questionsSub, score)
    else:
        pass
    
    print("Quiz completed! Your score is:", score)
    
def Set1_MCQ(questionsMCQ, score):
    print("\nMutiple Choice Questions\n")
    
    for count in range(1, 4):                    #only 3 questions are displayed
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
    return score

def Set1_TF(questionsTF, score):
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
    return score

def Set1_Match(questionMatch, score):   #taktahu!!!
    print("\nMatching Questions\n")
    print("Match the statements <1,2,3> correctly to their answers <A,B,C>.")
    
    for count in range (1, 4, 1):
        questionsNo=random.choices(range(len(questionsTF)), k=3)
        for index in questionsNo:
            question, answer = questionsMatch[index]
            print(question, count, answer)
            userAnswer=input("(",count,") : ").upper()
            if userAnswer == answer:
                score+=2
                print("Correct!")
                break
            else:
                print("Incorrect.")
                break
    return score


def quizHard_FIB(questionsFIB, score):
    print("\nHARD MODE\n")
    print("Fill in the blanks.\n")

    for count in range (1, 4):
        questionsNo=random.choices(range(len(questionsFIB)), k=3)
        for index in questionsNo:
            question, answer = questionsFIB[index]
            print(count, ".", question, "_" * len(answer))
            userAnswer = input("Answer: ").lower()
            if userAnswer == answer:
                score+=5
                print("Correct!!")
                break
            else:
                print("Incorrect.")
                break
    return score

def quizHard_Sub(questionsSub, score):
    print("\nSubjective Questions\n")

    for count in range (1, 4):
        questionsNo = random.choices(range(len(questionsFIB)), k=3)
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
    return score
    
            

quizEasy_Set1(questionsMCQ, questionsTF, questionsMatch, questionsFIB, questionsSub)

