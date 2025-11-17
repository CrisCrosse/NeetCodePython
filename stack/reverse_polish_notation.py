from typing import List


class NotCompleteSolution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) < 3:
            return 0

        # Need to make this smarter and search for an operand preceded by two numbers
        operand_1 = int(tokens[0])
        operand_2 = int(tokens[1])
        operator = tokens[2]
        result = 0
        match operator:
            case "+":
                result = operand_1 + operand_2
            case "-":
                result = operand_1 - operand_2
            case "*":
                result = operand_1 * operand_2
            case "/":
                result = operand_1 // operand_2

        if len(tokens) == 3:
            return result
        else:
            tokens.pop(0)
            tokens.pop(0)
            tokens.pop(0)
            tokens.insert(0, result)
            return self.evalRPN(tokens)

