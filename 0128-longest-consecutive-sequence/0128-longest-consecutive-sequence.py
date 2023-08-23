class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for value in nums:
            if(value-1) not in numset:
                length = 0
                while(value+length) in numset:
                    length +=1
                
                longest = max(length,longest)
        
        return longest