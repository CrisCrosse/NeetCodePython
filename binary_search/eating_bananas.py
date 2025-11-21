import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        number_of_piles = len(piles)
        if h == number_of_piles:
            return max(piles)
        if number_of_piles == 1:
            pile_size = piles[0]
            if pile_size % h == 0:
                return int(piles[0] / h)
            else:
                return int((piles[0] // h) + 1)

        left = 0
        right = max(piles)
        while True:
            middle = left + (right - left) // 2
            print(f"trying rate {middle}")
            hours_to_eat_with_current_rate = self.hoursToEatPile(piles, middle)
            if hours_to_eat_with_current_rate <= h:
                if self.hoursToEatPile(piles, middle - 1) > h:
                    print(
                        f"previous rate {middle - 1} is too quick whilst this rate {middle} is quick enough so use this rate")
                    return middle
                else:
                    print(f"rate was too quick going to lower rate")
                    right = middle
            else:
                if self.hoursToEatPile(piles, middle + 1) < h:
                    print(f"next rate {middle + 1} is quick enough whilst this rate {middle} is too slow so use next")
                    return middle + 1
                else:
                    print(f"rate was too slow going to increase rate")
                    left = middle

    def hoursToEatPile(self, piles: List[int], rate: int):
        if rate == 0:
            return -1
        total_hours = 0
        for pile in piles:
            if pile % rate == 0:
                total_hours += pile / rate
            else:
                total_hours += pile // rate + 1
        return total_hours


class OptimalSolution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            #     if we finished eating before we had to
            if totalTime <= h:
                # our new slowest rate is this rate
                res = k
                # search the left hand side of remaining rates
                r = k - 1
            else:
                l = k + 1
        return res

