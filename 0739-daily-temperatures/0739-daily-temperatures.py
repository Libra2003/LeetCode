class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        answer = [0]*len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t> stack[-1][1]:
                stackInd,stackValue = stack.pop()
                answer[stackInd] = i - stackInd
            stack.append((i,t))
        return answer