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