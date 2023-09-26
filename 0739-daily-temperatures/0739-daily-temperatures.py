class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        answer = [0]*len(temperatures)

        i = 0
        while(i < len(temperatures)):
            if not stack:
                stack.append(i)
            elif temperatures[stack[-1]] < temperatures[i]:
                answer[stack[-1]] = i-stack[-1]
                stack.pop()
                i -=1 
            elif temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)

            i+=1
        return answer