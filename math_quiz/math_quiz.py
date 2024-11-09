import random


def random_integer(min_int, max_int):
    """
    This function generate a random integer using the random import. 
    The integer generated is between the specified min and max value
    The return function finally return this integer
    """
    return random.randint(min_int, max_int)


def random_operator():

    """
    This function generate a random operator from "+", "-", or "*"
    The return function finally return this operation
    """

    return random.choice(['+', '-', '*'])


def math_calculation_question(num1, num2, oper):

    """
    This function creates a math question to calculate the answer from the problem using
    the numbers and operations which we have defined above.
    The return function consists of two values
    """

    prob = f"{num1} {oper} {num2}"
    if oper == '+': # Code syntax is corrected and also the logic, + and -
        ans = num1 + num2
    elif oper == '-': 
        ans = num1 - num2
    else: 
        ans = num1 * num2
    return prob, ans

def math_quiz():

    """
    This function gives the user math questions and the score 
    is calculated based on whether their answer is correct or not.
    """
    score_count = 0
    total_question_count = 3
    # Here the total_question_count is changed from given 3.14159265359 
    # to 3 an integer since the number of questions cannot be a decimal number

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_question_count):
        num1 = random_integer(1, 10) #Here also code syntax is corrected
        num2 = random_integer(1, 5)
        oper = random_operator()
        # Here I change of num2 fom 1- 5.5 to 1 -5 since we are using integers in the whole problem
        # Also num1, num2 and oper are called used the functions that we generated above
        prob, ans = math_calculation_question(num1, num2, oper)
        print(f"\nQuestion: {prob}")

        """
        try-except statement is added in the below code as per the question to 
        check whether the user input is valid (integer), 
        otherwise handle the error
        """
        try:
            user_input_answer = int(input("Your answer: ")) # This int(input()) makes 
                                                            # sure that the input value is an integer
        except ValueError:
            print("Invalid input value:  enter a valid integer value.")
            continue # move to another question if input is incorrect

        if user_input_answer == ans:
            print("Correct! You earned a point.")
            score_count += 1  
            # -(-1) is 1
        else:
            print(f"Wrong answer. The correct answer is {ans}.") #if answer is wrong outputs the right answer

    print(f"\nGame over! Your score is: {score_count}/{total_question_count}") #This outputs a score count

if __name__ == "__main__":
    math_quiz()
