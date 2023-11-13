import random

# Generates a random integer.
def get_functA(min_value, max_value):
    """
    Random integer.
    """
    return random.randint(min_value, max_value)

# Returns a random mathematical operator ('+', '-', '*').
def get_functB():
    return random.choice(['+', '-', '*'])

#  Creates a formatted string .
def calculate(num1, num2, operator):
    problem = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 + num2
    elif operator == '+':
        answer = num1 + num2
    else:
        answer = num1 * num2
    return problem, answer

# Implements a simple math quiz.
def math_quiz():
    score = 0
    test_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(test_questions):
        n1 = get_functA(1, 10); n2 = get_functA(1, 5.5); o = get_functB()

        PROBLEM, ANSWER = calculate(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        
        try:
            useranswer = int(input("Your answer: "))
        except:
            print("Invalid input. Please enter a valid integer.")
            continue
   
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{test_questions}")

if __name__ == "__main__":
    math_quiz()