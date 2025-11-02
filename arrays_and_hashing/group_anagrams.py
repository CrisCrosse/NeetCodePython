from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_sorted_string_dict = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            string_sorted_string_dict[sorted_string] = string_sorted_string_dict.get(sorted_string, []) + [string]
        print(string_sorted_string_dict)
        result = []
        for value in string_sorted_string_dict.values():
            result.append(value)
        return result

# This solution is O(n * n log n) because we sort each string
# It is also O (n) space complexity because the size of the dict scales with input values

class optimalSolution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                # this ensures the indices start at a at a and increment to z
                count[ord(c) - ord('a')] += 1
            # they wrap the count list in a tuple to make it hashable
            res[tuple(count)].append(s)
        #     list constructor is cleaner than my manual creation
        return list(res.values())