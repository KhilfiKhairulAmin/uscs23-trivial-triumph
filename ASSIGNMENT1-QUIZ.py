import random

questionsMCQ=[("Which movie was not directed by Tim Burton?", ["A. Snow White", "B. Pee-Wee’s Big Adventure", "C. Corpse Bride", "D. Big Fish"], "A"),
            ("What country is known to have the best quality tap water?", ["A. France", "B. Switzerland", "C. Germany", "D. Austria"], "B"),
            ("Riyadh is the capital of what Middle-Eastern country?", ["A. Yemen", "B. Iraq", "C. Saudi Arabia", "D. Syria"], "C"),
            ("What mountain is closest to the Moon?", ["A. Mount Everest", "B. Mount Chimborazo", "C. Nanga Parbat", "D. Mount Pandim"], "B"),
            ("What is the largest country in the world in terms of land area?", ["A. China", "B. Canada", "C. United States", "D. Russia"], "D")
]

questionsTF=[("Sharks are mammals.", "false"),
            ("The hummingbird egg is the world's smallest bird egg.", "true"),
            ("Bats are blind.", "false"), 
            ("An ant can lift 1,000 times its body weight.", "false"),
            ("The total length of the Great Wall of China adds up to 13,171 miles.", "true")
]


def quiz_Set1(questionsMCQ, questionsTF):
    score=0
    score+=Set1_MCQ(questionsMCQ, score)
    score+=Set1_TF(questionsTF, score)
    print("Quiz completed! Your score is:", score)
    
def Set1_MCQ(questionsMCQ, score):
    for count in range(1, 4, 1):
        questionsNo=random.sample(range(len(questionsMCQ)), len(questionsMCQ))
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

