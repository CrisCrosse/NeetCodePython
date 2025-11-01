# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BruteForce:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        diameter = left_height + right_height

        max_diameter_of_sub_tree = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max(diameter, max_diameter_of_sub_tree)

    # This has O(n^2) space complexity because in each diameterOfBinaryTree call we traverse each node using the maxDepth function
    # then we call diameterOfBinaryTree for each node --> n * n, it has the same space complexity as a result of the recursion


class Optimised:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def dfs(root) -> int:
            nonlocal max_diameter
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            current_diameter = left + right
            max_diameter = max(max_diameter, current_diameter)
            return 1 + max(left, right)

        dfs(root)
        return max_diameter

        # this solution has O(n) time complexity because it only traverses each node once
        # space complexity is the same due to the recursion
