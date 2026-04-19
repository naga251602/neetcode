class Solution:
    def isValidBox(self, board, r1, r2, c1, c2):
        box = set()
        for i in range(r1, r2+1):
            for j in range(c1, c2 + 1):
                if board[i][j] != '.' and board[i][j] in box: return False
                box.add(board[i][j])
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # checking row wise and column wise duplicates
        for i in range(9):
            col_set = set()
            row_set = set()
            for j in range(9):
                if board[i][j] in row_set and board[i][j] != '.': return False
                if board[j][i] in col_set and board[j][i] != '.': return False

                col_set.add(board[j][i])
                row_set.add(board[i][j])

        r = [
            (0,2,0,2), (0, 2, 3, 5), (0, 2, 6, 8),
            (3,5,0,2), (3, 5, 3, 5), (3, 5, 6, 8),
            (6,8,0,2), (6, 8, 3, 5), (6, 8, 6, 8),
        ]

        for _, (r1, r2, c1, c2) in enumerate(r):
            if not self.isValidBox(board, r1, r2, c1, c2): return False


        return True