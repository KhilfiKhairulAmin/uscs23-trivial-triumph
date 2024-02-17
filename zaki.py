print("WELCOME TO THE PROGRAM!")

# Global variable to store current player's data
data = []

def signLog():
    print("1. Sign Up")
    print("2. Log In")
    print("3. Exit program")
    choose = input("\nEnter your choice:")
    if choose== '1':
        signUp()
    elif choose=='2':
        logIn()
    elif choose=='3': 
        exit()
    else:
        print("Invalid choice")
        signLog()

def signUp():
    authentication = open("myName.txt",'a')
    print("Sign up section\n----------------")
    name=input("Enter Username:")
    program=input("Enter program:")
    studentID = input("Enter student ID:")
    marks=0
    authentication.write(name + " " + program + " " + studentID + " " + str(marks) + "\n")
    authentication.close()
    print("SUCCESSFUL! \n PLEASE CONTINUE TO LOGIN")
    logIn()

def logIn():
    name = input("Enter your username:")
    program = input("Enter your program:")
    studentID = input("Enter your student ID:")
    authentication = open("myName.txt",'r')
    successLog = False
    for line in authentication:
        global data
        data = line.strip().split()
        if name == data[0] and program == data[1] and studentID == data[2]:
            print("Login Successful. \n PLEASE PROCEED")
            mainMenu()
            successLog = True
            break
    authentication.close()
    if not successLog:
        print("Login failed, please try again!")
        signLog()
        
def mainMenu():
    global data
    print("~"*20)
    print("~","Welcome,",data[0],"!","~")
    print("~","Highest score :",data[3],  "~")
    print("~"*20)
    print("\n")
    print("1. Play Quiz")
    print("2. Exit program")
    choose=input("\nEnter your choice:")
    if choose=='1':
        playQuiz()       
    elif choose=='2':
        exit()
    else:
        print("Invalid input!")
        mainMenu()

def playQuiz():
    import random
    print("="*55)
    print("\nThe answers are case sensitive. Enter 000 to go back to main menu.\n")
    print("="*55)
    global totalMark
    global totalCount
    global indicator 
    indicator=0
    totalCount=0
    totalMark=0
    randomList=[]

    for i in range(100):            #100 to make sure all numbers are not repeated in randomisation
        r=random.randint(1,11)
        if r not in randomList:
            randomList.append(r)
    
    for i in range(0,11):        
        if randomList[i]== 1:
            ques1()
        elif randomList[i]==2:
            ques2()
        elif randomList[i]==3:
            ques3()
        elif randomList[i]==4:
            ques4()
        elif randomList[i]==5:
            ques5()
        elif randomList[i]==6:
            ques6()
        elif randomList[i]==7:
            ques7()
        elif randomList[i]==8:
            ques8()
        elif randomList[i]==9:
            ques9()
        elif randomList[i]==10:
            ques10()
        elif randomList[i]==11:
            ques11()

    percentage=float((totalCount/11.0)*100)
    
    print("DONE!")
    wait=input("press any key to continue:")
    print("+"*30)
    print("Your marks are...",totalMark,"!")
    print("You got %0.2f"%percentage,"% of questions correct!")
    print("+"*30,"\n")
    
    global data
    data[3]=max(int(data[3]),totalMark)        #to update the highest score

    
    studentScore = []
    file = open("myName.txt","r")
    for line in file:
        info = line.strip().split()
        if len(info)>=4 and len(data)>=3:
            if info[0]==data [0] and info[1]==data[1] and info[2]==data[2]:
                info[3] = str(max(int(info[3]),totalMark))
        studentScore.append(info)

    
    file = open("myName.txt","w")
    for info in studentScore:
        file.write(" ".join(info)+ "\n")
        
    repeat = input("Do you want to repeat (yes/no): ")
    repeat.lower()
    
    if repeat == "yes":
        mainMenu()
    else:
        exit()

        
def ques1():
    global totalMark
    global indicator
    indicator+=1
    global totalCount
    print("_"*60)
    print("\nAnak apa yang selalu dipijak?     [15 marks] ")
    answer=input("\nAnswer : Anak ")
    if answer == "tangga":
        print("Correct!")
        totalMark+=15
        totalCount+=1
    elif answer == "000":
        mainMenu()

def ques2():
    global totalMark
    global totalCount
    global indicator
    indicator+=1
    print("_"*60)
    print("\nWhich keyword allows us to load a module in Python?     [5 marks] ")
    print("\nA. library")
    print("B. include")
    print("C. import")
    answer=input("\nAnswer : ")

    if answer == 'A':
        totalMark+=0
        print("Wrong :( ")
    elif answer == 'B':
        totalMark+=0
        print("Wrong :( ")
    elif answer == 'C':
        totalMark+=5
        totalCount+=1
        print("Correct!")
    elif answer == "000":
        mainMenu()
    else:
        print("Invalid input!")
        ques2()

def ques3():
    global totalMark
    global totalCount
    global indicator
    indicator+=1
    print("_"*60)
    print("\nWhich one from the following objects in Python is immutable?     [5 marks] ")
    print("\nA. list")
    print("B. tuple")
    print("C. dictionary")
    answer=input("\nAnswer : ")

    if answer == 'A':
        totalMark+=0
        print("Wrong :( ")
    elif answer == 'B':
        totalMark+=5
        totalCount+=1
        print("Correct!")
    elif answer == 'C':
        totalMark+=0
        print("Wrong :( ")
    elif answer == "000":
        mainMenu()
    else:
        print("Invalid input!")
        ques3()
    
