class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        array = []
        for i, n in enumerate(nums):

            if i>0 and n ==nums[i-1]:
                continue
            lptr, rptr = i + 1, len(nums) - 1

            while lptr < rptr:
                threesum = nums[i] + nums[lptr] + nums[rptr]
                if threesum < 0:
                    lptr += 1
                elif threesum > 0:
                    rptr -= 1
                else:
                    array.append([nums[i], nums[lptr], nums[rptr]])
                    lptr+=1
                    rptr-=1
        return array


sol = Solution()
result = sol.threeSum([-1,0,1,2,-1,-4])

print(result)