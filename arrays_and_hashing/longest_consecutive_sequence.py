from typing import List


class FirstAttempt:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        res = 0

        if not len(nums):
            return 0

        previous_value = nums[0]
        current_consecutive_streak = 0
        for index in range(1, len(nums)):
            number = nums[index]
            print(
                f"previous value: {previous_value}, number: {number}, consecutive streak {current_consecutive_streak}, result {res}")
            if number == previous_value + 1:
                current_consecutive_streak += 1
                if current_consecutive_streak > res:
                    res = current_consecutive_streak
                previous_value = number
            if number == previous_value:
                continue
            else:
                current_consecutive_streak = 0
                previous_value = number

        return res + 1

    # O(n + n log(n)) time complexity due to sorting algorithm then looping over n elements

class Optimal:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest