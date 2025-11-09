from collections import defaultdict
from typing import List

class FirstAttempt:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []

        for i, number in enumerate(nums):
            # print(f"first index: {i} with value {number}")
            for j in range(i + 1, len(nums)):
                # print(f"second index: {j} with value {nums[j]}")
                if j > len(nums) - 1:
                    break
                for k in range(j + 1, len(nums)):
                    # print(f"third index: {k} with value {nums[k]}")
                    if k > len(nums) - 1:
                        break
                    if number + nums[j] + nums[k] == 0:
                        # print(f"answer found: {number} + {nums[j]} + {nums[k]}")
                        results.append([number, nums[j], nums[k]])

        for result in results:
            result.sort()

        # deduplicate
        for index in range(len(results)):
            print(len(results))
            if index > len(results) - 1:
                break
            second_index = index + 1
            while True:
                if second_index > len(results) - 1:
                    break
                if results[index] == results[second_index]:
                    results.pop(second_index)
                else:
                    second_index += 1

        return results

    # this is O(n^3) time complexity in the worst case because for each element we iterate over the whole list (its really list - index three times) three times
    # it is O(n) space complexity because the result array will scale with input


class BinarySearch:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        print(len(nums))
        for i in range(len(nums)):
            if i + 1 < len(nums):
                for j in range(i + 1, len(nums)):
                    target_number = - nums[i] - nums[j]
                    print(f"first number: {nums[i]}, second number: {nums[j]}, target number: {target_number}")

                    # binary search for target number in rest of list:
                    # this does not work because we need a sorted list for binary search --> could sort
                    # is this inclusive of j?
                    if j + 1 < len(nums):
                        print("attempting binary search for target")
                        left, right = j + 1, len(nums) - 1
                        while left < right:
                            print(nums)
                            print(f"left item: {nums[left]}, right item: {nums[right]}")
                            mid = left + (right - left) // 2
                            if nums[mid] > target_number:
                                right = mid - 1
                            if nums[mid] < target_number:
                                left = mid + 1
                            else:
                                result.append([nums[i], nums[j], nums[mid]])

        return result

from typing import List

class FirstAttempt:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []

        for i, number in enumerate(nums):
            # print(f"first index: {i} with value {number}")
            for j in range(i + 1, len(nums)):
                # print(f"second index: {j} with value {nums[j]}")
                if j > len(nums) - 1:
                    break
                for k in range(j + 1, len(nums)):
                    # print(f"third index: {k} with value {nums[k]}")
                    if k > len(nums) - 1:
                        break
                    if number + nums[j] + nums[k] == 0:
                        # print(f"answer found: {number} + {nums[j]} + {nums[k]}")
                        results.append([number, nums[j], nums[k]])

        for result in results:
            result.sort()

        # deduplicate
        for index in range(len(results)):
            print(len(results))
            if index > len(results) - 1:
                break
            second_index = index + 1
            while True:
                if second_index > len(results) - 1:
                    break
                if results[index] == results[second_index]:
                    results.pop(second_index)
                else:
                    second_index += 1

        return results

    # this is O(n^3) time complexity in the worst case because for each element we iterate over the whole list (its really list - index three times) three times
    # it is O(n) space complexity because the result array will scale with input

class BetterOnCubedTimeSolution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        # don't need the checks on the indexes as max value is already len(nums)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = [nums[i], nums[j], nums[k]]
                        # convert list result into a tuple so it is hashable to add to a set to deduplicate
                        res.add(tuple(tmp))
        return [list(i) for i in res]

class OnsquaredTimeComplexityUsingHashMap:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        res = []
        for i in range(len(nums)):
            print("iterating on i")
            print(count, nums[i])
            count[nums[i]] -= 1
            # if not the first index and this and the previous element are equal do nothing
            if i and nums[i] == nums[i - 1]:
                continue

            # for all the indexes after i
            for j in range(i + 1, len(nums)):
                # reduce the count of that element (something to do with deduping I think)
                print("iterating on j")
                print(count, nums[j])
                count[nums[j]] -= 1

                # if j is not the subsequent index after i and this and the previous element are equal do nothing
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                # get the target value
                target = -(nums[i] + nums[j])
                print(count, target)
                # we have the target in count
                if count[target] > 0:
                    res.append([nums[i], nums[j], target])

            # then recreate the counts as before we looped through for j
            for j in range(i + 1, len(nums)):
                count[nums[j]] += 1
        return res

class TwoPointers:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # only do this up till the first positive element
            if a > 0:
                break

            # if not the first element and a is the same as the last element skip this iteration
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res