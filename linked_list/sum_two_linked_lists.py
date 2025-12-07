# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_node, l2_node = l1, l2
        carry_over = 0
        previous_node, head = None, None
        while l1_node or l2_node:
            # default values to 0 so we can continue summing for unevenly sized l1 and l2
            l1_val = l1_node.val if l1_node else 0
            l2_val = l2_node.val if l2_node else 0

            # work out what current digit is and if we need to carry over a 1
            digit = l1_val + l2_val + carry_over
            if digit > 9:
                carry_over = digit // 10
                digit = digit % 10
            else:
                carry_over = 0

            # create digit node and link to previous digit
            node = ListNode(digit)
            if previous_node:
                previous_node.next = node
            else:
                head = node

            # iterate onto next set of digits
            previous_node = node
            if l1_node:
                l1_node = l1_node.next
            if l2_node:
                l2_node = l2_node.next

        if carry_over > 0:
            node.next = ListNode(carry_over)
        #
        # # display logic
        # sum_digits = []
        # sum_head = head
        # while sum_head:
        #     sum_digits.append(sum_head.val)
        #     sum_head = sum_head.next
        # print(f"sum digits in ascending order: {sum_digits}")

        return head

# This solution is O(n + m) time complexity because we iterate over the lists once (n is length of longer list)
# This solution is O(n) space complexity as we create n + 1 max additional nodes for the output

# could this be improved, I don't think so because you have to iterate over the all the digits,
# and you have to return the specified linked list


class Recursion:
    def add(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int) -> Optional[ListNode]:
        if not l1 and not l2 and carry == 0:
            return None

        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        carry, val = divmod(v1 + v2 + carry, 10)

        next_node = self.add(
            l1.next if l1 else None,
            l2.next if l2 else None,
            carry
        )
        return ListNode(val, next_node)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.add(l1, l2, 0)