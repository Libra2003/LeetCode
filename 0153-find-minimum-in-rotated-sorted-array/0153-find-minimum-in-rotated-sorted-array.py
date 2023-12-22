class Solution:
    def findMin(self, nums: List[int]) -> int:
        pivot = 0

        for idx, num in enumerate(nums):
            if nums[idx] < nums[idx - 1] and idx > 0:
                pivot = idx

        return nums[pivot]

        


        
