from collections import defaultdict

class InitialAttempt:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right, result = 0, 0, 0

        while left < len(s):
            starting_chars_to_try = set();
            for i in range(k + 1):
                if left + i < len(s):
                    starting_chars_to_try.add(s[left + i])

            if len(starting_chars_to_try) > 0:
                for char in starting_chars_to_try:
                    right = left
                    starting_char = char
                    print(starting_char)
                    non_identical_characters_remaining = k

                    while non_identical_characters_remaining >= 0 and right < len(s):
                        right_char = s[right]
                        print(left, right)
                        print(starting_char, right_char)
                        if starting_char != right_char:
                            non_identical_characters_remaining -= 1
                            if non_identical_characters_remaining < 0:
                                break
                        right += 1

                    print(
                        f"found max continous {starting_char} characters starting at index {left}, ending at index {right} for length {right - left}")
                    result = max(result, right - left)
            else:
                starting_char = s[left]
                non_identical_characters_remaining = k

                while non_identical_characters_remaining >= 0 and right < len(s):
                    right_char = s[right]
                    print(left, right)
                    print(starting_char, right_char)
                    if starting_char != right_char:
                        non_identical_characters_remaining -= 1
                        if non_identical_characters_remaining < 0:
                            break
                    right += 1

                print(
                    f"found max continous {starting_char} characters starting at index {left}, ending at index {right} for length {right - left}")
                result = max(result, right - left)

            left += 1
            right = left

        return result

class Refactor:
    def characterReplacement(self, s: str, k: int) -> int:
        left, result = 0, 0

        while left < len(s):
            starting_chars_to_try = set(s[left])
            for i in range(k + 1):
                if left + i < len(s):
                    starting_chars_to_try.add(s[left + i])

            for char in starting_chars_to_try:
                print(char)
                result = max(result, self.findMaxRepeatingSubstringForStartingCharAndIndex(k, left, s, char))

            left += 1
        return result

    def findMaxRepeatingSubstringForStartingCharAndIndex(self, k: int, left: int, s: str, starting_char) -> int:
        right = left
        non_identical_characters_remaining = k
        while non_identical_characters_remaining >= 0 and right < len(s):
            right_char = s[right]
            print(left, right)
            print(starting_char, right_char)
            if starting_char != right_char:
                non_identical_characters_remaining -= 1
                if non_identical_characters_remaining < 0:
                    break
            right += 1
        print(
            f"found max continous {starting_char} characters starting at index {left}, ending at index {right} for length {right - left}")
        return right - left

#     this is O(n^2 * m) complexity, because for each index we iterate over a maximum of n elements, and at each index we do that m times where m is the number of
# unique characters within k spaces of the index
# the space complexity is O(1) because we only use non_identical_characters_remaining, left, right and result regardless of input length

class BruteForce:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            count, maxf = {}, 0
            # count the frequency of chars after i
            for j in range(i, len(s)):
                count[s[j]] = 1 + count.get(s[j], 0)
                # number of time the most occuring char has been seen
                maxf = max(maxf, count[s[j]])
                # if the length of the substring minus the number of times the most occuring char is less than k
                # ie if we have less unique chars than k
                # set substring length to result if greater than existing result
                if (j - i + 1) - maxf <= k:
                    res = max(res, j - i + 1)
        return res
#     this is O(n^2) time complexity
#     this is O(m) space complexity where m is the number of unique characters because we create a counter dict of unique chars

class SlidingWindow:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)

        # for each unique character in the string
        for c in charSet:
            count = l = 0
            # for every right index
            for r in range(len(s)):
                if s[r] == c:
                    # count occurrences of the unique char
                    count += 1

                # while length between right and left minus occurrences of the unique char is greater than k
                # this is sliding the left along when we encounter a barrier of k unique characters
                # or sliding the left along when we encounter a unique character that puts us over the k limit
                count_of_non_c_chars = (r - l + 1) - count
                while count_of_non_c_chars > k:
                    # keep count up to do date with updated left pointer, this keeps our count of non - c chars accurate
                    if s[l] == c:
                        count -= 1
                    l += 1

                # add the max substring for each char
                res = max(res, r - l + 1)
        return res

# This is O(n * m) complexity because for every unique char (m = number of unique chars) we iterate through the whole string
# this is O(m) space complexity because we create a set of m length


