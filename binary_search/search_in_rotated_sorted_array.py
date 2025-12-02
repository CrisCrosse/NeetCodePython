from typing import List

# can optimise this by only searching left or right hand side, by checking if target is between pivot and the last element in nums
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.findLowestNumberPivotIndex(nums)

        left_array = nums[:pivot]
        target_index = self.findTargetsIndexInSortedArray(left_array, target)
        if target_index != -1:
            return target_index

        right_array = nums[pivot:]
        target_index = self.findTargetsIndexInSortedArray(right_array, target)
        if target_index != -1:
            return len(left_array) + target_index
        return target_index

    def findLowestNumberPivotIndex(self, nums: List[int]) -> int:
        # [1, 2, 3, 4, 5, 6]
        # [3, 4, 5, 6, 1, 2]
        # [5, 6, 1, 2, 3, 4]
        left, right = 0, len(nums) - 1

        while left < right:
            middle = left + (right - left) // 2

            if nums[middle] < nums[right]:
                right = middle
            else:
                left = middle + 1
        print(f"lowest number pivot is {nums[left]} at index {left}")
        return left

    def findTargetsIndexInSortedArray(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2

            if nums[middle] == target:
                print(f"found target value {target} at index {middle} in array {nums}")
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        print(f"did not find target value {target} in array {nums}")
        return - 1


# you can do this in one pass, but you need to switch your search pattern depending on where the break is:

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # if you have a monotonous increasing sequence to the left, so the pivot is elsewhere
            if nums[l] <= nums[mid]:
                # take right hand side if target out of bounds of the increasing sequence
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            # the break point is on the left hand side
            else:
                #  take the left hand side if target is out of bounds of the increasing sequence
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1