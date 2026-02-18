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
        print(digit_to_chars)
        print(digit_to_chars[3])

        def recurse(index, curr):
            if index == len(digits):
                result.append(curr.copy())
                return

            digit = int(digits[index])
            chars = digit_to_chars[digit]
            for char in chars:
                curr.append(char)
                recurse(index + 1, curr)
                curr.pop()

        recurse(0, [])

        return result







