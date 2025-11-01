from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bit_shift = 0
        for number in nums:
            bit_shift = number ^ bit_shift
        return bit_shift
    # this is O(n) time complexity and O(1) space complexity

class SortingSolution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)

        for index in range(0, len(nums), 2):
            print(f"checking {nums[index]} at index: {index}")
            if index == len(nums) - 1:
                return nums[index]
            # this works locally however on the neet code website this is not does not assert correctly (for negative numbers?) replacing with != worked
            if nums[index] is not nums[index + 1]:
                print(f"contigous two numbers didn't match {nums[index]} {nums[index+1]}")
                return nums[index]

class TheirSortSolution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        i = 0
        while i < len(nums) - 1:
            print(i)
            print(f"checking index {i} value: {nums[i]}")
            if nums[i] == nums[i + 1]:
                i += 2
            else:
                return nums[i]
        return nums[i]