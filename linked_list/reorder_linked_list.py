
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class BruteForce:
    def reorderList(self, head: Optional[ListNode]) -> None:
        seen_nodes = []

        while head:
            seen_nodes.append(head)
            head = head.next

        seen_nodes_val = [node.val for node in seen_nodes]
        print(seen_nodes_val)

        print("popped first ndoe")
        seen_nodes_val = [node.val for node in seen_nodes]
        print(seen_nodes_val)
        last_node = None
        while seen_nodes:
            first_node = seen_nodes.pop(0)
            if last_node:
                last_node.next = first_node
            if not seen_nodes:
                first_node.next = None
                break
            last_node = seen_nodes.pop()
            first_node.next = last_node
            last_node.next = None

            print(first_node.val, last_node.val)

# This solution is O(n) time complexity because we iterate through each element in the list to create the seen_nodes, we also
# do list comprehension twice and then iterate through n/2 so its actually 3.5n but this simplifies to n
# This solution is O(n) space complexity because we create a new list of n size

class SpaceOptimised:
    def reorderList(self, head: Optional[ListNode]) -> None:
        pointer = head
        count_nodes = 0
        seen_nodes = []
        while pointer:
            count_nodes += 1
            seen_nodes.append(pointer)
            pointer = pointer.next

        # remove logic for this for actual submission
        seen_nodes_display = [node.val for node in seen_nodes]

        print(f"nodes: {seen_nodes_display}")
        print(f"total nodes: {count_nodes}")
        number_of_nodes_to_insert = count_nodes // 2
        print(f"nodes to insert: {number_of_nodes_to_insert}")

        # [2, 4, 6, 8] [2, 4, 6, 8, 10]
        mid_point_node = head
        for i in range((count_nodes - 1) // 2):
            mid_point_node = mid_point_node.next
        print(f"mid point node: {mid_point_node.val}")

        for i in range(number_of_nodes_to_insert):
            print(f"inserting {i}th node")
            # find node to insert from mid_point_node
            node_to_insert = mid_point_node
            for j in range(number_of_nodes_to_insert - i):
                node_to_insert = node_to_insert.next
                print(f"finding node_to_insert, current {node_to_insert.val} on step {j}")

            print(f"head: {head.val}")
            print(f"node_to_insert: {node_to_insert.val}")
            # take next of current node into temp
            temp = head.next
            # current_node_next is node to insert
            head.next = node_to_insert
            # node to insert next is temp
            node_to_insert.next = temp
            print(f"heads new next is: {head.next.val}")
            print(f"inserted nodes new next is: {node_to_insert.next.val}")

            # move head along, could this ever be None?
            head = temp
            # repeat until we have reached number of nodes to insert
        head.next = None


class SpaceOptimisedCleaned:
    def reorderList(self, head: Optional[ListNode]) -> None:
        pointer = head
        count_nodes = 0
        while pointer:
            count_nodes += 1
            pointer = pointer.next


        number_of_nodes_to_insert = count_nodes // 2

        # [2, 4, 6, 8] [2, 4, 6, 8, 10]
        mid_point_node = head
        for i in range((count_nodes - 1) // 2):
            mid_point_node = mid_point_node.next

        for i in range(number_of_nodes_to_insert):
            # find node to insert from mid_point_node
            node_to_insert = mid_point_node
            for j in range(number_of_nodes_to_insert - i):
                node_to_insert = node_to_insert.next

            # take next of current node into temp
            temp = head.next
            # current_node_next is node to insert
            head.next = node_to_insert
            # node to insert next is temp
            node_to_insert.next = temp

            # move head along, could this ever be None?
            head = temp
            # repeat until we have reached number of nodes to insert
        head.next = None

# This is the optimal solution with a O(n) time complexity and a O(1) space complexity

class TheirVersionOfMergingTheTwoEndsOfTheLinkedList:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # slow is at the mid-point when fast reaches the end and breaks from the loop due to next being None
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half of the linked list
        second = slow.next
        # make the last element of the left side of the list point to nothing at the end
        # and initial element in this list also will point to nothing
        prev = slow.next = None
        while second:
            # reverse linked list
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge the two lists, second is now at the final element of the original list with the direction of linkages reversed
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

#         This is slightly nicer than my approach due to not using maths





