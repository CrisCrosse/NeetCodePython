import heapq
from typing import List


class FirstAttempt:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)

        for num in nums:
            # make number negative to switch min heap to max heap
            heapq.heappush(heap, -num)

        print(heap)
        # nonsense value to stop interpreter complaining, k being positive is a constraint
        result = -1
        while k:
            result = - heapq.heappop(heap)
            k -= 1

        return result

# This solution is O((n + k) logn) time complexity because we do the log n push and pop operations first n times then
# k times
# This solution is O(n) space complexity because we create a heap of n items

class RestrictHeapSize:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heapq.heappop(heap)

# This solution reduces space complexity to O(k) as the heap maintains k length,
# Due to reducing the size of the heap it makes the push and pop operations more efficient (log k instead of log n):
# but we still do O((n + (n - k)) log k )

class BuiltInMethod:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]
# This solition as above is O(k) space complexity and apparently is O(n log k) time complexity

class Sorting:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]
# This solution is O(n log n) time complexity due to timsort
# This solution is O(n) space complexity based on the input value, but uses no additional space --> tim sort is in place

class QuickSelect:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # index of kth largest element
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, pivot_index = nums[r], l
            for i in range(l, r):
                # if number is less than or equal to pivot; swap pivot and number, move pivot index to right
                # This has no effect until a number greater than pivot has been encountered and the pivot index does not move along
                if nums[i] <= pivot:
                    # move current number before last element that was greater than pivot
                    nums[pivot_index], nums[i] = nums[i], nums[pivot_index]
                    pivot_index += 1

            # move pivot to pivot index
            nums[pivot_index], nums[r] = nums[r], nums[pivot_index]

            # recurse
            if pivot_index > k:
                return quickSelect(l, pivot_index - 1)
            elif pivot_index < k:
                return quickSelect(pivot_index + 1, r)
            else:
                return nums[pivot_index]

        return quickSelect(0, len(nums) - 1)