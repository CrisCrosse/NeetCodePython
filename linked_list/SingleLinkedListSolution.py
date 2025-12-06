from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class BruteForce:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        all_nodes = [head]
        next_node = head.next
        while next_node is not None:
            all_nodes.append(next_node)
            next_node = next_node.next

        for index, node in enumerate(all_nodes):
            if index == 0:
                node.next = None
            else:
                node.next = all_nodes[index - 1]

        return all_nodes[-1]
    # this solution has O(2n) time complexity because we iterate over the whole input list twice
    # this solution has O(n) space complexity because we create a list with length n

class Optimised:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        next_node = head.next
        head.next = None
        previous_node = head

        while next_node is not None:
            print(f"previous node: {previous_node.val}")
            print(f"next node: {next_node.val}")
            node_after_next = next_node.next
            next_node.next = previous_node
            if node_after_next is not None:
                print(f"node_after_next: {node_after_next.val}")
            previous_node = next_node
            next_node = node_after_next

        return previous_node
    # this solution is O(n) time complexity because we traverse the linked list once
    # this solution is O(1) time complexity as we only create 3 objects regardless of linked list length

class Simplified:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous, current = None, head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
    # The setup can be simplified by initialising previous as a None value --> much cleaner
