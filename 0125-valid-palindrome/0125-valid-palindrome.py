class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        last = len(s) - 1

        while start < last:
            while not s[start].isalnum() and start<last:
                start += 1
            while not s[last].isalnum()  and start<last:
                last -= 1

            if s[start].lower() != s[last].lower():
                return False
            start +=1
            last -=1

        return True