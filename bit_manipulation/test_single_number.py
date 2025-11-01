from unittest import TestCase

from bit_manipulation.single_number import TheirSortSolution, SortingSolution


class TestSortingSolution(TestCase):
    def test_single_number(self):
        actual = TheirSortSolution().singleNumber([-336,513,-560,-481,-174,101,-997,40,-527,-784,-283,-336,513,-560,-481,-174,101,-997,40,-527,-784,-283,354])
        self.assertEqual(actual, 354)

    def test_single_number(self):
        actual = SortingSolution().singleNumber(
            [-336, 513, -560, -481, -174, 101, -997, 40, -527, -784, -283, -336, 513, -560, -481, -174, 101, -997,
             40, -527, -784, -283, 354])
        self.assertEqual(actual, 354)

