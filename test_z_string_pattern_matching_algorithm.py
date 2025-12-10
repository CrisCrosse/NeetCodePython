from unittest import TestCase

from z_string_pattern_matching_algorithm import ZAlgorithm


class TestZAlgorithm(TestCase):
    def test_ZAlgorithm_simple(self):
        z = ZAlgorithm()
        result = z.ZSearch("abab")

        self.assertEqual(result, [0, 0, 2, 0])

    def test_ZAlgorithm_complex(self):
        z = ZAlgorithm()
        result = z.ZSearch("abaxabab")

        self.assertEqual(result, [0, 0, 1, 0, 3, 0, 2, 0])

    def test_ZAlgorithm_from_online_complex(self):
        z = ZAlgorithm()
        result = z.z_function("abaxabab")

        self.assertEqual(result, [0, 0, 1, 0, 3, 0, 2, 0])

    def test_ZAlgorithm_indices_which_match(self):
        z = ZAlgorithm()
        result = z.ReturnIndicesWhichMatchPattern("abab", "xyzababxyzabab")
        self.assertEqual(result, [3, 10])
