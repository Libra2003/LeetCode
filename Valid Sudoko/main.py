import collections
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        column = collections.defaultdict(set)
        square = collections.defaultdict(set)
        for rIndex,rValue in enumerate(board):
            for cIndex,cValue in enumerate(rValue):
                if cValue =='.':
                    continue
                else:
                    if (cValue in rows[rIndex]) or (cValue in column[cIndex] or (cValue in square[rIndex // 3 , cIndex // 3])):
                        return False
                    rows[rIndex].add(cValue)
                    column[cIndex].add(cValue)
                    square[(rIndex//3,cIndex // 3)].add(cValue)

        return True
sol = Solution()
board = [
 ["5", "3", ".", ".", "7", ".", ".", ".", "."]
,["6", ".", ".", "1", "9", "5", ".", ".", "."]
,[".", "9", "8", ".", ".", ".", ".", "6", "."]
,["8", ".", ".", ".", "6", ".", ".", ".", "3"]
,["4", ".", ".", "8", ".", "3", ".", ".", "1"]
,["7", ".", ".", ".", "2", ".", ".", ".", "6"]
,[".", "6", ".", ".", ".", ".", "2", "8", "."]
,[".", ".", ".", "4", "1", "9", ".", ".", "5"]
,[".", ".", ".", ".", "8", ".", ".", "7", "9"]]
result = sol.isValidSudoku(board)

print(result)