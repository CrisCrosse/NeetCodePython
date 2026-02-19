from typing import List


class InitialAttempt:
    # 6/ 21 test cases working
    def partition(self, s: str) -> List[List[str]]:
        # each char on its own is valid palindrome
        # double of same chars + single chars are valid palindromes
        # for the amount of times you have a char you could have it up to that many times on its own and then the rest individual chars
        # you could have doubles within doubles eg baab
        #

        # get all valid palindrome substrings
        # all single chars
        # duplicate chars 2 -> n times
        #
        palindromic_substrings = set()

        def isPalindrome(s) -> bool:
            return s == s[::-1]

        def getAllPalindromicSubstrings(s) -> List[str]:
            res = ['']
            for char in s:
                # print(f"char: {char}")
                size = len(res)
                for i in range(size):
                    substring = res[i]
                    # print(f"substring: {substring}")
                    new_substring = substring + char
                    if isPalindrome(new_substring):
                        # print(f"substring {new_substring} is a palindrome")
                        res.append(new_substring)
                    # print(f"res: {res}")

            return res[1:]

        all_substrings = getAllPalindromicSubstrings(s)
        frequency_chars = {}
        for char in s:
            if char not in frequency_chars:
                frequency_chars[char] = 1
            else:
                existing_frequency = frequency_chars[char]
                frequency_chars[char] = existing_frequency + 1
        print(all_substrings, frequency_chars)
        result = []

        def getCombinationsPalindromicSubstrings(curr: [str], i: int):
            print(
                f"iterating to get all combinations of substrings, curr: {curr}, i: {i}, freq_dict: {frequency_chars}")

            all_chars_used = True
            for frequency in frequency_chars.values():
                # print(f"checking frequency {frequency}")
                if frequency < 0:
                    return
                if frequency != 0:
                    all_chars_used = False
            if all_chars_used:
                print(f"found a combination {curr}")
                result.append(curr.copy())
                return

            if i == len(all_substrings):
                return

            substring_to_add = all_substrings[i]
            curr.append(substring_to_add)
            for char in substring_to_add:
                frequency_chars[char] = frequency_chars[char] - 1

            getCombinationsPalindromicSubstrings(curr, i + 1)

            curr.pop()
            for char in substring_to_add:
                frequency_chars[char] = frequency_chars[char] + 1

            getCombinationsPalindromicSubstrings(curr, i + 1)

        getCombinationsPalindromicSubstrings([], 0)

        return result

        return [[""]]


class BacktrackingSolution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(j, i):
            if i >= len(s):
                # if we have recursed to the end of the substring and used all letters, add this combination of palindromes to the result
                if i == j:
                    res.append(part.copy())
                return

            # if current substring is palindrome
            if self.isPali(s, j, i):
                # append current substring
                part.append(s[j : i + 1])
                # depth first search after end of substring with the current substring
                dfs(i + 1, i + 1)
                # remove that palindrome and keep searching
                part.pop()

            # search larger substring
            dfs(j, i + 1)

        dfs(0, 0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

