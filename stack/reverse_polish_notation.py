from typing import List


class MySolution:
    def evalRPN(self, tokens: List[str]) -> int:
        print(tokens)
        if len(tokens) == 1:
            return int(tokens[0])

        operators = set(["+", "-", "*", "/"])

        operator_index = 0
        for i in range(len(tokens)):
            if tokens[i] in operators:
                operator_index = i
                break
        operand_1 = int(tokens[operator_index - 2])
        operand_2 = int(tokens[operator_index - 1])
        operator = tokens[operator_index]
        result = 0
        match operator:
            case "+":
                result = operand_1 + operand_2
            case "-":
                result = operand_1 - operand_2
            case "*":
                result = operand_1 * operand_2
            case "/":
                result = int(operand_1 / operand_2)

        if len(tokens) == 3:
            return result
        else:
            tokens.pop(operator_index - 2)
            tokens.pop(operator_index - 2)
            tokens.pop(operator_index - 2)
            tokens.insert(operator_index - 2, str(result))
            return self.evalRPN(tokens)

# this is O(n^2) worse case time complexity if the operators are all at the end of the sequence, as for each
# operation we loop through the whole array
# this is O(n) space complexity for the input array

class Recursion:
    def evalRPN(self, tokens: List[str]) -> int:
        def solveRecursivelyByPoppingFromTheRight():
            popped = tokens.pop()
            print(tokens)
            print(f"popped {popped}")
            if popped not in ["/", "*", "+", "-"]:
                return int(popped)

            right_operand = solveRecursivelyByPoppingFromTheRight()
            left_operand = solveRecursivelyByPoppingFromTheRight()

            print(left_operand, right_operand)

            match popped:
                case "+":
                    return left_operand + right_operand
                case "-":
                    return left_operand - right_operand
                case "*":
                    return left_operand * right_operand
                case "/":
                    return int(left_operand / right_operand)

        return solveRecursivelyByPoppingFromTheRight()

class Stack:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            print(tokens)
            print(stack)
            if tokens[i] in "+-/*":
                right_operand = stack.pop()
                left_operand = stack.pop()
                match tokens[i]:
                    case "+":
                        stack.append(left_operand + right_operand)
                    case "-":
                        stack.append(left_operand - right_operand)
                    case "*":
                        stack.append(left_operand * right_operand)
                    case "/":
                        stack.append(int(left_operand / right_operand))
                continue
            stack.append(int(tokens[i]))
        return stack[0]

