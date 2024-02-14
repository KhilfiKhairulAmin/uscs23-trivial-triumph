"""
Program: quiz.py
Author: Trivial Triumph Devs
Provide quiz algorithms for handling quiz logics and scoring
"""


from db import load_mcq_questions, load_tf_questions, load_matching_questions, load_FIB_questions, load_sub_questions

import random


def quizEasy():
    questionsMCQ   = load_mcq_questions()
    questionsTF    = load_tf_questions()
    questionsMatch = load_matching_questions()
    questionsFIB   = load_FIB_questions()
    questionsSub   = load_sub_questions()

    score = 0
    score += quizEasy_MCQ(questionsMCQ, number_of_questions=3)
    score += quizEasy_TF(questionsTF, number_of_questions=3)
    score += quizEasy_Match(questionsMatch, number_of_questions=3)

    if score > 9:
        print("\nHARD MODE  (5marks)\n")
        score += quizHard_FIB(questionsFIB, number_of_questions=3)
        score += quizHard_Sub(questionsSub, number_of_questions=3)
    else:
        score += quizEasy_MCQ(questionsMCQ, number_of_questions=2)
        score += quizEasy_TF(questionsTF, number_of_questions=2)
        score += quizEasy_Match(questionsMatch, number_of_questions=2)
        
    
    print("Quiz completed! Your score is:", score)

    
def quizEasy_MCQ(questionsMCQ: list, number_of_questions=3):
    print("\nMutiple Choice Questions\n")
    
    score = 0
    for count in range(1, number_of_questions+1):              
        questionsNo = random.randint(0, len(questionsMCQ)-1)

        question, options, answer = questionsMCQ[questionsNo]
        print(count, ".", question)
        for option in options:
            print(option)
        userAnswer = input("\nEnter your answer <A, B, C, D>: ").upper()
        if userAnswer == answer:
            score += 2
            print("Correct!\n")
        else:
            print("Incorrect.\n")

        # Remove picked questions so it doesn't repeat
        questionsMCQ.pop(questionsNo)

    return score


def quizEasy_TF(questionsTF: list, number_of_questions=3):
    print("\nTRUE OR FALSE QUESTIONS\n")
    
    score = 0
    for count in range(1, number_of_questions+1):
        questionsNo = random.randint(0, len(questionsTF)-1)
        
        question, answer = questionsTF[questionsNo]
        print(count, ".", question)
        userAnswer = input("Enter your answer <True/False>: ").lower()
        if userAnswer == answer:
            score += 2
            print("Correct!\n")
        else:
            print("Incorrect.\n")

        # Remove picked questions so it doesn't repeat
        questionsTF.pop(questionsNo)
        
    return score


def quizEasy_Match(questionsMatch: list, number_of_questions=3):   
    print("\nMATCHING QUESTIONS\n")

    score = 0
    for count in range(1, number_of_questions+1):
        print(f"{count}. Match the statements <A,B,C> correctly to their answers <1,2,3>.\n")

        questionsNo = random.randint(0, len(questionsMatch)-1)

        match = questionsMatch[questionsNo]
        correct_answers = [1, 2, 3]
        random.shuffle(correct_answers)

        question_map = {
            correct_answers[0]: match[0][1],
            correct_answers[1]: match[1][1],
            correct_answers[2]: match[2][1],
        }

        char_map = { 1: "A", 2: "B", 3: "C" }

        # Display matching boxes
        for i in range(3):
            print(f"%45s ({char_map[i+1]})\t({i+1}) %-45s" % (match[i][0], question_map[i+1]))
        print()

        correct = 0
        for j in range(3):
            answer = input(f"{char_map[j+1]} -> ")
            if answer == str(correct_answers[j]):
                print("Correct!")
                correct += 1
            else:
                print("Incorrect!")
        
        if correct == 3:
            score += 2
        elif correct == 2:
            score += 1

        # Remove picked question so it doesn't repeat
        questionsMatch.pop(questionsNo)
        
    return score


def quizHard_FIB(questionsFIB, number_of_questions=3):
    print("\nFILL IN THE BLANKS.\n")

    score = 0
    for count in range (1, number_of_questions+1):
        questionsNo = random.randint(0, len(questionsFIB)-1)

        question, answer = questionsFIB[questionsNo]
        print(count, ".", question)
        userAnswer = input("Answer: ").lower()
        if userAnswer == answer:
            score += 5
            print("Correct!!")
        else:
            print("Incorrect.")
        
        questionsFIB.pop(questionsNo)

        
    return score

def quizHard_Sub(questionsSub, number_of_questions=3):
    print("\nSUBJECTIVE QUESTIONS\n")

    score = 0
    for count in range (1, number_of_questions+1):
        questionsNo = random.randint(0, len(questionsSub)-1)

        question, answer = questionsSub[questionsNo]
        print(count, ".", question)
        userAnswer = input("Answer: ").lower()
        if userAnswer == answer:
            score += 5
            print("Correct!!")
        else:
            print("Incorrect.")

        questionsSub.pop(questionsNo)
        
    return score


if __name__ == "__main__":
    quizEasy()
