# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class InitialAttempt:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen_nodes = set()

        if not head:
            return False

        while head.next:
            print(f"looking at node {head.val}, next node is {head.next.val}")
            seen_nodes.add(head)
            if head.next in seen_nodes:
                return True
            head = head.next

        return False
#     this solution is O(n) time complexity because in the worst case we have to traverse all n nodes
#     this solution uses O(n) space complexity due to the set; how to reduce this? need to O(1)? need to be able to store
# which nodes have been seen without using extra space

class FastAndSlowPointers:
        def hasCycle(self, head: Optional[ListNode]) -> bool:

            if not head:
                return False

            slow_pointer, fast_pointer = head, head
            while fast_pointer.next and fast_pointer.next.next:
                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next.next
                if slow_pointer == fast_pointer:
                    return True
            return False

#     this solution is O(n) time complexity because in the worst case we have to traverse all n nodes + n nodes in the cycle = 2n = n
#     this solution uses O(1) space complexity because we create only two references regardless of input size

class SimplifiedSolution:
    class Solution:
        def hasCycle(self, head: Optional[ListNode]) -> bool:
            slow_pointer, fast_pointer = head, head
            while fast_pointer and fast_pointer.next:
                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next.next
                if slow_pointer == fast_pointer:
                    return True
            return False
