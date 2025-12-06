# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class BruteForce:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        seen_nodes = []
        original_head = head
        while head:
            seen_nodes.append(head)
            head = head.next

        if n == len(seen_nodes):
            seen_nodes.pop(0)
            if seen_nodes:
                return seen_nodes[0]
            return None

        if n == 1:
            node_before_final = seen_nodes[-2]
            node_before_final.next = None
            return original_head

        else:
            node_index_to_remove = len(seen_nodes) - n
            node_before = seen_nodes[node_index_to_remove - 1]
            node_after = seen_nodes[node_index_to_remove + 1]
            node_before.next = node_after
            return original_head

# This solution is O(n) for both time and space complexity because we iterate through the whole linked list and
# create a list of nodes


class SpaceOptimisedSolution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        original_head = head
        number_of_nodes = 0
        while head:
            number_of_nodes += 1
            head = head.next

        if n == number_of_nodes:
            return original_head.next


        node_traversals_to_removal_node = number_of_nodes - n
        node_before = original_head
        for i in range(node_traversals_to_removal_node - 1):
            node_before = node_before.next
        print(
            f"node before is {node_before.val}, while node to remove is {node_before.next.val} which is {node_traversals_to_removal_node} jumps from the head")
        node_before.next = node_before.next.next
        return original_head

# this solution is O(n) time complexity because we iterate through the whole list and then alter it, in worst cases 2n
# because we would traverse right to the end again
# But it is O(1) space complexity because we create 4 variables regardless of input size


class OptimalSolution:
    # this solution uses two pointers sliding rightwards with a gap of n until right side reaches end
    # this means you do not have to traverse the list more than once so is slightly better time complexity than above
    # it is also cleaner
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if n = 5 and our list is [1, 2, 3, 4, 5]
        # if n = 2 and our list is [1, 2, 3, 4, 5]
        # dummy is used to store the head value? --> could this work by just storing another ref
        dummy = ListNode(0, head)
        left = dummy
        right = head
        # [0 (left), 1 (right), 2, 3, 4, 5]
        while n > 0:
            right = right.next
            n -= 1
        # [0 (left), 1, 2, 3, 4, 5, None (right) ]
        # [0 (left), 1, 2, 3 (right), 4, 5]

        while right:
            left = left.next
            right = right.next
        # [0 (left), 1, 2, 3, 4, 5, None (right) ]
        # [0, 1, 2 (left), 3, 4, 5 (right)]

        left.next = left.next.next
        # [0 (left), 2, 3, 4, 5, None (right) ]
        # [0, 1, 2 (left), 4, 5 (right)]
        return dummy.next
        # return 2
        # return 1
