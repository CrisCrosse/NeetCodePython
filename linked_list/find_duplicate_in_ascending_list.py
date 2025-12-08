from typing import List


class HashSet:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()

        for number in nums:
            if number in seen:
                return number
            seen.add(number)
    # This solution is O(n) time complexity and O(n) space complexity due to the hash set storage

class NegativeMarking:
    def findDuplicate(self, nums: List[int]) -> int:
        for number in nums:
            index = abs(number) - 1
            value_at_index = nums[index]
            # use numbers value as index into this array, we have n + repeating len array and n values so this is safe
            if value_at_index < 0:
                return abs(number)

            # set the value pointed to be negative, we only come back to this value for the repeating index/value
            nums[index] = value_at_index * -1

class LinkedListFloydsAlgo:
    def findDuplicate(self, nums: List[int]) -> int:
        # find intersection of fast and slow pointer
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        intersection = slow

        # set slow pointer with intersection and entry
        slow_one = 0
        slow_two = intersection
        while True:
            slow_one = nums[slow_one]
            slow_two = nums[slow_two]
            # intersection of slows is start of cycle
            if slow_one == slow_two:
                return slow_one

