from typing import List


class ZAlgorithm:
    def ReturnIndicesWhichMatchPattern(self, pattern: str, string: str) -> List[int]:
        # pass in combined string with separator as non-present element
        # this will not work where the pattern or string contains this element
        result_array = self.ZSearch(pattern + "§" + string)

        indices = []
        string_start = len(pattern) + 1 # adding one means we will start after the non-matching char

        for i in range(string_start, len(result_array)):
            if result_array[i] == len(pattern):
                indices.append(i - string_start)

        return indices

    def ZSearch(self, string: str) -> List[int]:
        # create result z array of an int per char in string
        result = [0] * len(string)
        # each int is the number of matching substring chars from the index in the string, where the substring is the chars from the start of the string
        for i in range(len(string)):
            # for each char
            matching_chars = 0
            for j in range(i):
                # return if we go beyond end of string
                if i + j >= len(string):
                    break
                # compare every char up to char with chars after char
                if string[j] == string[i + j]:
                    matching_chars += 1
                else:
                    # if there is a non matching char stop comparing
                    break
            result[i] = matching_chars

        return result

    def z_function(self, s: str) -> list:
        z = [0] * len(s)
        l, r, n = 0, 0, len(s)
        for i in range(1, n):
            length_of_matching_substring = z[i]
            if i <= r:
                # don't check chars that already have a matching substring covering them
                length_of_matching_substring = min(r - i + 1, z[i - l])

            end_index_of_current_substring = i + length_of_matching_substring
            end_char_of_current_substring = s[end_index_of_current_substring]
            pattern_char = s[length_of_matching_substring]

            while end_index_of_current_substring < n and pattern_char == end_char_of_current_substring:
                length_of_matching_substring += 1
                end_index_of_current_substring = i + length_of_matching_substring

                if end_index_of_current_substring >= n:
                    break
                end_char_of_current_substring = s[end_index_of_current_substring]
                pattern_char = s[length_of_matching_substring]
            if i + length_of_matching_substring - 1 > r:
                l, r = i, i + length_of_matching_substring - 1
            z[i] = length_of_matching_substring
        return z