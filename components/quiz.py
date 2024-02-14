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
    score += quizEasy_MCQ(questionsMCQ, score)
    score += quizEasy_TF(questionsTF, score)
    score += quizEasy_Match(questionsMatch, score)

    if score>9:
        print("\nHARD MODE  (5marks)\n")
        score += quizHard_FIB(questionsFIB, score)
        score += quizHard_Sub(questionsSub, score)
    else:
        score += quizEasy2_MCQ(questionsMCQ, score)
        score += quizEasy2_TF(questionsTF, score)
        
    
    print("Quiz completed! Your score is:", score)

    
def quizEasy_MCQ(questionsMCQ: list, score):
    print("\nMutiple Choice Questions\n")
    
    for count in range(1, 4):              
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

        # Remove picked questions so it doesn't repeat
        for picked in sorted(questionsNo, reverse=True):
            questionsMCQ.pop(picked)

    return score


def quizEasy_TF(questionsTF, score):
    print("\nTRUE OR FALSE QUESTIONS\n")
    
    for count in range(1, 4):
        questionsNo = random.choices(range(len(questionsTF)), k=3)
        
        for index in questionsNo:
            question, answer = questionsTF[index]
            print(count, ".", question)
            userAnswer = input("Enter your answer <True/False>: ").lower()
            if userAnswer == answer:
                score += 2
                print("Correct!\n")
                break
            else:
                print("Incorrect.\n")
                break

        # Remove picked questions so it doesn't repeat
        for picked in sorted(questionsNo, reverse=True):
            questionsTF.pop(picked)
        
    return score


def quizEasy_Match(questionsMatch: list, score):   
    print("\nMACHING QUESTIONS\n")
    print("Match the statements <A,B,C> correctly to their answers <1,2,3>.\n")

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

    for j in range(3):
        answer = int(input(f"{char_map[j+1]} -> "))
        if answer == correct_answers[j]:
            print("Correct!")
            score += 2
        else:
            print("Incorrect!")

    # Remove picked question so it doesn't repeat
    questionsMatch.pop(questionsNo)
        
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

            
# quizEasy(questionsMCQ, questionsTF, questionsMatch, questionsFIB, questionsSub)
if __name__ == "__main__":
    quizEasy()
