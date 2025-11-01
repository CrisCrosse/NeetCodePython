from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for number in range(n + 1):
            res.append(bin(number).count("1"))
        return res

class Optimal:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        highest_power_of_two_seen_so_far = 1

        for i in range(1, n + 1):
            print("we are at index ", i)
            print(dp)


            if highest_power_of_two_seen_so_far * 2 == i:
                print(dp[i - highest_power_of_two_seen_so_far:i])
                highest_power_of_two_seen_so_far = i

            print(f"highest power seen so far is: {highest_power_of_two_seen_so_far}, so we offset back this far and add 1 ")

            dp[i] = 1 + dp[i - highest_power_of_two_seen_so_far]

        return dp