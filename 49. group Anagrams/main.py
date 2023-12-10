import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = collections.defaultdict(list)
        print(ans)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1

            ans[tuple(count)].append(s)
        print(ans)

        return ans.values()


# Create an instance of the Solution class
sol = Solution()

# Example usage:
input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = sol.groupAnagrams(input_list)
print(result)
