class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for value in nums:
            if value in hashset:
                return True
            hashset.add(value)
           
        
        return False