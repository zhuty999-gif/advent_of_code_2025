import unittest
from solution import find_largest_joltage_from_a_bank

class TestLargestJoltage(unittest.TestCase):
    def test_example_1(self):
        # In 987654321111111, you can make the largest joltage possible, 98
        self.assertEqual(find_largest_joltage_from_a_bank("987654321111111"), 98)

    def test_example_2(self):
        # In 811111111111119, you can make the largest joltage possible by turning on the batteries labeled 8 and 9, producing 89 jolts.
        self.assertEqual(find_largest_joltage_from_a_bank("811111111111119"), 89)

    def test_example_3(self):
        # In 234234234234278, you can make 78 by turning on the last two batteries (marked 7 and 8).
        self.assertEqual(find_largest_joltage_from_a_bank("234234234234278"), 78)

    def test_example_4(self):
        # In 818181911112111, the largest joltage you can produce is 92.
        self.assertEqual(find_largest_joltage_from_a_bank("818181911112111"), 92)

    def test_total_output(self):
        # The total output joltage is the sum of the maximum joltage from each bank... 357.
        banks = [
            "987654321111111",
            "811111111111119",
            "234234234234278",
            "818181911112111"
        ]
        total = sum(find_largest_joltage_from_a_bank(bank) for bank in banks)
        self.assertEqual(total, 357)

if __name__ == '__main__':
    unittest.main()

