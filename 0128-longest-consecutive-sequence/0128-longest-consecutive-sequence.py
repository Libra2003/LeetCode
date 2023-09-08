class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        longest = 0

        for value in numSet:
            if(value-1) not in numSet:
                length = 1
                while(value+length) in numSet:
                    length +=1
                
                longest = max(length,longest)
        
        return longest

