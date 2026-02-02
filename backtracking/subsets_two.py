from typing import List


class FirstAttemptNotWorking:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def subsets(index, cur: List[int]):
            if index == len(nums):
                # the actual solution appends the subset at this point
                return

            current_value = nums[index]
            cur.append(current_value)

            # the actual solution does not append the subset here
            res.append(cur.copy())
            print(f"current element {current_value} at index {index}, combination {cur}")

            subsets(index + 1, cur)
            print(f"current before popping {cur}")
            cur.pop()
            print(f"current after popping {cur}")

            print(f"deciding if to do combinations without current element: {current_value} at index {index}")
            # I am entering this path too often
            # this path is not choosing an element --> I do not need to append to the result when ongoing because there is a path whereby we will not add any
            while nums[index] == current_value:
                index += 1
                if index == len(nums):
                    return
                print(
                    f"iterating to find solutions without {current_value}, found different element {nums[index]} at index {index}, current combination {cur}")
                subsets(index, cur)

        subsets(0, [])
        return res



class BruteForce:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # using a set prevents duplicate tuples being added
        res = set()

        def backtrack(i, subset):
            if i == len(nums):
                # we use tuples because they are hashable, lists are mutable and therefore unhashable as there is no guarantee the object is the same and matches the hash
                res.add(tuple(subset))
                return

            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            backtrack(i + 1, subset)

        nums.sort()
        backtrack(0, [])
        return [list(mySet) for mySet in res]

# Time complexity: O(n * 2^n) for each element we do 2 ^ n recursions?
# Space complexity: O(2 * n)

class BacktrackingOne:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[:])
                return
            subset.append(nums[i])
            backtrack(i+ 1, subset)
            subset.pop()

            # while not on last index and current index is duplicate of next
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res

# Time complexity: O(n * 2^n)
# Space complexity:O(n) extra space. O(2 ^ n) space for the output list.

class BacktrackingTwo:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            print(
                f"starting recursion with index: {i} and element: {nums[i] if i < len(nums) else "Out of bounds"} and subset: {subset}")
            res.append(subset[::])

            # for each element add all possible subsets starting with this element
            for j in range(i, len(nums)):
                print(f"looking at index: {j} value: {nums[j]}")
                # if we are looking at a remaining element (not the first in the iteration from i) and it is a duplicate then skip
                if j > i and nums[j] == nums[j - 1]:
                    print(f"skipping further recursion")
                    # do not recurse further if we are beyond the first index and we have a duplicated element
                    continue
                subset.append(nums[j])
                backtrack(j + 1, subset)
                subset.pop()

            print(
                f"finished recursion with index: {i} and element: {nums[i] if i < len(nums) else "Out of bounds"} and subset: {subset}")

        backtrack(0, [])
        return res

# Time complexity: O(n * 2^n)
# Space complexity:O(n) extra space. O(2 ^ n) space for the output list.
# TODO: could do with a diagram for this one

class Iteration:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()

        length_of_subsets_before_last_recursion = 0

        for i in range(len(nums)):
            print(f"looking at index {i} with value: {nums[i]}")
            # index is prev if we are not on the first element and we are on a duplicate otherwise it is start of sequence
            # ie do not repeat the same subsets for duplicate values, only append to freshly created subsets in last round
            start_index_to_iterate_over = length_of_subsets_before_last_recursion if i >= 1 and nums[i] == nums[
                i - 1] else 0

            length_of_subsets_before_last_recursion = len(res)
            for j in range(start_index_to_iterate_over, length_of_subsets_before_last_recursion):
                print(
                    f"at value {j} in range {start_index_to_iterate_over, length_of_subsets_before_last_recursion}, subset to be appended to is {res[j]}, res is {res}")
                tmp = res[j].copy()
                tmp.append(nums[i])
                res.append(tmp)

        return res

# Time complexity: O(n * 2^n)
# Space complexity:O(n) extra space. O(2 ^ n) space for the output list.