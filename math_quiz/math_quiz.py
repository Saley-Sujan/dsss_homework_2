import random


def random_value(min_value, max_value):
    """
    Generate random integer values between minimum and maximum value.
    """
    return random.randint(min_value, max_value)


def choose_operator(): #choose random arethmetic operator 
    return random.choice(['+', '-', '*'])


def generate_math(num1, num2, op):
    pro = f"{num1} {op} {num2}"
    if op == '+': ans = num1 + num2
    elif op == '-': ans = num1 - num2
    else: ans = num1 * num2
    return pro, ans

def math_quiz():
    s = 0
    total_qus = 3 #changed float value to int value

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_qus):
        num1 = random_value(1, 10); num2 = random_value(1, 5); op = choose_operator()

        PROBLEM, ANSWER = generate_math(num1, num2, op)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{total_qus}")

if __name__ == "__main__":
    math_quiz()
