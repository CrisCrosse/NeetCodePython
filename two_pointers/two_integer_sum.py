from typing import List


class BruteForceButOSpaceSolution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, numberi in enumerate(numbers):
            for j, numberj in enumerate(numbers):
                if i != j and numberi + numberj == target:
                    return [i + 1, j + 1]


class OptimisedTimeOnlogn01SpaceSolution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, numberi in enumerate(numbers):
            # binary search for matching number
            complementary_number = target - numberi
            left_index = i + 1
            right_index = len(numbers) - 1

            while (left_index <= right_index):
                mid_index = left_index + (right_index - left_index) // 2
                print(f"Middle Index: {mid_index}")
                mid_number = numbers[mid_index]

                print(f"Middle number: {mid_number}")
                if mid_number == complementary_number:
                    return [i + 1, mid_index + 1]
                elif mid_number > complementary_number:
                    right_index = mid_index - 1
                else:
                    left_index = mid_index + 1

            # this should satisfy the O(1) space complexity because we create a constant number of objects per input
            # this should be O(n log n) time complexity because we in the worst case iterate till the penultimate element and then binary search for the remaining element?

class OptimisedTimeOn01SpaceSolution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers_and_indices_dict = {}
        for i, number in enumerate(numbers):
            complementary_number = target - number
            if complementary_number in numbers_and_indices_dict:
                return [numbers_and_indices_dict[complementary_number] + 1, i + 1]
            numbers_and_indices_dict[number] = i

            # this should satisfy the O(1) space complexity because we create a constant number of objects per input length
            # this should be O(n) time complexity because we only iterate through the list once