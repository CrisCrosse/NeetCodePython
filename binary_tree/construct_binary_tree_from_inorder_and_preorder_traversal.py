# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Pre order traversal is root, left subtree, right subtree
# first value in pre order traversal is always the root
# in order traversal is left subtree, root, right subtree

class DepthFirstSearch:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # take the root node
        top_node_val = preorder[0]
        root = TreeNode(top_node_val)

        # find the root nodes index in the ordered array, everything below index is left subtree, above is right
        mid = inorder.index(top_node_val)
        number_of_left_subtree_nodes = mid
        #  mid also equals number of left subnodes
        #  eg PRE root:3, left 9 right: [ root 20, left 15, right 7 ] ORDER left 9, root: 3, right: [left: 15, root: 20, right: 7]
        # recursively build the left subtree as mid gives us the number of left subtree nodes we take and passing the left subtree of ordered array
        root.left = self.buildTree(preorder[1 : number_of_left_subtree_nodes + 1], inorder[:mid])
        # recursively build the right subtree because mid to the end of the array gives us the right subtree nodes
        root.right = self.buildTree(preorder[number_of_left_subtree_nodes + 1 :], inorder[mid + 1 :])
        return root

# THis solution is O(n^2) time complexity due to using .index()
# This solution is O(n) space complexity

class DepthFirstSearchWithHashMap:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}
        # store hashmap of int value to index for in order (left, root, right) to avoid .index() call for O(n) time complexity

        # current index in pre-ordered array
        self.pre_idx = 0
        # instead of altering the subarrays passed in use left and right pointers
        def dfs(l, r):
            if l > r:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = indices[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root

        return dfs(0, len(inorder) - 1)


class DepthFirstSearchOptimal:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIdx = inIdx = 0

        # limit is the
        def dfs(limit):
            nonlocal preIdx, inIdx
            if preIdx >= len(preorder):
                return None
            if inorder[inIdx] == limit:
                inIdx += 1
                return None

            root = TreeNode(preorder[preIdx])
            preIdx += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root
        return dfs(float('inf'))


class MorrisTraversal:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        head = TreeNode(None)
        curr = head
        i, j, n = 0, 0, len(preorder)
        while i < n and j < n:
            # Go right and then as far left as possible
            curr.right = TreeNode(preorder[i], right=curr.right)
            curr = curr.right
            i += 1
            while i < n and curr.val != inorder[j]:
                curr.left = TreeNode(preorder[i], right=curr)
                curr = curr.left
                i += 1
            j += 1
            while curr.right and j < n and curr.right.val == inorder[j]:
                prev = curr.right
                curr.right = None
                curr = prev
                j += 1

        return head.right