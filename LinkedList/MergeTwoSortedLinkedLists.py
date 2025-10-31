
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        is_list_1_starting = list1.val <= list2.val
        current_node = list1 if is_list_1_starting else list2
        head = current_node
        other_list_node = list2 if is_list_1_starting else list1

        next_node = current_node.next

        while next_node or other_list_node:
            print(f"current node: {current_node.val}")
            if next_node:
                print(f"next node: {next_node.val}")
            else:
                print("next_node is None")
            if other_list_node:
                print(f"other_list_node: {other_list_node.val}")
            else:
                print("other list node is none")

            if not next_node:
                current_node.next = other_list_node
                current_node = other_list_node
                other_list_node = other_list_node.next
            elif not other_list_node:
                current_node.next = next_node
                current_node = next_node
                next_node = next_node.next

            elif other_list_node.val <= next_node.val:
                current_node.next = other_list_node
                current_node = other_list_node
                other_list_node = other_list_node.next
            else:
                current_node.next = next_node
                current_node = next_node
                next_node = next_node.next
        return head

    # this is O(n + m) complexity as we iterate through each list once
    # this is O(1) space complexity because we create 5 data objects per run regardless of list size

