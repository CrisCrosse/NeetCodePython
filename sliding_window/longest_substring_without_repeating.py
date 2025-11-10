from collections import defaultdict


class InitialAttempt:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        max_substring = 1

        left, right = 0, 1
        while left < len(s):
            seen = set()
            seen.add(s[left])
            counter = 1
            while right < len(s):
                next_char = s[right]
                if next_char in seen:
                    break
                seen.add(next_char)
                right += 1
                counter += 1
            left += 1
            right = left + 1
            max_substring = max(max_substring, counter)

        return max_substring

        # This solution is O(n^2) time complexity because in the worst case where the string is one non repeating string
        # We iterate over every element twice --> there will be some way to speed this up where we do not need
        # to check every single char depending on where the next one eneded

    # eg dvdf = 3 not 2
    # rg fdvdfeaiod


class SlidingWindow:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        res = 0

        for right in range(len(s)):
            # if we get to a repeated element, get rid of all the chars before the first of said element and
            # recalibrate the counter

            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1

            # while chars are unique add them to the set and count the unique no of chars
            charSet.add(s[right])
            res = max(res, right - left + 1)
        return res

#     this is O(n) time complexity because we only iterate rightwards once, although we do some work in the while s[right] loop also which would make it worse case 2n
# this is O(m) space complexity where m is the number of unique chars because charSet has length m

class OptimalSlidingWindow:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            # if char already in map
            if s[r] in mp:
                # slide to 1 past previous occurence of char or stay where we are if we have already iterated past it
                # , when would this not be mp[s[r]] + 1? if we have already iterated past the previous occurence of the element due to another repeated element
                l = max(mp[s[r]] + 1, l)
            #     map of char to index
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res

class rememberedOptimalSlidingWindow:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        char_to_last_seen_index = {}
        left, right, result = 0, 0, 0

        while right < len(s):
            right_char = s[right]
            if right_char in char_to_last_seen_index:
                left = max(left, char_to_last_seen_index[right_char] + 1)

            char_to_last_seen_index[right_char] = right
            result = max(result, (right - left) + 1)
            right += 1

        return result









