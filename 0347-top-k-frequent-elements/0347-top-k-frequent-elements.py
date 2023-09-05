class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for index, value in enumerate(nums):
            hashMap[value] = hashMap.get(value, 0) + 1
        sorted_nums  = sorted(hashMap.items(), key=lambda x: x[1], reverse=True)
        top_k = [x[0] for x in sorted_nums[:k]]
        return top_k

