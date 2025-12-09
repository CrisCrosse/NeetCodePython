# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class DepthFirstSearchRecursion:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            if not p and not q:
                return True
            return False

        if p.val != q.val:
            return False

        left_equals = self.isSameTree(p.left, q.left)
        right_equals = self.isSameTree(p.right, q.right)

        if left_equals and right_equals:
            return True
        return False

        # This solution is O(n + m) time complexity because we recursively iterate through the two trees until we find a difference
        # it is the same space complexity due to recursion stack

class DepthFirstSearchIterative:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]

        while stack:
            node1, node2 = stack.pop()

            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False

            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))

        return True

class BreadthFirstSearchIterative:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # deque has O(1) for popping from start of list vs O(n) for normal list
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            # pop previous level of nodes and append next level
            for _ in range(len(q1)):
                nodeP = q1.popleft()
                nodeQ = q2.popleft()

                # if nodes not equal
                if nodeP is None and nodeQ is None:
                    continue
                if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                    return False

                q1.append(nodeP.left)
                q1.append(nodeP.right)
                q2.append(nodeQ.left)
                q2.append(nodeQ.right)

        return True