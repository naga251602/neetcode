class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkBox(board, r1, r2, c1, c2):
            s = set()
            for r in range(r1, r2+1):
                for c in range(c1, c2+1):
                    if board[r][c] in s and board[r][c] != '.': return False
                    s.add(board[r][c])
            return True

        for r in range(9):
            s1, s2 = set(), set()
            for c in range(9):
                if board[r][c] in s1 and board[r][c] != '.': return False
                s1.add(board[r][c])
                
                if board[c][r] in s2 and board[c][r] != '.': return False
                s2.add(board[c][r])
        
        r = [(0, 2), (3, 5), (6, 8)]
        c = [(0, 2), (3, 5), (6, 8)]

        for r1, r2 in r:
            for c1, c2 in c:
                if not checkBox(board, r1, r2, c1, c2): return False
                
        return True
