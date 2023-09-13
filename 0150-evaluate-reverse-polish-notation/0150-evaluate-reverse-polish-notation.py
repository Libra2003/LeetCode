class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        val = 0
        for value in tokens:
         

          if value == "+":
              val = int(stack.pop()) + int(stack.pop())
              stack.append(val)
          elif value == "-":
            a = int(stack.pop())
            b = int(stack.pop())
            val = b - a
            stack.append(val)
          elif value == "*":
              val = int(stack.pop()) * int(stack.pop())
              stack.append(val)
          elif value == "/":
            a = int(stack.pop())
            b = int(stack.pop())
            val = b / a
            stack.append(val)

          else:
            stack.append(value)
        if stack:
            val = int(stack.pop())

        return val
