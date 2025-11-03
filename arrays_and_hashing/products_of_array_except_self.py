from typing import List


class BruteForce:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for index, number in enumerate(nums):
            product = 1
            for j in range(len(nums)):
                print(f"looking at index {j}")
                if index != j:
                    number = nums[j]
                    print(f"multiplying product {product} by {number}")
                    product = product * number
            res.append(product)
        return res
    # This is O(n^2) time complexity
    # it is O(n) space complexity as we create an array of size (n)


# can't get this solution to work due to having 0 values in array (can't divide by 0)
class DivisionSolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        product = 1
        for number in nums:
            product = product * number
        for number in nums:
            res.append(int(product / number))
        return res

class WorkingDivisionSolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0

        # this solution recognises that having one zero or two zeroes alters the pattern,
        # but having more than two zeroes has no extra impact
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt +=  1
        if zero_cnt > 1: return [0] * len(nums)

        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_cnt: res[i] = 0 if c else prod
            else: res[i] = prod // c
        return res

class PrefixSuffix:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        # create two arrays, pref: at the ith element have the product of all elements to the left of i
        # suff: at the ith element have the product of all the elements to the right of i
        # they are padded with 1 at the start and end respectively due to there being no
        # elements left/right of the start/end
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        print(pref)
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        print(suff)
        for i in range(n):
            res[i] = pref[i] * suff[i]
        print(res)
        return res



