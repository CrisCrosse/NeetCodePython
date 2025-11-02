class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = [char for char in s]
        t_list = [char for char in t]
        print(s_list)
        print(t_list)
        s_list.sort()
        t_list.sort()
        return s_list == t_list

    # this is O(n log n) due to the sorting algorithm and O(n) space due to creating lists

class NoSorting:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_list = [char for char in s]
        t_list = [char for char in t]
        for char in s_list:
            if char not in t_list:
                return False
            t_list.remove(char)
        return True
# this is O(n) due to iterating over each element and O(2n) space due to creating lists

class Dict:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
    # this is O(n) time but O(1) space due having max 26 keys in each dict