from unittest import TestCase

from two_pointers.three_sum import BinarySearch, OnsquaredTimeComplexityUsingHashMap


class TestBinarySearch(TestCase):
    def test_three_sum(self):
        actual = OnsquaredTimeComplexityUsingHashMap().threeSum([-1,0,1,2,-1,-4])
        return actual
