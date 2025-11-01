class BruteForce:
    def reverseBits(self, n: int) -> int:
        binary = ""
        for i in range(32):
            if n & (1 << i):
                binary += "1"
            else:
                binary += "0"

        res = 0
        for i, bit in enumerate(binary[::-1]):
            if bit == "1":
                # res = res | (1 << i)
                # 0|1 --> 1, 1|10 --> 11, not entered because 0, 11|1000 --> 1011
                # iteratively build res through bit shifting and using or to keep previously assigned lesser significance bits
                res |= (1 << i)

        return res

class BitManipulation:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            print(i)

            # get the least significant bit (0 or 1) moving left to right over the binary representation of n
            bit = (n >> i) & 1
            print(bit)

            # put that bit in the reverse position of result
            res += (bit << (31 - i))
            print(res)
        return res