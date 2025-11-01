import math
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        power_of_ten = len(digits) - 1

        number = 0
        for index, digit in enumerate(digits):
            multiplication_factor = math.pow(10, power_of_ten - index)
            number += multiplication_factor * digit
            print(f"digit: {digit}, multiply by {multiplication_factor}, current number {number})")

        new_number = number + 1
        result = []
        print(f"result: {result}, incremented number: {new_number}")
        while new_number:
        # for i in range(10):
            result.append(int(new_number % 10))
            new_number = new_number // 10
            print(f"result: {result}, incremented number: {new_number}")

        return result[::-1]

class MyRecursion:
    def incrementDigit(self, digits, index):

        digit_to_increment = digits[index]
        print(f"digit to increment: {digit_to_increment}")
        if index == 0 and digit_to_increment == 9:
            digits[index] = 0
            digits.insert(0, 1)
        elif digit_to_increment == 9:
            digits[index] = 0
            self.incrementDigit(digits, index - 1)
        else:
            digits[index] = digit_to_increment + 1

    def plusOne(self, digits: List[int]) -> List[int]:
        self.incrementDigit(digits, len(digits) - 1)
        return digits


class RecursionSolution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return [1]

        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            return self.plusOne(digits[:-1]) + [0]