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
            val = int(stack.pop())

        return val