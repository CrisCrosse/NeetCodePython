class MySolution:
    def getSumOfDigitsSquared(self, anInt: int) -> int:
        digit_one = anInt // 100
        print(digit_one)
        remainder = anInt % 100
        digit_two = remainder // 10
        print(digit_two)
        remainder = remainder % 10
        digit_three = remainder // 1
        print(digit_three)
        return (digit_one * digit_one) + (digit_two * digit_two) + (digit_three * digit_three)

    def isHappy(self, n: int) -> bool:
        # up to 1000 -> 999, 102, 17
        sum = n
        sequence = []
        while True:
            sum = self.getSumOfDigitsSquared(sum)
            print(f"The sum of squared digits is: {sum}. Original number: {n}")
            if sum in sequence:
                return False
            sequence.append(sum)
            if sum == 1:
                return True
            if sum == n:
                return False

        # THis is O(1) time complexity, worse case is not determined by input but by the sequence length
        #     it is actually log n  time and o 1 space
        # This is O(infinity) time complexity but worse case is sequence is ever growing as the sequence never repeats?



class OptimalSolution:
    # set fast going quicker than slow and if fast catches up to slow then it is an infinite sequence
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumOfSquares(n)

        while slow != fast:
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)
            slow = self.sumOfSquares(slow)
        return True if fast == 1 else False

    def sumOfSquares(self, n: int) -> int:
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output