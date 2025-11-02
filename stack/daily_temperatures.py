from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        number_of_days = len(temperatures)
        result = [0] * number_of_days
        stack = []

        for index, temp in enumerate(temperatures):
            print(f"currently at index: {index} and temp: {temp}")
            while stack and temp > stack[-1][1]:
                print(f"current stack: {stack}")
                popped_index, popped_temp = stack.pop()
                print(
                    f"current temp is higher than last stack value with index: {popped_index} and temp: {popped_temp}")
                result[popped_index] = index - popped_index
            stack.append((index, temp))

        return result

#     this solution is O(n) time complexity as we iterate once over the input values
#     and O(n) space complexity as we in the worst case create a stack with n elements


# TODO: I don't understand how this is working, look into dynamic programming principles
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                if res[j] == 0:
                    j = n
                    break
                j += res[j]

            if j < n:
                res[i] = j - i
        return res
