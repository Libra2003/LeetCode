class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            temp = min(height[r], height[l]) * (r - l)
            if temp > res:
                res = temp
            if height[l] <= height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
        return res

sol = Solution()
res = sol.maxArea([1,8,6,2,5,4,8,3,7])
print(res)