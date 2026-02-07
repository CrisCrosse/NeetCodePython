from typing import List


class BruteForce:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def isValid(string: str):
            open_brackets = 0
            for bracket in string:
                open_brackets += 1 if bracket == '(' else -1
                # exit out of this recursion if we have closed a bracket before opening
                if open_brackets < 0:
                    return False
            # if final open bracket count is not 0 return false
            return not open_brackets

        def dfs(s: str):
            # base case, if we have the right length and brackets are opene d and clsoed properly add to result
            if n * 2 == len(s):
                if isValid(s):
                    res.append(s)
                return

            dfs(s + '(')
            dfs(s + ')')

        dfs("")
        return res

# Time complexity: O(2^2n *n)
# Space complexity: O(2^2n *n)

class Backtracking:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            # if we have valid brackets and the right number add to result
            if openN == closedN == n:
                res.append("".join(stack))
                return

            # open a bracket if valid
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            # close a bracket if valid --> avoids wrong solutionds
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res


# Time complexity: O(4n / square root n)
# Space complexity: O(n)

class DynamicProgramming:
    def generateParenthesis(self, n):
        res = [[] for _ in range(n+1)]
        res[0] = [""]

        for k in range(n + 1):
            for i in range(k):
                # we loop over previous amounts of brackets and combine them
                for left in res[i]:
                    for right in res[k-i-1]:
                        print(f"k: {k}, i: {i},\n res[i]: {res[i]} left: {left} \n res[k-i-1]: {res[k-i-1]}, right: {right}")
                        res[k].append("(" + left + ")" + right)
                        print(f"result: {res}")

        return res[-1]

    # Time complexity: O(4n / square root n)
    # Space complexity: O(n)
