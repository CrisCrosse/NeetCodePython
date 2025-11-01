from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        numbers = self.nums
        numbers.append(val)
        numbers.sort()
        k = self.k
        k_largest = numbers[-k]
        return k_largest


class KthLargestWithHeap:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify(nums)
        print(type(nums))
        self.nums = nums

        while len(self.nums) > k:
            # remove smallest size - k elements from heap
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:
            # remove smallest size - k elements from heap
            # should only be one
            heapq.heappop(self.nums)
        # return smallest element from heap
        return self.nums[0]