class SlidingWindowOptimal:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        # for every index in s
        for r in range(len(s)):
            # count the times a char occurs
            count[s[r]] = 1 + count.get(s[r], 0)
            # get max times a char has occurred
            maxf = max(maxf, count[s[r]])

            # pulling this out does not work because we need this value reevaluated on each while loop check
            number_of_characters_other_than_most_common_one = (r - l + 1) - maxf


            # while the number_of_characters_other_than_most_common_one is greater than k
            # how does this handle when k is 0, it will move the left hand side along to the right until they are equal, and there is only m
            # how does this work because maxf would not be updated?
            # eg AAABAA, k = 0
            # it hits this while loop at right index is 3 and left is 0, so 4 - maxf (3 As) = 1 > 0
            # then decrements the count of A one, and increments l, reevaluates the loop: (3 - 1 + 1) - 3 = 0 > k
            # and calculates the res as max(res, 3)
            # the next for loop is executed with l = 1, r = 4
            # count of A is again 3 and maxf is 3
            # it hits the while loop: (4 -1 + 1) - 3 = 1 > 0:
            # count of A --> 2 again left --> 2 also
            # it reevaluates the while (4 -2 + 1) - 3 = 0 > 0: false so exits the loop
            # the next round is left index = 2, right = 5
            # maxf is 3 again due to A
            # while loop is (5 - 2 + 1) - 3 = 1 > 0:
            # so it moves left along one again, and decrements the frequency dict
            # this is effectively only allowing our sliding window to grow when it contains less than k unique chars
            # otherwise it shifts the window continually over to the right
            # this feels like it shouldn't work because maxf is no longer up to date and is recording
            # the most frequent element from before the while loop


            # what about when more we encounter more than one of the non most frequent chars:
            # AAABBAAA, k = 0
            # we have the same entry to the while loop of l = 0, r = 3, maxf = 3
            # we exit thw while loop after incrementing l again
            # now we enter the while loop with l = 1, r = 4, maxf = 2 because we added a B so we have two Bs two As
            # we increment l and remove an A from dict (4 - 2 + 1) - 2 = 1 > 0
            # we increment l again and remove an A from the dict (4 - 3 + 1) - 2 = 0 > 0
            # we exit the loop


            # what about when more we encounter more than one of the non most frequent chars:
            # AAAABBAAA, k = 0
            # we enter the while loop with l = 0, r = 4, maxf = 4 (4 - 0 + 1) - 4 = 1 > 0
            # we increment l and remove an A from the dict: (4 - 1 + 1) -4 = 0 > 0: loop exit
            # now we enter the while loop with l = 1, r = 5, maxf = 3 because we added a B so we have two Bs two 3 As
            # ( 5 - 1 + 1) - 3 = 2 > 0
            # so stay in the while loop twice and increment l by two whilst removing two As
            # (5 - 3 + 1) - 3 = 0 > 0
            # on the next for iteration we enter the loop with, l = 3, r = 6, maxF = 2 (2 we now have 2As and 2Bs)
            # (6 - 3 + 1) - 2 = 2 > 0
            # so stay in the while loop twice and increment l by two whilst removing two As
            # (6 - 5 + 1) - 2 = 0 > 0
            # we enter the loop again with l = 5, r = 7, maxf = 2 as we now have 1B then 2As
            # (7 - 5 + 1) - 2 = 1 > 0

            # With this method we grow the window to the right by incrementing r whilst we have unique chars under k
            # otherwise we decrement the window to the left by incrementing l by the number of chars other than the most frequent we have that is above k and go again


            # we increment l and remove an A from dict (4 - 2 + 1) - 2 = 1 > 0
            # we increment l again and remove an A from the dict (4 - 3 + 1) - 2 = 0 > 0
            # we exit the loop




            # ((r - l + 1) - maxf) stays at 0 whilst adding the same char, and increases when adding a char that is not the most frequent
            # we use the most frequent char as the one we should be counting
            while  (r - l + 1) - maxf > k:
                # remove the left hand character from the dict
                count[s[l]] -= 1
                # increment the left pointer
                l += 1
            # save the max result
            res = max(res, r - l + 1)

        return res

class SlidingWindowOptimalRewritten:
    from collections import defaultdict

    class Solution:
        def characterReplacement(self, s: str, k: int) -> int:
            left, max_frequency, result = 0, 0, 0
            count = defaultdict(int)

            for right in range(len(s)):
                previous_char_count = count[s[right]]
                count[s[right]] = previous_char_count + 1
                max_frequency = max(max_frequency, previous_char_count + 1)

                # length of current substring = r - l + 1
                # while we have more unique chars in the substring than k
                print(count)
                while (right - left + 1) - max_frequency > k:
                    print(f"we have too many unique chars for substring length {right - left + 1} and k value {k} ")
                    # shorten the window from the left
                    previous_char_count = count[s[left]]
                    count[s[left]] = previous_char_count - 1
                    left += 1

                print(count)
                print(left, right)
                print(s[left], s[right])

                result = max(result, right - left + 1)
            return result





