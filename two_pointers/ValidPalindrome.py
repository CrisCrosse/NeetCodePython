class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_chars = [char.lower() for char in s if char.isalnum()]
        return filtered_chars == filtered_chars[::-1]

    class Solution:
        def isPalindrome(self, s: str) -> bool:
            clean_chars = [str.lower(char) for char in s if str.isalnum(char)]
            print(clean_chars)
            left_pointer, right_pointer = 0, len(clean_chars) - 1

            while left_pointer < right_pointer:
                if clean_chars[left_pointer] != clean_chars[right_pointer]:
                    return False
                left_pointer += 1
                right_pointer -= 1
            return True
