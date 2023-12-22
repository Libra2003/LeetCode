class Solution:
    def findMin(self, nums: list[int]) -> int:
        l,r = 0 , len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[l]<=nums[mid]<=nums[r]:
                return nums[l]
            if nums[mid]>=nums[r]:
                l = mid+1
            else:
                r = mid
        return nums[l]