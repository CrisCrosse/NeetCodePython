# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        print(f"checking")
        if not root or not subRoot:
            if not root and not subRoot:
                return True
            return False

        if self.isSame(root, subRoot):
            return True

        print(
            f"checking if left node {root.left.val if root.left else None} is same as subTree starting at node {subRoot.val}")
        if self.isSubtree(root.left, subRoot):
            return True
        print(
            f"checking if right node {root.right.val if root.right else None} is same as subTree starting at node {subRoot.val}")
        if self.isSubtree(root.right, subRoot):
            return True

        return False

    def isSame(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        print(
            f"checking if subtree starting at root node {root.val if root else None} is same as subTree starting at node {subRoot.val if subRoot else None}")
        if not root or not subRoot:
            if not root and not subRoot:
                return True
            else:
                return False

        values_equal = root.val == subRoot.val
        if not values_equal:
            return False

        left_same = self.isSame(root.left, subRoot.left)
        right_same = self.isSame(root.right, subRoot.right)

        if left_same and right_same and values_equal:
            return True

# this solution is O(n^2) space and time as for each node in the tree we recurse through every lower node matches the subTree and repeat for each tree node

class Serialiszing:
    def serialize(self, root: Optional[TreeNode], result="") -> str:
        if not root:
            return "$#"
        result += str(root.val)
        result += self.serialize(root.left)
        result += self.serialize(root.right)

        return result

    # see ZAlgorithmClassForExplanation
    def z_function(self, s: str) -> list:
        z = [0] * len(s)
        l, r, n = 0, 0, len(s)
        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1
        return z

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        pattern = self.serialize(subRoot)
        string = self.serialize(root)
        print(f"pattern {pattern}, string: {string}")
        serialized_subtree_then_tree = pattern + "/" + string
        pattern_match_indices = self.z_function(serialized_subtree_then_tree)

        for matching_chars in pattern_match_indices:
            if matching_chars == len(pattern):
                return True

        return False
