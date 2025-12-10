# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class InitialAttempt:
    def findSubNodes(self, node: Optional[TreeNode]) -> List[TreeNode]:
        # recurse through all nodes below this one and return all
        if not node:
            return []
        nodes = [node]
        return nodes + self.findSubNodes(node.left) + self.findSubNodes(node.right)

    def depthFirstSearchForCommonAncestors(self, node: Optional[TreeNode], p: TreeNode, q: TreeNode) -> List[TreeNode]:
        if not node:
            return []

        print(f"looking at node {node.val if node else None}")
        common_ancestors = []

        # get all sub nodes from this node
        sub_nodes = self.findSubNodes(node)
        sub_nodes_vals = [sub_node.val for sub_node in sub_nodes]
        print(f"sub nodes of node {sub_nodes_vals}")

        # if it is a common ancestor of targets add to list
        if p.val in sub_nodes_vals and q.val in sub_nodes_vals:
            print(f"node is a common ancestor of {p.val} and {q.val}")
            common_ancestors.append(node)

        # recurse through all nodes below current node and append each common ancestor set
        return common_ancestors + self.depthFirstSearchForCommonAncestors(node.left, p, q) + self.depthFirstSearchForCommonAncestors(node.right, p, q)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        common_ancestors = self.depthFirstSearchForCommonAncestors(root, p, q)

        # this is above the max input size of 100 so any common ancestor gets returned
        min_node_val = 101
        min_node = None
        for ancestor in common_ancestors:
            if ancestor.val < min_node_val:
                min_node = ancestor

        return min_node

# this solution is O(n^2) time and space complexity because for each input node of the tree,
# we recurse through all the nodes below it to find the sub nodes
# and repeat for every single node

# This solution does not take into account that the input tree is a binary search tree
# so for th first node if val = 8, all vals < 8 are on the left, and all vals > 8 are on the right


class BinarySearchTreeRecursion:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q:
            return None
        # if both values are on the left hand side of the tree
        if (max(p.val, q.val) < root.val):
            # search left hand side as lower in the tree = lower value
            return self.lowestCommonAncestor(root.left, p, q)
        # if both values are on the right hand side of the tree
        elif (min(p.val, q.val) > root.val):
            # search right hand side as lower in the tree = lower valuex
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            # values are split across the current nodes branches, so this node is the lowest common ancestor
            return root

# this solution is O(h) time and space where h is the height of the tree
# because we disregard the non-relevant branch at each node and recurse through the height of the tree

class BinarySearchTreeIteration:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur

# this solution is O(h) time complexity as above but O(1) space complexity because we only use cur as the ref


