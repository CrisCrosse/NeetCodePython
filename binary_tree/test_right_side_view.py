from unittest import TestCase
from binary_tree.right_side_view import Solution, TreeNode

class TestSolution(TestCase):
    def test_right_side_view(self):
        # root=[1,2,3]
        root = TreeNode(1, TreeNode(2), TreeNode(3))



        result = Solution().rightSideView(root)

        self.assertEqual(result, [1, 3])
