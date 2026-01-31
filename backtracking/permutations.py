from typing import List


class MyInitialAttempt:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []

        frequency_dict = {}
        for number in nums:
            current_frequency = frequency_dict.get(number, 0)
            frequency_dict[number] = current_frequency + 1
        print(frequency_dict)

        def permute(curr, frequency_dict):
            print(f"entering permutation recursion with combination {curr}")
            print(f"current frequency_dict {frequency_dict} at {id(frequency_dict)}")

            if len(curr) == len(nums):
                output.append(curr.copy())
                return

            keys = list(frequency_dict.keys())
            original_frequency_dict = frequency_dict.copy()
            for key in keys:
                dict_for_this_recursion = original_frequency_dict.copy()
                current_frequency = dict_for_this_recursion[key]
                if current_frequency == 1:
                    del dict_for_this_recursion[key]
                else:
                    dict_for_this_recursion[key] = current_frequency - 1
                curr.append(key)
                # we finish the whole permutation recurse for 1 before entering with 2,
                permute(curr, dict_for_this_recursion)
                curr.pop()

        permute([], frequency_dict)

        return output

class RecursionSolution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])
        print(f"perms is {perms} with nums {nums}")
        res = []
        for p in perms:
            # for each position where we could add an element: no of indexes plus one
            for i in range(len(p) + 1):
                p_copy = p.copy()
                # insert the first element remaining in nums into index
                p_copy.insert(i, nums[0])
                res.append(p_copy)
                print(f"p: {p}, i: {i}, p_copy: {p_copy}")
        return res

# Time complexity: O(n! * n^2)
# Space complexity: O(n! * n) for the output list.

class IterationSolution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for num in nums:
            new_perms = []
            for p in perms:
                # for each possible position in the permutation, add the number
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, num)
                    new_perms.append(p_copy)
            perms = new_perms
        return perms

# Time complexity: O(n! * n^2)
# Space complexity: O(n! * n) for the output list.


class BackTrackSolution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], nums, [False] * len(nums))
        return self.res

    def backtrack(self, perm: List[int], nums: List[int], pick: List[bool]):
        if len(perm) == len(nums):
            self.res.append(perm[:])
            return
        for i in range(len(nums)):
            # if not yet used number
            if not pick[i]:
                # add to permutation
                perm.append(nums[i])
                # mark as used
                pick[i] = True
                # add all possible combinations starting with this number
                self.backtrack(perm, nums, pick)
                perm.pop()
                # remove the number and allow it to be used in other places than first
                pick[i] = False

# Time complexity: O(n! * n)
# Space complexity: O(n! * n) for the output list.


class BacktrackWithBitMask:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], nums, 0)
        return self.res

    def backtrack(self, perm: List[int], nums: List[int], mask: int):
        # mask is initially 0 so bits: 00000000000 ...
        if len(perm) == len(nums):
            self.res.append(perm[:])
            return
        for i in range(len(nums)):
            # if bit at index i from the left is not already used (has been marked as one)
            if not (mask & (1 << i)):
                perm.append(nums[i])
                # using or sets the mask bit at i indexes from the left to 1
                self.backtrack(perm, nums, mask | (1 << i))
                perm.pop()

# Time complexity: O(n! * n)
# Space complexity: O(n! * n) for the output list.
# but quicker lookups of number already used?


class OptimalBacktracking:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(nums, 0)
        return self.res

    def backtrack(self, nums: List[int], idx: int):
        if idx == len(nums):
            self.res.append(nums[:])
            return
        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            self.backtrack(nums, idx + 1)
            nums[idx], nums[i] = nums[i], nums[idx]

# Time complexity: O(n! * n)
# Space complexity: O(n! * n) for the output list.
# optimal due to in place swappring