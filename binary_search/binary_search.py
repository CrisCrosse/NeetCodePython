class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while (left <= right):
            print(f"left index: {left}, right index: {right}")
            mid_point = left + (right - left) // 2
            mid_value = nums[mid_point]
            print(f"mid index: {mid_point} with a value of: {mid_value}")
            if mid_value < target:
                left = mid_point + 1
            elif mid_value > target:
                right = mid_point - 1
            else:
                return mid_point
        return -1