class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for index, values in enumerate(nums):
            diff = target-values
            if diff in hashMap:
                return [hashMap[diff],index]

            hashMap[values] = index
