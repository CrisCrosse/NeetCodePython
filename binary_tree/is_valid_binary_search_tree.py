# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def DFS(self, root: Optional[TreeNode], min: int, max: int):
        if not root:
            return True
        key = root.val

        # if no left or right branches then is valid
        left_is_valid, right_is_valid = True, True
        if root.left:
            left = root.left
            if left.val >= key:
                return False
            if left.val >= max:
                return False
            if left.val <= min:
                return False
            left_is_valid = self.DFS(left, min, key)
        if root.right:
            right = root.right
            if right.val <= key:
                return False
            if right.val >= max:
                return False
            if right.val <= min:
                return False
            right_is_valid = self.DFS(right, key, max)

        return left_is_valid and right_is_valid

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return None
        return self.DFS(root, -1001, 1001)

# This method uses depth first search and is O(n) time compllexity because we iterate over each node just once
# It is O(n) space complexity because we the recursion tree will expand up to O(n) size

class BruteForce:
    left_check = staticmethod(lambda val, limit: val < limit)
    right_check = staticmethod(lambda val, limit: val > limit)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if (not self.isValid(root.left, root.val, self.left_check) or
            not self.isValid(root.right, root.val, self.right_check)):
            return False

        return self.isValidBST(root.left) and self.isValidBST(root.right)

    def isValid(self, root: Optional[TreeNode], limit: int, check) -> bool:
        if not root:
            return True
        if not check(root.val, limit):
            return False
        return (self.isValid(root.left, limit, check) and
                self.isValid(root.right, limit, check))

# This method is O(n^2) time complexity because for each node we iterate over every other node once
# It is O(n^2) space complexity also due to recursion