class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashS, hashT = {}, {}

        for value in range(len(s)):
            hashS[s[value]] = hashS.get(s[value], 0) + 1
            hashT[t[value]] = hashT.get(t[value], 0) + 1
            print(hashS[s[value]])
            print(s[value])
            print(hashS)

        return hashS == hashT

sol = Solution()

result = sol.isAnagram('anagram','nagaram')
print(result)