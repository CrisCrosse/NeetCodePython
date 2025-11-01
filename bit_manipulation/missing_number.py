from os.path import samefile
from typing import List


class SortingSolution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        largest_number = nums[-1]

        for number in range(largest_number + 1):
            if number not in nums:
                return number
        else:
            return largest_number + 1
        # this solution is O(n log n) due to the sort, we also do an O(n) as we iterate over the whole list of n elements in the worst case
        # this solution is O(1) for space complexity because we only ever have larges_number and number in memory and sort the array in place

class SetSolution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        for number in range(len(nums) + 1):
            if number not in num_set:
                return number

class ExclusiveOrSolution:

    # TODO: requires more thought
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xorr = n
        for i in range(n):
            print(f"i: {i}, nums[i] {nums[i]}, xorr: {xorr}")
            print(nums[i])
            xorr ^= i ^ nums[i]
            print(f"xorr after operation: {xorr}")
        return xorr