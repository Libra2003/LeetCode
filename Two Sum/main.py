from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for index, value in enumerate(nums):
            diff = target - value
            if diff in prevMap:
                print(prevMap[diff])
                print(prevMap)

                return [prevMap[diff], index]
            prevMap[value] = index
            print(value)



sol = Solution()
result = sol.twoSum([2,15,11,7], 9)

print(result)