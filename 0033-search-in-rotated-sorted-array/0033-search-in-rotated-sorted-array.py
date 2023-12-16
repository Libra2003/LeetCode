class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0 , len(nums)-1

        while l<=r:
            mid = (l+r)//2
            if nums[mid]>nums[r]>target:
                l = mid+1
            else:
                r = mid-1
            
            if nums[mid]==target:
                return mid
        return -1
