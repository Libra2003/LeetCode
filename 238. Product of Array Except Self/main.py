from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            print("pre: ", res)

        postfix = 1
        for j in range(len(nums) - 1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j]
            print('pos: ',res)

        return res

sol = Solution()
nums = [1, 2, 3, 4]

result = sol.productExceptSelf([1, 2, 3, 4])

print(result)