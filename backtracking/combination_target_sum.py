from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return

            # this will initially go through and repeatedly add the first element until we exceed target
            # then we will finish that recursion, remove the last element that put us over target and add the next element
            # this repeats and neatly recurses over the whole list of elements for every possible combination
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i + 1, cur, total)

        # start at the first number with an empty combination giving a sum of 0
        dfs(0, [], 0)
        return res

# The time complexity is O(2 ^ t/m) and the space complexity is O(t/m)
# because the recursive decision tree has 2 outcomes, add the element or do not add it and proceed to next
# and the max height of the tree, or the max elements in a single solution is target (where every element is 1)

# Where t is the given target and m is the minimum value in nums

class Optimal:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                cur.append(nums[j])
                dfs(j, cur, total + nums[j])
                cur.pop()

        dfs(0, [], 0)
        return res

# This solution has the same worst case space and time compleixty but when the solution has exceeded the target it returns
# avoiding exploring paths that are too large