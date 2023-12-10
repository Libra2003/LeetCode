class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                ans[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        
        return ans

sol = Solution()

temperatures = [73,74,75,71,69,72,76,73]
result = sol.dailyTemperatures(temperatures)

print(sol)