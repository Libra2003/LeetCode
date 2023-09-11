class Solution:
    def isValid(self, s: str) -> bool:
        top = -1
        stack = [0] *len(s)

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                top += 1
                stack[top] = s[i]
            else:
                if (s[i] == ')' and stack[top] != '(') or (s[i] == '}' and stack[top] != '{') or (
                        s[i] == ']' and stack[top] != '['):
                    return False
                else:
                    stack[top] = 0
                    top -= 1

        if(top == -1):
            return True
        else:
            return False