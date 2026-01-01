from unittest import TestCase
from heap_or_priority_queue.task_scheduler import BruteForce


class TestSolution(TestCase):
    def test_least_interval(self):
        result = BruteForce().leastInterval(["X","X","Y","Y"], n = 2)
