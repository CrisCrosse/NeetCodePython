# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class BreadthFirstSearch:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        nodes = deque([root])
        right_side_nodes = []

        while nodes:
            print(
                f"starting new level of breadth first search, current level nodes: {[node.val for node in nodes]}, adding {nodes[-1].val} as right hand side val for this level")
            right_side_nodes.append(nodes[-1].val)
            for index in range(len(nodes)):
                node = nodes.popleft()
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)

        return right_side_nodes

# This solution is O(n) time and space complexity and breadth first search is more suitable for this problem because
# you want to evaluate each level to determine the most right value


class DepthFirstSearch:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, depth):
            if not node:
                return None
            # If we are yet to add anything to result for this level of recursion
            if depth == len(res):
                res.append(node.val)
            # search right hand side first
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return res