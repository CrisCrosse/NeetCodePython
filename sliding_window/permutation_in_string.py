from collections import defaultdict
import copy


class InitialAttempt:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_characters_and_frequency = defaultdict(int)

        for char in s1:
            s1_characters_and_frequency[char] += 1

        print(s1_characters_and_frequency)
        for i, char in enumerate(s2):
            print(i, char)
            if char in s1_characters_and_frequency:
                print(f"checking permutation")
                frequency_copy = copy.copy(s1_characters_and_frequency)
                for j in range(len(s1)):
                    print(f"checking forward {j} characters from {i}")
                    if i + j >= len(s2):
                        print(
                            f"index too high and permutation no longer fits in after checking forward {j} characters from {i}")
                        return False
                    if frequency_copy[s2[i + j]] <= 0:
                        print(
                            f"breaking out of loop because element {s2[i + j]} not in frequency dict {frequency_copy}")
                        break
                    frequency_copy[s2[i + j]] -= 1
                    if j == len(s1) - 1:
                        # if we have reached the final char in the permutation and are still in the loop
                        return True

        return False

# this solution is O(n * m) in the worst case where m is the length of s1 and n is the length of s2, because we
# iterate through each char of s2 and potentially check len s1 chars each time
# it is O(2y) space complexity where y in the number of unique chars in s1 because we create two freq dicts

class OptimalSolution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if permutation cannot be contained in s2
        if len(s1) > len(s2):
            return False

        # create integer count for each english alphabet character
        s1Count, s2Count = [0] * 26, [0] * 26
        # start off with the start of s2, the first possible occurence of the permutation
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # s2 contains s1 when all the 26 alphabet chars have the same frequency as s1
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        # start sliding the window over to the right for each character s2 is greater than s1, keeping the same window size
        # becuase we know the length of the permutation needed
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26

class OptimalSolutionRewrittenMyselfFromMemory:
    class Solution:
        def checkInclusion(self, s1: str, s2: str) -> bool:
            if len(s1) > len(s2):
                return False

            s1_char_count = [0] * 26
            s2_char_count = [0] * 26

            for index in range(len(s1)):
                s1_char_index = self.getZeroBasedAlphabetIndexOfChar(s1[index])
                s1_char_count[s1_char_index] += 1

                s2_char_index = self.getZeroBasedAlphabetIndexOfChar(s2[index])
                s2_char_count[s2_char_index] += 1

            matching_characters_in_s1_and_s2 = 0
            for index in range(26):
                if s1_char_count[index] == s2_char_count[index]:
                    matching_characters_in_s1_and_s2 += 1
            if matching_characters_in_s1_and_s2 == 26:
                return True

            left = 0
            # for the remaining chars in s2, shift window right, fix counts and matches and check again
            for right in range(len(s1), len(s2)):
                print(s1_char_count)
                print(s2_char_count)
                right_char_to_add = s2[right]
                right_char_index = self.getZeroBasedAlphabetIndexOfChar(right_char_to_add)

                former_s2_right_char_count = s2_char_count[right_char_index]
                if former_s2_right_char_count == s1_char_count[right_char_index]:
                    matching_characters_in_s1_and_s2 -= 1
                if former_s2_right_char_count + 1 == s1_char_count[right_char_index]:
                    matching_characters_in_s1_and_s2 += 1
                s2_char_count[right_char_index] += 1

                left_char_to_remove = s2[left]
                left_char_index = self.getZeroBasedAlphabetIndexOfChar(left_char_to_remove)

                former_s2_left_char_count = s2_char_count[left_char_index]
                if former_s2_left_char_count == s1_char_count[left_char_index]:
                    matching_characters_in_s1_and_s2 -= 1
                if former_s2_left_char_count - 1 == s1_char_count[left_char_index]:
                    matching_characters_in_s1_and_s2 += 1
                s2_char_count[left_char_index] -= 1

                print(left, right)
                print(left_char_to_remove, right_char_to_add)
                if matching_characters_in_s1_and_s2 == 26:
                    return True
                left += 1
            return False

        def getZeroBasedAlphabetIndexOfChar(self, character: str):
            return ord(character) - ord('a')

# This solution is O(n) time complexity because we iterate over every element in s2 in the worst case
# it is O(1) space complexity because we create some vars and two 26 length arrays regardless of input size

