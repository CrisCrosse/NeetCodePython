# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BruteForce:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ordered_nodes = []
        q = deque([root])

        while q:
            for i in range(len(q)):
                node = q.popleft()
                ordered_nodes.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        ordered_nodes.sort()
        print(ordered_nodes)
        return ordered_nodes[k - 1]

# This solution is O(n log n) time complexity in the worst case because we use the built in list sort which utilises tim sort
# The solution is O(n) space complexity because we construct an array of all nodes

class InOrderDepthFirstSearch:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

        dfs(root)
        return arr[k - 1]

# This solution is O(n) because we traverse each node once
# The solution is O(n) space complexity because we construct an array of all nodes


class OptimalDFS:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k
        res = root.val

        def dfs(node):
            # global variables
            nonlocal cnt, res

            if not node:
                return

            dfs(node.left)
            cnt -= 1
            if cnt == 0:
                res = node.val
                return
            dfs(node.right)

        dfs(root)
        return res

# This solution is up to O(n) if k is the length of the whole tree, but we will stop early otherwise
# The solution is O(n) space complexity because we recurse

class Iterative:
    class Solution:
        def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
            stack = []
            curr = root

            while stack or curr:
                # add left nodes to stack
                while curr:
                    stack.append(curr)
                    curr = curr.left
                # remove a left node
                curr = stack.pop()
                # remove one from the count
                k -= 1
                if k == 0:
                    return curr.val
                #
                curr = curr.right

# This solution is O(n) space and time complexity

class Optimal:
    class MorrisTraversal:
        def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
            curr = root

            while curr:
                # if no left node visit current (decrement count) and move right or up tree
                if not curr.left:
                    k -= 1
                    if k == 0:
                        return curr.val
                    curr = curr.right
                else:
                    # otherwise find predecessor of curr in ordered list
                    pred = curr.left
                    # predecessor is rightmost node
                    while pred.right and pred.right != curr:
                        pred = pred.right

                    # if no right node then create reverse link
                    if not pred.right:
                        pred.right = curr
                        curr = curr.left
                    # reverse link encountered, remove reverse link and traverse right hand side
                    else:
                        pred.right = None
                        k -= 1
                        if k == 0:
                            return curr.val
                        curr = curr.right

            return -1

# This solution is O(n) time complexity as it traverses the tree
# It is O(1) space complexity because we do not use a stack or recursion