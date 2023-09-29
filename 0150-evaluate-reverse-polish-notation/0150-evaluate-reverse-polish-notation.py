class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators_dict = {
            '+':lambda a,b: operator.add(a,b),
            '-':lambda a,b: operator.sub(b,a),
            '*':lambda a,b: operator.mul(b,a),
            '/':lambda a,b: floor(int(b/a))
        }
        for i in tokens:
            if i in operators_dict:
                x = stack.pop()
                y = stack.pop()
                stack.append(operators_dict[i](int(x),int(y)))
            else:
                stack.append(int(i))
        
        return stack[-1]