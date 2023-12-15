class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l<=r:
            totaltime = 0
            k = (l + r) // 2
            for p in piles:
                totaltime += math.ceil(float(p) / k)
            if totaltime <= h:
                    res = k
                    r = k - 1
            else:
                    l = k + 1

        return res