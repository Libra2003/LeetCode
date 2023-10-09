class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for index, height in enumerate(heights):
            curr_i = index
            while stack and height<stack[-1][1]:
                curr_i,h = stack.pop()
                max_area = max(max_area,(index-curr_i)*h)
            stack.append((curr_i,height))
        while stack:
            curr_i,h = stack.pop()
            max_area = max(max_area, (len(heights)-curr_i)*h)
        return max_area
