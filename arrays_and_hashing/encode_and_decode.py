from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for string in strs:
            for char in string:
                print(ord(char))
                encoded_string += str(ord(char)) + '?'
            encoded_string += "!"
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        result = []
        current_word = ''
        current_character_code = ''
        for char in s:
            print(f"char {char}, current_char_code: {current_character_code}, current_word {current_word}")
            if char == "!":
                result.append(current_word)
                current_word = ''
                current_character_code = ''
            elif char == "?":
                current_word += chr(int(current_character_code))
                current_character_code = ''
            else:
                print("char is not ! or ?")
                current_character_code += char

        return result

    # this solution is O(m * n) time complexity where m is number of words and n is the length of the words
    # it is o(1) space complexity because we

class OptimalSolution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res
# this is O(m) time complexity
# this is O(m + n) space complexity