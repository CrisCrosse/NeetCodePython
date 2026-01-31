from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort() # in place sort using tim sort algo is O(n log n) time

        def dfs(i, cur, total):
            if total > target:
                return
            if total == target:
                res.append(cur.copy())
                return
            if i > len(candidates) - 1:
                return

            # binary decision tree, include element at index and have all solutions with element, or never include another of element
            # both decisions increment index because we do not want an element to be present more than its frequency in candidates

            current_element = candidates[i]
            cur.append(current_element)
            dfs(i + 1, cur, total + current_element)

            cur.pop()

            while True:
                # this is how we remove duplicate solutions,
                # skipping all the same element at once, this branch never contains current element
                i += 1
                # need to duplicate the index check here
                if i > len(candidates) - 1:
                    return
                if candidates[i] != current_element:
                    break
            dfs(i, cur, total)


        dfs(0, [], 0)
        return res


# the time complexity is O(n * 2 ^ n), 2 ^ n because we have a binary decision tree for n height
# we then have a copy of the result for each of the possible solutions, which will in the worst case be all the elements and be n length each
# therefore we n lots of work * 2 ^ n number of decisions/solutions
# space complexity is n?, we have a result of multiple combinations where each could contain approaching n, so isnt it still n * 2 ^ n space complexity

class NonOptimal:
    class Solution:
        def combinationSum2(self, candidates, target):
            # use a set to not allow addition of duplicates
            res = set()
            candidates.sort()

            def generate_subsets(i, cur, total):
                if total == target:
                    res.add(tuple(cur))
                    return
                if total > target or i == len(candidates):
                    return

                cur.append(candidates[i])
                generate_subsets(i + 1, cur, total + candidates[i])
                cur.pop()

                generate_subsets(i + 1, cur, total)

            generate_subsets(0, [], 0)
            # convert to list at the end
            return [list(combination) for combination in res]
