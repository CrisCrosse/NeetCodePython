import math

class Solution:
    def hammingWeight(self, n: int) -> int:

        count = 0
        for power in range(32, -1, -1):
            print(f"checking 2 to the power {power}: {math.exp2(power)}")
            print(n)
            if n - math.exp2(power) >= 0:
                count += 1
                n = n - math.exp2(power)
        return count

class BitShiftOne:
    def hammingWeight(self, n: int) -> int:
        count = 0

        for number in range(32):
            # move the 1 number amount of bits to the left eg number = 4 --> 10000 --> 16
            one_bit_shifted = 1 << number

            # if n contains that 1: all other bits in n get set to 0 by the &, the result will be 0 or one_bit_shifted
            if n & one_bit_shifted == one_bit_shifted:
                count += 1

        return count

class BitShiftInput:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            # if the rightmost but is 1
            res += 1 if n & 1 else 0
            # move the next most significant bit into the 1 position
            n >>= 1
        return res

class OptimalSolution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            # this is equivalent to n = n & n-1
            # the n -1 makes the least significant bit a 0 and all preceding bits 1s ie 1000100 --> 1000011
            # then when this is & with n only the original 1s remain: 1000011 & 1000100 => 1000000
            n &= n - 1
            # this loop will run res times so is more efficient than the above which run 32 times, but all are O(1)
            res += 1
        return res

class BuiltInSolution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')