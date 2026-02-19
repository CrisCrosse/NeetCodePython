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
                curr += char
                recurse(index + 1, curr)
                curr = curr[:-1]

        recurse(0, "")

        return result