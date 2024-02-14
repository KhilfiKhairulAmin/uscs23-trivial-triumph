"""
Program: quiz.py
Author: Trivial Triumph Devs
Provide quiz algorithms for handling quiz logics and scoring
"""


from components.db import load_mcq_questions, load_tf_questions, load_matching_questions, load_FIB_questions, load_sub_questions

import random


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

