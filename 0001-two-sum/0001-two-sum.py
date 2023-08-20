class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       hashnum = {}
       
       for index, values in enumerate(nums):
            diff = target - values
            if diff in hashnum:
                return [hashnum[diff],index]
            hashnum[values]=index
