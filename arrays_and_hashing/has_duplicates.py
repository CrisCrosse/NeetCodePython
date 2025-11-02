from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_numbers = set()
        for number in nums:
            if number in seen_numbers:
                return True
            seen_numbers.add(number)
        return False

    # this is O(n) space and time complexity

class sortingSolution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for index, number in enumerate(nums):
            if index == len(nums) - 1:
                return False
            if nums[index] == nums[index + 1]:
                return True
        return False
    # this is O(n log n) time complexity due to tim sort
    # but O(1) space complexity

class leastCodeSolution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
