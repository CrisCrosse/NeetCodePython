from typing import List


class InitialAttempt:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_chars = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"]}

        result = []
        def recurse(index, curr):
            if not digits:
                return
            if index == len(digits):
                result.append(curr)
                return

            digit = int(digits[index])
            chars = digit_to_chars[digit]
            for char in chars:
                recurse(index + 1, curr + char)

        recurse(0, "")

        return result

# Time complexity: O(n * 4^n ) because we have n characters and up to 4 branches n times
# Space complexity: O(n) extra space, O(n * 4^n) space for the output list.


class Iteration:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = [""]
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        for digit in digits:
            tmp = []
            for curStr in res:
                for c in digitToChar[digit]:
                    tmp.append(curStr + c)
            res = tmp
        return res

# same time and space complexity, this way might be slightly more readable
