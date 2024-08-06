## Python Quiz Game By Team Achievers ##

## Introductory Lines

print("""

Welcome to the Computer Quiz Game by Team Achievers
""")

## User Prompts and Explaination of Rules to the user

print("""

Each Correct Response shall award you 10 Point,
while Incorrect Responses give -1.5 Points,

You may incorrect spellings are considered to be wrong as well!
Its not case sensitive

Total 5 Questions
Total Points 50
""")

## Initialize the user score

user_score = 0.0
print("Your innitial Score is: ", user_score)

## User Inputs 

user_name = input("\nEnter Your Name: ")
user_age = int(input("Enter Your Age: "))
user_consent = input("Type \"yes\" to start playing the game or \"no\" to exit: ")

## Error Handling

if user_consent.lower() == "yes":
    
    
    print("""
Question A : What is full form of TPU?
    """)
    
    user_response = input("Enter your answer: ").lower()
    answer_a = "tensor processing unit"
    if user_response == answer_a:
        print("\nCorrect You Get 10 points!")
        user_score +=10.0
        print("\nYour Updated Score! ",user_score)
    else:
        print("\nSorry Incorrect Answer!")
        print("Correct Answer: ",answer_a)
        user_score -=1.5
        print("\nYour Updated Score: ", user_score)

    print("""
Question B : What is the full form of GPU?
    """)

    user_response = input("Enter your answer: ").lower()
    answer_b = "graphics processing unit"
    if user_response == answer_b:
        print("\nCorrect You Get 10 points!")
        user_score +=10.0
        print("\nYour Updated Score! ",user_score)
    else:
        print("\nSorry Incorrect Answer!")
        print("Correct Answer: ",answer_b)
        user_score -=1.5
        print("\nYour Updated Score: ", user_score)

    print("""
Question C : Who is the father of Computer Graphics ?
    """)

    user_response = input("Enter your answer: ").lower()
    answer_c = "ivan sutherland"
    if user_response == answer_c:
        print("\nCorrect You Get 10 points!")
        user_score +=10.0
        print("\nYour Updated Score! ",user_score)
    else:
        print("\nSorry Incorrect Answer!")
        print("Correct Answer: ",answer_c)
        user_score -=1.5
        print("\nYour Updated Score: ", user_score)

    print("""
Question D : First user of Computer Graphics ?
    """)

    user_response = input("Enter your answer: ").lower()
    answer_d = "william fetter"
    if user_response == answer_d:
        print("\nCorrect You Get 10 points!")
        user_score +=10.0
        print("\nYour Updated Score! ",user_score)
    else:
        print("\nSorry Incorrect Answer!")
        print("Correct Answer: ",answer_d)
        user_score -=1.5
        print("\nYour Updated Score: ", user_score)

    print("""
Question E : Who is the father of Computer?
    """)

    user_response = input("Enter your answer: ").lower()
    answer_e = "charles babbage"
    if user_response == answer_e:
        print("\nCorrect You Get 10 points!")
        user_score +=10.0
        print("\nYour Updated Score! ",user_score)
    else:
        print("\nSorry Incorrect Answer!")
        print("Correct Answer: ",answer_e)
        user_score -=1.5
        print("\nYour Updated Score: ", user_score)


elif user_response.lower() == "no":
    print("Thanks for Playing!")
else:
    print("Invalid Input!! Type Yes or No")
    


## Evaluation of Result and Display the Result 

print("\n Your Results !!! ",user_score)
print("""
Thanks for Playing
""")