def ques4():
    global totalMark
    global totalCount
    global indicator
    indicator+=1
    print("_"*60)
    print("\nGive the output of the following code. a = \"Python Quiz\" print(a[2:5])     [5 marks] ")
    answer=input("\nAnswer : ")

    if answer == "tho":
        totalMark+=5
        totalCount+=1
        print("Correct!")
    elif answer == "000":
        mainMenu()

def ques5():
    global totalMark
    global totalCount
    global indicator
    indicator+=1
    print("_"*60)
    print("\nWhich one of the following operators can perform floor division in Python?     [5 marks] ")
    print("\nA. //")
    print("B. %")
    print("C. ÷")
    answer=input("\nAnswer : ")

    if answer == 'A':
        totalMark+=5
        totalCount+=1
        print("Correct!")
    elif answer == 'B':
        totalMark+=0
        print("Wrong :( ")
    elif answer == 'C':
        totalMark+=0
        print("Wrong :( ")
    elif answer == "000":
        mainMenu()
    else:
        print("Invalid input!")
        ques5()

def ques6():
    global totalMark
    global indicator
    indicator+=1
    global totalCount
    print("_"*60)
    print("\nThe update function can add elements to the end of a list.     [5 marks] ")
    print("\nA. True")
    print("B. False")
    answer=input("\nAnswer : ")

    if answer == 'A' :
        totalMark+=0
        print("Wrong :( ")
    elif answer == 'B':
        totalMark+=5
        totalCount+=1
        print("Correct!")
    elif answer == "000":
        mainMenu()
    else:
        print("Invalid input!")
        ques6()
    
def ques7():
    global totalMark
    global totalCount
    global indicator
    indicator+=1
    print("_"*60)
    print("\nUsing the ________ statement, we can come out of a for loop in Python.     [5 marks] ")
    print("\nA. end")
    print("B. break")
    print("C. out")
    answer=input("\nAnswer : ")

    if answer == 'A' :
        totalMark+=0
        print("Wrong :( ")
    elif answer == 'B' :
        totalMark+=5
        totalCount+=1
        print("Correct!")
    elif answer == 'C':
        totalMark+=0
        print("Wrong :( ")
    elif answer == "000":
        mainMenu()
    else:
        print("Invalid input!")
        ques7()

def ques8():
    global totalMark
    global totalCount
    global indicator
    indicator+=1
    print("_"*60)
    print("\nWhich substances are involved in the opening and closing of the stomata? \n\nI Potassium ion \nII Sucrose \nIII Glucose \nIV Sodium ion             [15 marks] ")
    print("\n\nA. I and IV")
    print("B. I and II")
    print("C. III and IV")
    answer=input("\nAnswer : ")

    if answer == 'A':
        totalMark+=0
        print("Wrong :( ")
    elif answer == 'B' :
        totalMark+=15
        totalCount+=1
        print("Correct!")
    elif answer == 'C' :
        totalMark+=0
        print("Wrong :( ")
    elif answer == "000":
        mainMenu()
    else:
        print("Invalid input!")
        ques8()

def ques9():
    global totalMark
    global indicator
    indicator+=1
    global totalCount
    print("_"*60)
    print("\nWhich of the following is true about photosynthesis and respiration?      [10 marks] ")
    print("\nA. Photosynthesis involves a catabolic reaction while respiration involves an anabolism reaction.")
    print("B. Photosynthesis occurs in plant cells while respiration occurs in animal cells. ")
    print("C. Photosynthesis requires light while respiration does not require light")
    answer=input("\nAnswer : ")

    if answer == 'A' :
        totalMark+=0
        print("Wrong :( ")
    elif answer == 'B' :
        totalMark+=0
        print("Wrong :( ")
    elif answer == 'C':
        totalMark+=10
        totalCount+=1
        print("Correct!")
    elif answer == "000":
        mainMenu()
    else:
        print("Invalid input!")
        ques9()

def ques10():
    print("_"*60)
    global totalMark
    global indicator
    global totalCount
    indicator+=1
    print("\nWhich of the following is a micronutrient?      [10 marks] ")
    print("\nA. iron")
    print("B. magnesium  ")
    print("C. potassium ")
    answer=input("\nAnswer : ")

    if answer == 'A' :
        totalMark+=10
        totalCount+=1
        print("Correct!")
    elif answer == 'B' :
        totalMark+=0
        print("Wrong :( ")
    elif answer == 'C' :
        totalMark+=0
        print("Wrong :( ")
    elif answer == "000":
        mainMenu()
    else:
        print("Invalid input!")
        ques10()

def ques11():
    global totalMark
    global indicator
    global totalCount
    indicator+=1
    print("_"*60)
    print("\n□ Earth")
    print("□ Mercury")
    print("□ Jupiter")
    print("□ Saturn")
    print("□ Neptune")
    print("□ Venus")
    print("□ Uranus")
    print("□ Mars")
    print("\nWhat is the correct order of the planets?    [20 marks]")
    print("answer example: 2,3,7,1,8")
    answer=input("\nAnswer : ")

    if answer == "2,6,1,8,3,4,7,5":
        totalMark+=20
        totalCount+=1
        print("CORRECT!")
    elif answer == "000":
        mainMenu()
    else:
        print("Wrong answer, it's okay")
        totalMark+=0

signLog()
