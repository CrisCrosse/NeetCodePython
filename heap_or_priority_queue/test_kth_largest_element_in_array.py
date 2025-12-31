from unittest import TestCase
from heap_or_priority_queue.kth_largest_element_in_array import QuickSelect


class TestQuickSelect(TestCase):
    def test_quick_select(self):
        result = QuickSelect().findKthLargest([2,3,1,1,5,1,5,4], 3)
