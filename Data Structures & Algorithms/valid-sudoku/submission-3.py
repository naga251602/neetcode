class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkBox(board, t):
            st = set()
            p, q, r, s = t
            for i in range(p, q+1):
                for j in range(r, s + 1):
                    if board[i][j] != '.':
                        if board[i][j] in st: return False
                        st.add(board[i][j])
            return True

        for i in range(9):
            r, c = [0] * 9, [0] * 9
            for j in range(9):
                if board[i][j] != '.':
                    key = int(board[i][j]) - 1
                    if c[key] != 0: return False
                    else: c[key] = 1
                
                if board[j][i] != '.':
                    key = int(board[j][i]) - 1
                    if r[key] != 0: return False
                    else: r[key] = 1
        ls = [
            (0, 2, 0, 2), (0, 2, 3, 5), (0, 2, 6, 8),
            (3, 5, 0, 2), (3, 5, 3, 5), (3, 5, 6, 8),
            (6, 8, 0, 2), (6, 8, 3, 5), (6, 8, 6, 8)
        ]

        for t in ls:
            if not checkBox(board, t): return False

        return True   