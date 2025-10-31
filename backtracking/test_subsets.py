from unittest import TestCase

from backtracking.subsets import Solution


class Test(TestCase):
    def test_subsets(self):
        answer =  Solution().subsets([1, 2, 3, 4])
        self.assertEqual(answer, )

    def test_bit_subsets(self):
        answer = Solution().bitsubsets([1, 2, 3])

