from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while True:
            print(stones)
            if len(stones) == 1:
                return stones[0]
            if len(stones) == 0:
                return 0
            top_rock = stones.pop()
            next_rock = stones.pop()
            print(f"top rock: {top_rock}")
            print(f"next rock: {next_rock}")
            if top_rock > next_rock:
                remaining_rock = top_rock - next_rock
                print(f"appending remaining rock of weight: {remaining_rock}")
                stones.append(remaining_rock)
                stones.sort()
            else:
                print("rocks destroyed")

        # a max heap would simplify this
        # this method is worst case O((n log(n)) ^ 2) because we run the .sort algorithm which uses timsort (O(n log n)) for every time there is a remaining rock
        # it is O(n) space complexity because we do in place sorting

class SolutionBinarySearch:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        n = len(stones)

        while n > 1:
            cur = stones.pop() - stones.pop()
            n -= 2
            if cur > 0:
                print(cur)
                l, r = 0, n
                while l < r:
                    mid = (l + r) // 2
                    if stones[mid] < cur:
                        l = mid + 1
                    else:
                        r = mid
                pos = l
                print(f"pos to add stone: {pos}")
                n += 1
                stones.append(0)

                for i in range(n - 1, pos, -1):
                    # iterate through list in reverese order
                    print(stones)
                    # set this element to the previous element --> shift all elements down to pos right one
                    stones[i] = stones[i - 1]
                stones[pos] = cur
                print(stones)

        return stones[0] if n > 0 else 0

    # Time complexity O(n^2)
    # SPace: O(1) or O(n) depending on sort algo

class NegativeHeapSolution:
        def lastStoneWeight(self, stones: List[int]) -> int:
            stones = [-stone for stone in stones]
            # make all the stones negative, so that a min heap where you pop the min number actually acts on the greatest absolute value
            heapq.heapify(stones)

            while len(stones) > 1:
                print(stones)
                heaviest_rock = heapq.heappop(stones)
                next_heaviest_rock = heapq.heappop(stones)
                remaining_rock = heaviest_rock - next_heaviest_rock
                print(f"heaviest rock: {heaviest_rock}")
                print(f"next heaviest rock: {next_heaviest_rock}")
                print(f"remaining rock: {remaining_rock}")
                if remaining_rock < 0:
                    heapq.heappush(stones, remaining_rock)

            return -stones[0] if len(stones) == 1 else 0
