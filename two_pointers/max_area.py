from typing import List


class InitialAttempt:
    def maxArea(self, heights: List[int]) -> int:
        # index = base so can't sort
        largest_area = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                area = (j - i) * min(heights[i], heights[j])
                largest_area = max(area, largest_area)

        return largest_area

    # O(n^2) time complexity because for each element we iterate over every other element
    # But O(1) constant space because we only create have a single value in memory

class TwoPointers:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left, right = 0, len(heights) - 1

        while left < right:
            left_height = heights[left]
            right_height = heights[right]
            print(left_height, right_height)
            area = (right - left) * min(left_height, right_height)
            max_area = max(max_area, area)

            # this solution searches for a max height combination
            if left_height < right_height:
                left += 1
            else:
                right -= 1
        return max_area
    # THis is O(n) time complexity because we iterate over each element at most once
    # This is O(1) space complexity because we only create 4 vars regardless of input size