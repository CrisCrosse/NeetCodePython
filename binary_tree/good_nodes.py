# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# A good node is one where the path to the node contains no greater values than the node value

class Solution:
    def DFS(self, root: TreeNode, traversedNodes: List[int]):
        if not root:
            return 0
        print(f"traversing node {root.val} having seen {traversedNodes}")
        result = 0
        if root.val >= max(traversedNodes):
            result += 1

        traversedNodes.append(root.val)
        result += self.DFS(root.left, traversedNodes)
        result += self.DFS(root.right, traversedNodes)
        traversedNodes.pop()
        print(f"finished traversing below node {root.val} good nodes is {result}")
        return result

    def goodNodes(self, root: TreeNode) -> int:
        return self.DFS(root, [-1000])

# This solution is O(n) space and time complexity due to recursing through each node

class DfsUsingMaxVal:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            # This is better than passing in all the traversed nodes
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)



