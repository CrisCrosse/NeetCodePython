class Solution:
    def isValid(self, s: str) -> bool:
        bracket_stack = []
        bracket_dict = {"]": "[", ")": "(", "}": "{"}
        open_brackets = ["[", "(", "{"]
        for bracket in s:
            if bracket in open_brackets:
                bracket_stack.append(bracket)
                print(f"bracket_stack: {bracket_stack}")
            else:
                # closed bracket
                matching_bracket = bracket_dict.get(bracket)
                if len(bracket_stack) > 0:
                    popped_bracket = bracket_stack.pop()
                else:
                    return False
                print(f"closing bracket encountered: {bracket}")
                print(f"matching bracket is: {matching_bracket}")
                print(f"popped bracket is: {popped_bracket}")

                if matching_bracket != popped_bracket:
                    print("brackets did not match")
                    return False
        if len(bracket_stack) == 0:
            return True
        return False;

