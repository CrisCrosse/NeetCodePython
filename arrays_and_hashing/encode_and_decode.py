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

