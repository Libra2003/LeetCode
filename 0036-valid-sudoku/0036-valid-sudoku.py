class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = collections.defaultdict(set)
        row = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for rows in range(9):
            for column in range(9):
                if board[rows][column] == '.':
                    continue
                if (board[rows][column] in row[rows] or
                        board[rows][column] in col[column] or
                        board[rows][column] in square[(rows // 3, column // 3)]):
                    return False

                row[rows].add(board[rows][column])
                col[column].add(board[rows][column])
                square[(rows // 3, column // 3)].add(board[rows][column])

        return True