import collections
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class InitialAttempt:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        
        original_nodes = []
        while head:
            original_nodes.append(head)
            head = head.next

        original_nodes_display = [(node.val, node.random.val if node.random else None) for node in original_nodes]
        print(f"original nodes {original_nodes_display}")

        new_nodes = []
        original_nodes.reverse()
        original_nodes_display = [(node.val, node.random.val if node.random else None) for node in original_nodes]
        print(f"original nodes reversed {original_nodes_display}")
        # reverse nodes in list, so I can create new nodes with next values in one pass
        for index, original_node in enumerate(original_nodes):
            if index > 0:
                new_nodes.append(Node(original_node.val, new_nodes[index - 1]))
            else:
                new_nodes.append(Node(original_node.val))

        new_nodes_display = [(node.val, node.random.val if node.random else None, node.next.val if node.next else None)
                             for node in new_nodes]
        print(f"new nodes {new_nodes_display}")

        # get the random ref
        for index, new_node in enumerate(new_nodes):
            original_node = original_nodes[index]
            if original_node.random:
                print(
                    f"assigning random field for new_node {new_node.val} and original_node {original_node.val} with random value of {original_node.random.val}")
                random_node = original_node.random
                val_to_find = random_node.val
                next_val_to_find = random_node.next.val if random_node.next else None
                next_next_val_to_find = random_node.next.next.val if random_node.next and random_node.next.next else None
                index_of_random_node = 0
                for index, node in enumerate(original_nodes):
                    # this can result in the wrong relative node being set where duplicate values
                    node_next_val = node.next.val if node.next else None
                    node_next_next_val = node.next.next.val if node.next and node.next.next else None

                    if node.val == val_to_find and node_next_val == next_val_to_find and node_next_next_val == next_next_val_to_find:
                        print(f"found value {val_to_find} at index {index} of original nodes with val of {node.val}")
                        index_of_random_node = index
                        break
                new_node.random = new_nodes[index_of_random_node]

        new_nodes_display = [(node.val, node.random.val if node.random else None, node.next.val if node.next else None)
                             for node in new_nodes]
        print(f"new nodes {new_nodes_display}")
        print(f"new nodes {new_nodes}")
        return new_nodes[-1]

# This solution is O(n^2) time complexity because in the worst case for each node we loop through all the original nodes
# to find the correct random reference, we also iterate through the list at least twice extra so + 2n
# This solution is O(3n) space complexity because I create a list of the original nodes, create the new nodes and a list of new_nodes
# The solution is also very messy and likely will not work for some specific test cases
# I hacked in the way to find the correct reference by looking ahead twice

# to not have to search in the original nodes for the correct position I could store the original nodes with their index
# either through an extended class or using a pair of (node, index), this would reduce the time complexity to O(n) as
# to assign the random ref I could simply loop through the new nodes, get the random index of the original node and assign

# Is there a way to do this without O(n) space complexity? No because we have to create the new nodes which will be
# O(n), there is likely a way to do it without using lists and just iterating through the linked lists


class Recursion:
    def __init__(self):
        # map of original_node -> copied node
        self.original_to_copied_nodes = {}

    # this is called with the original head of the list
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        # when could head already be in the map? if we have a circular list only?
        if head in self.original_to_copied_nodes:
            return self.original_to_copied_nodes[head]

        copy = Node(head.val)
        self.original_to_copied_nodes[head] = copy
        # recursively copy all nexts until we reach the end of the sequence --> back to front processing
        # then assign the nexts in back to front order
        copy.next = self.copyRandomList(head.next)
        # assign all randoms from the complete list that we have copied
        copy.random = self.original_to_copied_nodes.get(head.random)
        return copy

# This is quite an elegant solution and one where recursion works well because it allows you to process the nodes
# in reverse order and thus create the copy with only a single pass
# The solution is O(n) time and space complexity

class HashMapTwoPass:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}

        # create all copy nodes with only vals
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        cur = head

        # assign all nexts and randoms
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]

# this solution is O(2n) time complexity and O(n) space complexity


class HashMapOnePass:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # utilise default dict to create blank nodes when we haven't already copied the original
        oldToCopy = collections.defaultdict(lambda: Node(0))
        oldToCopy[None] = None

        cur = head
        while cur:
            oldToCopy[cur].val = cur.val
            # nodes area created here by default dict if we haven't seen them
            oldToCopy[cur].next = oldToCopy[cur.next]
            oldToCopy[cur].random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]


class SpaceOptimised:
    class Solution:
        def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
            if head is None:
                return None

            # interleave copy of every node after original node
            l1 = head
            while l1 is not None:
                l2 = Node(l1.val)
                l2.next = l1.next
                l1.next = l2
                l1 = l2.next

            newHead = head.next

            # assign randoms
            l1 = head
            while l1 is not None:
                if l1.random is not None:
                    # copied nodes random = node after original nodes random (another copied node)
                    l1.next.random = l1.random.next
                l1 = l1.next.next

            # break apart interleaved original and copied nodes
            l1 = head
            while l1 is not None:
                l2 = l1.next
                l1.next = l2.next
                if l2.next is not None:
                    l2.next = l2.next.next
                l1 = l1.next

            return newHead

# this solution uses only O(1) extra space