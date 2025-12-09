# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class NonOptimisedSolution:
    def isBalanced(self, root: Optional[TreeNode], tree_level=0) -> bool:
        if not root:
            return True

        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)

        print(
            f"at tree level {tree_level} with node {root.val}, left {root.left.val if root.left else None}, right {root.right.val if root.right else None}")
        print(
            f"left height {left_height}, right height {right_height} with difference {abs(left_height - right_height)}")
        if abs(left_height - right_height) > 1:
            print("Trees are not balanced")
            return False
        else:
            return self.isBalanced(root.left, 1 + tree_level) and self.isBalanced(root.right, 1 + tree_level)

    def getHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

# This solution is O(n^2) time complexity because for each node we traverse all the way down the tree in both directions
# with get height
# it is the same space complexity due to using recursion keeping references open until the recursion stack starts to
# recede

class OptimisedSolution:
    class Solution:
        def isBalanced(self, root: Optional[TreeNode], tree_level=0) -> bool:
            if not root:
                return True

            left_height, left_balanced = self.getHeight(root.left)
            right_height, right_balanced = self.getHeight(root.right)

            if abs(left_height - right_height) <= 1 and left_balanced and right_balanced:
                return True

            print("Trees are not balanced")
            return False

        def getHeight(self, root: Optional[TreeNode]) -> (int, bool):
            if not root:
                return 0, True

            left_height, left_balanced = self.getHeight(root.left)
            right_height, right_balanced = self.getHeight(root.right)

            this_node_is_balanced = abs(left_height - right_height) <= 1

            return 1 + max(left_height, right_height), left_balanced and right_balanced and this_node_is_balanced

# This solution is O(n) time and space complexity because we only recurse through each node once

class CleanedUpOptimisedSolution:
    def isBalanced(self, root: Optional[TreeNode], tree_level=0) -> bool:
        return self.DepthFirstSearchHeightAndBalance(root)[1]

    def DepthFirstSearchHeightAndBalance(self, root: Optional[TreeNode]) -> (int, bool):
        if not root:
            return 0, True

        left_height, left_balanced = self.DepthFirstSearchHeightAndBalance(root.left)
        # these early returns aren't necessary but as soon as we find an unbalanced node we can cease our recursion
        if not left_balanced:
            return 0, False
        right_height, right_balanced = self.DepthFirstSearchHeightAndBalance(root.right)
        # these early returns aren't necessary but as soon as we find an unbalanced node we can cease our recursion
        if not right_balanced:
            return 0, False

        this_node_is_balanced = abs(left_height - right_height) <= 1

        return (1 + max(left_height, right_height), left_balanced and right_balanced and this_node_is_balanced)


