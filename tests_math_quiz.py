import unittest
from math_quiz import generate_random_number, choose_operator, calculate_answer

class TestMathQuizFunctions(unittest.TestCase):

    def test_generate_random_number(self):
        """
        Test returns a number within the given range.
        """
        # Range between 1 to 10
        result = generate_random_number(1, 10)
        self.assertGreaterEqual(result, 1, "Generated number should be greater than or equal to 1.")
        self.assertLessEqual(result, 10, "Generated number should be less than or equal to 10.")
        
        # Range between 0.1 to 5.5
        result = generate_random_number(0.1, 5.5)
        self.assertGreaterEqual(result, 0.1, "Generated number should be greater than or equal to 0.1.")
        self.assertLessEqual(result, 5.5, "Generated number should be less than or equal to 5.5.")

    def test_choose_operator(self):
        """
        Test retur valid operators such as '+', '-', or '*'.
        """
        operator = choose_operator()
        self.assertIn(operator, ['+', '-', '*'], f"The operator '{operator}' is invalid.")

    def test_calculate_answer(self):
        """
        Test calculates the answer for various operators.
        """
        # addition
        result = calculate_answer(5, 3, '+')
        self.assertEqual(result, 8, "5 + 3 should equal 8.")

        #subtraction
        result = calculate_answer(10, 4, '-')
        self.assertEqual(result, 6, "10 - 4 should equal 6.")

        # multiplication
        result = calculate_answer(3, 5, '*')
        self.assertEqual(result, 15, "3 * 5 should equal 15.")

        # For an invalid operator (ValueError exception is raised)
        with self.assertRaises(ValueError):
            calculate_answer(3, 5, '/')

if __name__ == "__main__":
    unittest.main()

