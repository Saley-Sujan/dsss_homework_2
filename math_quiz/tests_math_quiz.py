import unittest
from math_quiz import random_value, choose_operator, generate_math


class TestMathGame(unittest.TestCase):

    def test_random_value(self):
        # Test if random numbers generated are within the specified range
        min_value = 1
        max_value = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_value(min_value, max_value)
            self.assertTrue(min_value <= rand_num <= max_value)

    def test_choose_operator(self):
        
        ope = {'+', '-', '*'}
        for _ in range(1500):  # Test multiple random variables
            operator = choose_operator()
            self.assertIn(operator, ope)

    def test_generate_math(self):
            test_cases = [
            (6, 2, '+', '6 + 2', 8),
            (15, 3, '-', '15 - 3', 12),
            (4, 6, '*', '4 * 6', 24),
            (6, 0, '+', '6 + 0', 6),
            (0, 5, '*', '0 * 5', 0),
            (9, 1, '-', '9 - 1', 8),
            (3, 3, '+', '3 + 3', 6)
         ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = generate_math(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
