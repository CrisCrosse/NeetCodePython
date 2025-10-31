from typing import List

class FirstTrySolution:
    def subset(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        if len(nums) == 0:
            return subsets
        subsets.append(nums)
        if len(nums) == 1:
            return subsets
        for number in nums:
            subsets.append([number])

        for index, number in enumerate(nums):
            number_of_elements_left_in_list = len(nums) - index
            for i in range(1, number_of_elements_left_in_list):
                subsets.append([number, nums[index + i]])

        print(subsets)
        return subsets

class IterativeSolution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for number in nums:
            print()
            print()
            print(f"number: {number}")
            size = len(res)
            for i in range(size):
                subset = res[i]
                print(f"subset: {subset}")
                new_subset = subset + [number]
                print(f"new subset with number: {new_subset}")
                res.append(new_subset)

        return res

class BitSolution:
    def bitsubsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for i in range(1 << n):
            subset = [nums[j] for j in range(n) if (i & (1 << j))]
            print(f"i: {i}")
            print(subset)
            res.append(subset)
        return res