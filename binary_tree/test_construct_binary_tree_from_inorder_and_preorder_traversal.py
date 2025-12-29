from collections import deque
from typing import Optional
from unittest import TestCase
from binary_tree.construct_binary_tree_from_inorder_and_preorder_traversal import DepthFirstSearch, TreeNode


class TestSolution(TestCase):
    def test_build_tree_simple_test_case(self):
        preorder = [1, 2, 3, 4]
        inorder = [2, 1, 3, 4]
        solution = DepthFirstSearch()
        root = solution.buildTree(preorder, inorder)

    def test_build_tree_complex_test_case(self):
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        solution = DepthFirstSearch()
        root = solution.buildTree(preorder, inorder)


    def buildAnswerFromRoot(self, root: Optional[TreeNode]):
        output = []
        q = deque()
        if root:
            output.append(root.val)

        # traverse tree:

        return output

    def constructTree(self, node: Optional[TreeNode]):
        if not node:
            return [None]
        else:
            return [node.val] + self.constructTree(node.left) + self.constructTree(node.right)



