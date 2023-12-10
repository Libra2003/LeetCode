from typing import List
import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = {}

        for elements in nums:
            numsMap[elements] = 1 + numsMap.get(elements, 0)

            sorted_nums = sorted(numsMap.items(), key=lambda x: x[1], reverse=True)

        top_k = [x[0] for x in sorted_nums[:k]]


        return top_k

sol = Solution()
result = sol.topKFrequent([1,1,1,2,2,3,3,4,5],k = 2)

print(result)