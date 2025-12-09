from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FirstTry:
    def traverseNode(self, root: Optional[TreeNode], current_depth: int) -> int:
        max_left_depth = current_depth
        max_right_depth = current_depth
        if root.left:
            max_left_depth = self.traverseNode(root.left, current_depth + 1)
        if root.right:
            max_right_depth = self.traverseNode(root.right, current_depth + 1)
        return max_left_depth if max_left_depth >= max_right_depth else max_right_depth

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.traverseNode(root, 1)

    # this solution is O(n) for time and space complexity

class SimplifiedSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # this solution relies on getting to the tip nodes and when maxDepth is called with None
    # we return 0, which then gets propogated back up the recursion stack adding one with each recursion depth
    # very elegant