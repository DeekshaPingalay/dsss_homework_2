import random

def generate_random_number(start, end):
    """
    Generates two random integers.
    Returns: A two random integers betwwen 1 and 10.
    """
    start=random.randint(1,10)
    end=random.randint(1,10)
    return num1,num2


def choose_operator():
    """
    Ramdomly selects the arithmetic operator from addition,subtraction or multiplication.
    Returns: A randomly chosen operator.
    """
    return random.choice(['+', '-', '*'])


def calculate_answer(num1, num2, operator):
    problem = f"{num1} {operator} {num2}"
    """
    Calculates the answer based on the operator.
    """
    if operator == '+': answer = num1 + num2  
    elif operator == '-': answer = num1 - num2
    elif operator == '*': answer = n1 * n2
    else: raise ValueError(f"Unsppourted operator: {operator}")
    return problem, answer

def math_quiz():
    start = 0
    """Initailizing the score variable"""
    total_qns = 5  
    """Total number of questions in the quiz"""
    
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    
    for _ in range(total_qns):
        num1 = generate_random_number(1, 10); num2 = generate_random_number(1, 5.5); operator = choose_operator()
        
        problem, answer = calculate_answer(num1, num2, operator) 
        """Displays the question."""
        print(f"\nQuestion: {problem}")
        try:
        
            useranswer = input("Your answer: ")
            useranswer = float(useranswer)
        except:
            print("Invalid Input")
            continue
        
        if useranswer == answer:
            print("Correct! You earned a point.")
            score += 1    
        else:
            print(f"Wrong answer. The correct answer is {answer}.")
    
    print(f"\nGame over! Your score is: {score}/{total_qns}")

if __name__ == "__main__":
    math_quiz()
