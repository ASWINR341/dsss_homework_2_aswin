import unittest
from math_quiz import random_integer, random_operator, math_calculation_question


class TestMathGame(unittest.TestCase):

    def test_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        # Test if random operator generated are within the list
        valid_operators = ['+','-','*']
        for _ in range(10):
            operator = random_operator()
            # the self.assertIn tell if specified item is present in a given container
            self.assertIn(operator,valid_operators)

    def test_math_calculation_question(self):
            test_cases = [
                #numerous test cases with all operators were added
                (5, 2, '+', '5 + 2', 7),
                (3, 7, '-', '3 - 7', -4),
                (15, 2, '*', '15 * 2', 30),
                (10, 4, '-', '10 - 4', 6)
                
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                prob, ans = math_calculation_question(num1,num2,operator)
                # The self.assertEqual tells if the values are equal
                self.assertEqual(prob,expected_problem)
                self.assertEqual(ans,expected_answer)

if __name__ == "__main__":
    unittest.main()
