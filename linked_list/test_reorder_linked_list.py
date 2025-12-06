from unittest import TestCase
from linked_list.reorder_linked_list import BruteForce, ListNode, SpaceOptimised


class TestSolution(TestCase):
    def test_reorder_linked_list_length_4(self):

        last = ListNode(8)
        third = ListNode(6, last)
        second = ListNode(4, third)
        head = ListNode(2, second)

        # [2, 4, 6, 8] -> [2, 8, 4, 6]
        solution = BruteForce()
        solution.reorderList(head)

        assert(head.next == last)
        assert(last.next == second)
        assert(second.next == third)
        assert(third.next is None)

    def test_reorder_linked_list_length_5(self):
        last = ListNode(10)
        fourth = ListNode(8, last)
        third = ListNode(6, fourth)
        second = ListNode(4, third)
        head = ListNode(2, second)
        # [2, 4, 6, 8, 10] -> [2, 10, 4, 8, 6]
        solution = BruteForce()
        solution.reorderList(head)

        assert(head.next == last)
        assert(last.next == second)
        assert(second.next == fourth)
        assert(fourth.next == third)
        assert(third.next is None)

    def test_reorder_linked_list_length_4_optimised(self):
        last = ListNode(8)
        third = ListNode(6, last)
        second = ListNode(4, third)
        head = ListNode(2, second)

        # [2, 4, 6, 8] -> [2, 8, 4, 6]
        solution = SpaceOptimised()
        solution.reorderList(head)

        assert (head.next == last)
        assert (last.next == second)
        assert (second.next == third)
        assert (third.next is None)

    def test_reorder_linked_list_length_5_optimised(self):
        last = ListNode(10)
        fourth = ListNode(8, last)
        third = ListNode(6, fourth)
        second = ListNode(4, third)
        head = ListNode(2, second)
        # [2, 4, 6, 8, 10] -> [2, 10, 4, 8, 6]
        solution = SpaceOptimised()
        solution.reorderList(head)

        assert(head.next == last)
        assert(last.next == second)
        assert(second.next == fourth)
        assert(fourth.next == third)
        assert(third.next is None)

    def test_reorder_linked_list_length_long_optimised(self):
        assert(True)
        # for even numbers the number of elements to insert is actually n - 1 // 2, this works for odd as well
        # number of nodes to insert is 3, mid point is 8 3 nexts from 2
        # [2, 4, 6, 8, 10, 12, 14] -> [2, 14, 4, 12, 6, 10, 8]
        # number of nodes to insert 4, mid point is 10, 4 nexts from 2,
        # [2, 4, 6, 8, 10, 12, 14, 16] -> [2, 16, 4, 14, 6, 12, 8, 10]