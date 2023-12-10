class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_Area = 0
        for index,height in enumerate(heights):
            start = index
            while stack and stack[-1][1]>height:
                i,h = stack.pop()
                max_Area = max(max_Area,h *(index-i))
                start = i
            stack.append((start,height))
        
        for index,height in stack:
            max_Area = max(max_Area, height * (len(heights)-index))
        return max_Area
sol = Solution()
result = sol.largestRectangleArea([2,1,5,6,2,3])
print(result)