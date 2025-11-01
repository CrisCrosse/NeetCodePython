from unittest import TestCase

from bit_manipulation.counting_bits import Optimal


class TestOptimal(TestCase):
    def test_count_bits(self):
        actual = Optimal().countBits(4)
        self.assertEqual(actual, [0,1,1,2,1])

    def test_count_bits_2(self):
        actual = Optimal().countBits(30)