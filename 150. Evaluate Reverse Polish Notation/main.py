from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "/", "*"}
        val = 0
        for value in tokens:
            if value in operators:
                a = int(stack.pop())
                b = int(stack.pop())

                if value == "+":
                    val = b + a
                elif value == "-":
                    val = b - a
                elif value == "*":
                    val = b * a
                elif value == "/":
                    val = b / a

                stack.append(val)
            else:
                stack.append(value)
        if stack:
            val = stack.pop()

        return val


sol = Solution()

result = sol.evalRPN(["19"])
print(result)