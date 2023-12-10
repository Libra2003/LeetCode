class Solution:
    def search(self, nums: list[int], target: int) -> int:
        h,l = len(nums)-1,0
        while l<h:
            m = l+((h-l)//2)
            if target<nums[m]:
                h = m-1
            elif target>nums[m]:
                l = m+1
            else:
                return m
        return -1


sol = Solution()
result = sol.search( [-1,0,3,5,9,12], 9)
print(result)
