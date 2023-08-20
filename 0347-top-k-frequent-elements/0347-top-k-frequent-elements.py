class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = {}
        freq = [[] for i in range(len(nums)+1)]

        for elements in nums:
            numsMap[elements] = 1 + numsMap.get(elements, 0)
        
        for index, values in numsMap.items():
            freq[values].append(index)
        
        result = []
        
        for i in range(len(freq) - 1 , 0 , -1):

            for n in freq[i]:
                result.append(n)
                if len(result)==k:
                    return result
                