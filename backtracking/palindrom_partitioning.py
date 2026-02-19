from operator import index
from typing import List

from pandas.core.indexes.base import ensure_index


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

# Time complexity: O(n * 2^n ) because we iterate throught the list --> n, and at each point we depth first search the rest of the solution with 2 branches
# Space complexity: O(n) extra space. O(n * 2^n) space for the output list.

class BacktrackingSolution2:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(i):
            # same exit condition as previous backtracking but we do not check if i == j
            if i >= len(s):
                res.append(part.copy())
                return

            # for each remaining substring endpoint, if it is a palindrom add it to the part and try to complete the sequence
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i: j + 1])
                    dfs(j + 1)
                    # remove that part so we can try larger substrings from i
                    part.pop()

        dfs(0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

# same time and space complexity

class BacktrackingWithDynamicProgramming:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        # create 2D array [i=1[j=1False, j=2False, j=3False, j=4False], i=2[j=1False, j=2False, j=3False, j=4False]]
        # which stores if s[i:j] is a palindrome
        dp = [[False] * n for _ in range(n)]


        for length in range(1, n + 1):
            for starting_index in range(n - length + 1):
                end_index = starting_index + length - 1
                print(f"length: {length}, starting_index: {starting_index}, end_index {end_index}")
                print(f"substring: {s[starting_index:end_index]}")

                dp[starting_index][end_index] = self.isPali(s, starting_index, end_index)
                print(f"dp: {dp}")

        res, part = [], []

        def dfs(i):
            # same exit condition as backtracking 2
            if i >= len(s):
                res.append(part.copy())
                return

            # for each subsequent index, if substring i->j is palindrom, recurse to find all solutions with that substring in this position
            for j in range(i, len(s)):
                if dp[i][j]:
                    part.append(s[i: j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

# this has the same tine and space complexity so doesn't seem to be worth the extra effort of creating the ahead of time palindrome lookup table


class Recursive:
    def partition(self, s: str) -> List[List[str]]:
        # dynamic program an is palindrome 2d array
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for l in range(1, n + 1):
            for i in range(n - l + 1):
                dp[i][i + l - 1] = (s[i] == s[i + l - 1] and
                                    (i + 1 > (i + l - 2) or
                                     dp[i + 1][i + l - 2]))

        # dfs with no global result var
        def dfs(i):
            # base case returns an empty list of lists
            if i >= n:
                return [[]]

            ret = []
            for j in range(i, n):
                if dp[i][j]:
                    # for all possible combinations of palindromes after j
                    # add the current found palindromic substring to it
                    nxt = dfs(j + 1)
                    for part in nxt:
                        cur = [s[i: j + 1]] + part
                        ret.append(cur)
            # return all possible palindromic subtrings from this index
            return ret

        return dfs(0)

