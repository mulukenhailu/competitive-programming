class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check_min_square=collections.defaultdict(set)
        for  r in range(9): 
            for c in range(9):
                if board[r][c] != ".":
                    for cc in range(c+1, 9):
                        if board[r][c] == board[r][cc]:
                            return False
                    for rr in range(r+1, 9):
                        if board[r][c] == board[rr][c]:
                            return False
                    if board[r][c] in check_min_square[(r//3, c//3)]:
                        return False
                    else:
                        check_min_square[(r//3, c//3)].add(board[r][c])
        return True