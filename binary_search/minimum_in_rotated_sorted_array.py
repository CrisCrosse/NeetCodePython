from typing import List


class InitialAttempt:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        current_min = 1001

        # [3, 4, 5, 6, 1, 2]
        # [5, 6, 1, 2, 3, 4]
        # [6, 1, 2, 3, 4, 5]
        # [1, 2, 3, 4, 5, 6]

        while left <= right:
            middle = left + (right - left) // 2
            print(nums[left], nums[middle], nums[right])
            if nums[middle] < nums[right]:
                current_min = min(current_min, nums[middle])
                right = middle - 1
            else:
                current_min = min(current_min, nums[right])
                left = middle + 1
        return current_min

        # if left is less than middle is less than right:
        # non rotated sequence and take left? is that guaranteed
        # if left is less than middle but both are greater than right

        # binary search where we do not know the ends of
        # the ascending sequence

class OptimalSolution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        # exit when left exceeds right
        while l < r:
            m = l + (r - l) // 2
            # no setting of min, only shifting search to find min
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        # return the finishing element
        return nums[l]