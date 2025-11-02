from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_and_index = {}

        for index, number in enumerate(nums):
            other_number_needed = target - number
            if other_number_needed in number_and_index:
                return [number_and_index[other_number_needed], index]
            number_and_index[number] = index

    # this is O(n) time complexity and O(n) space complexity