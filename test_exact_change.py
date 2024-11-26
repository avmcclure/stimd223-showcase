import unittest
from io import StringIO
import sys
from exact_change import exact_change

class TestExactChange(unittest.TestCase):
    def setUp(self):
        # Redirect stdout to capture print statements
        self.sio = StringIO()
        self.saved_stdout = sys.stdout
        sys.stdout = self.sio

    def tearDown(self):
        # Restore stdout to its original state
        sys.stdout = self.saved_stdout

    def test_exact_change(self):
        exact_change(11.46)

        # Capture the output
        output = self.sio.getvalue().strip().split("\n")

        # Expected output list
        expected_output = ["1 - $10 bill", "1 - $1 bill", "1 - quarter", "2 - dime", "1 - penny"]

        # Check that the captured output matches the expected output
        self.assertEqual(output, expected_output)

    def test_zero_total(self):
        exact_change(0.00)

        # Capture the output
        output = self.sio.getvalue().strip().split("\n")

        # Expected output list
        expected_output = ['']

        # Check that the captured output matches the expected output
        self.assertEqual(output, expected_output)

    def test_large_amt(self):
        exact_change(423.44)

        # Capture the output
        output = self.sio.getvalue().strip().split("\n")

        # Expected output list
        expected_output = ['42 - $10 bill', '3 - $1 bill', '1 - quarter', '1 - dime', '1 - nickel', '4 - penny']

        # Check that the captured output matches the expected output
        self.assertEqual(output, expected_output)

if __name__ == "__main__":
    unittest.main()