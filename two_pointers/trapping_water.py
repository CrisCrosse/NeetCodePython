from typing import List


class AnAttempt:
    # 7/22 test cases correct
    def trap(self, height: List[int]) -> int:

        left, right = 0, 0
        max_index = len(height) - 1
        result = 0

        while left < max_index:
            left_height = height[left]

            if left_height > 0:
                # possible trap --> search right
                current_trap = 0
                areas_since_left_trap = []
                possible_right_trap_index = []
                # min_height_in_trap = left_height
                while right < max_index:
                    right += 1
                    right_height = height[right]
                    terrain_heights_ = []
                    if right_height < left_height:
                        areas_since_left_trap.append(left_height - right_height)
                        # if right_height > min_height_in_trap:
                        #     possible_right_trap_index.append(right)
                        # min_height_in_trap = min(right_height, min_height_in_trap)
                    else:
                        # end of trap found with tall right, add current trap area
                        current_trap = sum(areas_since_left_trap)
                        result += current_trap
                        # search from end of current trap
                        left = right
                        break
                if right == max_index:
                    # did not break out of loop, reached end with no tall right trap
                    # case where left trap is found, but no valid right trap before end
                    if left == max_index:
                        break
                    else:
                        # can't always move on because left could be the start of the trap its just not full sized
                        left += 1
                        right = left

                    # and areas_since_left_trap

                    # max_water_area_in_sequence = areas_since_left_trap[0]
                    # for water_area in areas_since_left_trap:
                    #     if water_area < max_water_area_in_sequence:
                    #         # we have the dip

                    #     else:
                    #         max_water_area_in_sequence = max(water_area, max_water_area_in_sequence)
                    #     #  there needs to be a dip in terrain for a trap


            else:
                left += 1
                right += 1

        return result

class WorkingSolution:
    def searchForRightTrapOfHeight(self, right: int, height_to_find: int, max_index: int, height: List[int]) -> tuple[int, int]:
        # print(f"searching for right trap of at least height {height_to_find} from index {right}")
        original_right = right
        trapSize = 0

        while right <= max_index:
            right_height = height[right]

            if right_height >= height_to_find:
                # we have found the desired trap
                return (right, trapSize)

            trapSize += height_to_find - right_height
            # print(f"added water volume {height_to_find - right_height} to current trap due to trap height of {height_to_find} and terrain height of {right_height}")
            right += 1

        return self.searchForRightTrapOfHeight(original_right, height_to_find - 1, max_index, height)

    def trap(self, height: List[int]) -> int:

        left, right = 0, 0
        max_index = len(height) - 1
        result = 0

        while left < max_index:
            left_height = height[left]
            if left_height == 0:
                left += 1
                right += 1
                continue
            right, trapSize = self.searchForRightTrapOfHeight(right + 1, left_height, max_index, height)
            print(f"found a trap between {left_height} and {height[right]} with a size of {trapSize}")
            print(f"left and right pointers shifted to index {right}")
            left = right
            result += trapSize

        return result

#     This solution is O(n^2) worse case time complexity as we have nested and recursive loops
# This solution is the same space complexity due to the recursion


class BruteForce:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        res = 0

        for i in range(n):
            leftMax = rightMax = height[i]

            # search the array at each position for the left and right max
            for j in range(i):
                leftMax = max(leftMax, height[j])
            for j in range(i + 1, n):
                rightMax = max(rightMax, height[j])

            res += min(leftMax, rightMax) - height[i]
        return res

# This solution is O(n^2) time complexity and O(1) space

class PrefixAndSuffixArrays:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        leftMax = [0] * n
        rightMax = [0] * n

        leftMax[0] = height[0]
        for i in range(1, n):
            # left max is the maximum value seen so far, starting from 0 index up to index i
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            # right max is the maximum value seen so far, starting at the end index and going in reverse order to index i
            rightMax[i] = max(rightMax[i + 1], height[i])

        res = 0
        for i in range(n):
            res += min(leftMax[i], rightMax[i]) - height[i]
        return res

# This solution is O(n) time complexity and space complexity because it creates two arrays of length n and iterates through
# the input array 3 n times


class TwoPointers:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res

# This solution is O(n) time complexity because it only iterates over the list once
# And it is O(1) space because we only create 5 int variables

class Stack:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        # a stack of height indexes
        # The stack actually maintains the left and right trap we have seen up to now, when we encounter a new max value it resets to just a left trap
        # quite clever but not one that would be easy to come up with organically
        stack = []
        res = 0

        # example: --> 3, 0 , 1, 2, 3 --> trap of 6 volume
        for i in range(len(height)):

            # if current height is greater than or equal top of stack height
            # we enter this while loop first evaluating index 2 with [0, 1] on stack for values [3, 0]
            # now we have [0, 2] on stack for values [3, 1] as we popped the 0, evaluating index 3 with height 2
            # now we have [0, 3] on stack for values [3, 2] as we popped 1, evaluating index 4 of height 3
            while stack and height[i] >= height[stack[-1]]:
                # remove top of stack
                # this is 0 in example
                # then 1
                # remove 2 height with index 3 from stack, we go through the while loop again and pop the remaining left value
                # end up with [4] --> height 3 on stack
                mid = height[stack.pop()]

                if stack:
                    # right = 1, left = 3
                    # right = 2, left = 3
                    # right = 3, left = 3
                    right = height[i]
                    left = height[stack[-1]]
                    h = min(right, left) - mid
                    # initial width = 1
                    # second time we enter here width is 2
                    # third time is 3
                    w = i - stack[-1] - 1
                    res += h * w

            stack.append(i)
        return res