from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FirstTry:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        left = root.left
        right = root.right
        if left or right:
            root.right = left
            root.left = right
            self.invertTree(right)
            self.invertTree(left)
        return root
    # This solution is O(n) time complexity as we traverse the tree once
    # this solution is O(n) space complexity due to recursion we create 2n objects in memory