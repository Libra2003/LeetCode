from typing import List
import collections


# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         numsMap = {}
#
#         for elements in nums:
#             numsMap[elements] = 1 + numsMap.get(elements, 0)
#
#             sorted_nums = sorted(numsMap.items(), key=lambda x: x[1], reverse=True)
#
#         top_k = [x[0] for x in sorted_nums[:k]]
#
#
#         return top_k

#class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         numsMap = {}
#         freq = [[] for i in range(len(nums)+1)]
#
#         for elements in nums:
#             numsMap[elements] = 1 + numsMap.get(elements,0)
#             print(numsMap)
#         for index ,values in numsMap.items():
#             freq[values].append(index)
#             print(f"values: {values}, index: {index}")
#             #
#             print(freq)
#
#         result = []
#
#         for i in range(len(freq) - 1 , 0 , -1):
#             for n in freq[i]:
#                 result.append(n)
#                 # print(result)
#                 print(freq[i])
#                 print(len(result))
#                 if len(result) == k:
#                     return result

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for index, value in enumerate(nums):
            hashMap[value] = hashMap.get(value, 0) + 1
        sorted_nums  = sorted(hashMap.items(), key=lambda x: x[1], reverse=True)
        top_k = [x[0] for x in sorted_nums[:k]]
        return top_k


sol = Solution()
result = sol.topKFrequent([1,1,1,2,2,3,3,4,5],k = 2)

print(result)