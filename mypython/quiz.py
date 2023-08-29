import getpass, sys, os

# Questions and answers
print("1\n")
questions = [
    "Which command allows people to import commands and funcitons?"
    "What command defines a funciton?"
    "Which command prints a specified messge on the screen?"
    "Which command helps differentiate right from wrong?"
    "Which command returns input from the user?"
    "A collection of characters is called ____?"
]
print("2\n")
correct_answers = [
    "import"
    "def"
    "print"
    "if"
    "return"
    "string"
]

def question_with_response(prompt):
    print(f"\nQuestion {prompt+1}: {questions[prompt]}")
    msg = input("\nYour answer: ").lower()
    return msg

#Quiz function
def run_quiz():
    print("hi\n")
    correct = 0
    for i in range(len(questions)):
        print(i)
                
        rsp = question_with_response(i)
        if rsp == correct_answers[i]:
            print("Correct!")
            correct +=1
        else:
            print("Incorrect")
print("hello\n")

run_quiz()        
            
print("\nQuiz completed!")
print(getpass.getuser() + " you scored " + str((correct)/6))