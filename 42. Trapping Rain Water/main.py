class Solution:
    def trap(self, height: list[int]) -> int:
    
        l = 0
        r = len(height)-1
        maxL = height[l]
        maxR = height[r]
        trap = 0
        while l<r:
            if height[l]<height[r]:
                maxL = max(maxL,height[l])
                trap += max(0,(maxL-height[l+1]))
                l+=1

            else:
                maxR = max(maxR,height[r])
                trap += max(0,maxR - height[r-1])
                r-=1
        return trap
sol = Solution()
result = sol.trap([6,2,0,3,2,4]
)
print(result)
