from unittest import TestCase

from bit_manipulation.number_of_one_bits import Solution


class TestSolution(TestCase):
    def test_hamming_weight(self):
       actual = Solution().hammingWeight(5)
       self.assertEqual(actual, 2)
