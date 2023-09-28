class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {'(':')', '{': '}', '[':']'}
        for bracks in s:
            if bracks in map:
                stack.append(bracks)
                continue
            elif len(stack)==0 or bracks != map[stack.pop()]:
                    return False
        return len(stack)==0
            