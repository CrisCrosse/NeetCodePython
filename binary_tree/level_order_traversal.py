# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BreadthFirstSearch:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BreadthFirstSearch
        if not root:
            return []
        result = []
        nodes = deque([root])

        while nodes:
            print(f"result is currently {result}, nodes currently on level stack {[node.val for node in nodes]}")
            new_level = []
            for i in range(len(nodes)):
                # using a normal list for this = O(n) time complexity due to popping from front of list,
                #  use deque for O(1)
                node = nodes.popleft()
                print(f"looking at the {i + 1}th node in this level with val {node.val}")
                new_level.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            result.append(new_level)

        return result
# This solution is O(n) time and space complexity because we traverse each node once and add it to the return list of
# lists which has a total size of n
# I don't think there is any way to improve this because you have to traverse each node and the output is fixed at n size


class DepthFirstSearch:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(node, depth):
            if not node:
                return None
            # accessing and mutating global res is a bit fishy
            if len(res) == depth:
                # if no existing level list add empty list for new level
                res.append([])
            # add the node to the correct level
            res[depth].append(node.val)
            # add all deeper nodes also until we get to the leaf nodes
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        # start recursion which mutates res
        dfs(root, 0)
        return res

# This solution works and is also O(n) time due to traversing every node once, but will be more memory intensive due to
# using recursion although still O(n)?



