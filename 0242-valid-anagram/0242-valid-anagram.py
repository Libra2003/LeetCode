class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
           return False
        hashS = {}
        hashT = {}

        for value in range(len(s)):
            hashS[s[value]] = hashS.get(s[value],0)+1
            hashT[t[value]] = hashT.get(t[value],0) +1

        if hashS == hashT:
            return True
        else:
            return False