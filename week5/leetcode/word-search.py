class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r, c=len(board), len(board[0])

        def search(i, j, r, c, board, word, k):
            if k==len(word):
                return True
            if i<0 or j<0 or i==r or j==c or board[i][j] != word[k]:
                return False 

            curchar=board[i][j]
            board[i][j]="NotValid"

            search1=search(i+1, j, r, c, board, word, k+1)
            search2=search(i-1, j, r, c, board, word, k+1)
            search3=search(i, j+1, r, c, board, word, k+1)
            search4=search(i, j-1, r, c, board, word, k+1)

            board[i][j]=curchar

            return search1 or search2 or search3 or search4

        for i in range(r):
            for j in range(c):
                if word[0]==board[i][j] and search(i, j, r, c, board, word, 0):
                     return True
        return False

        
            
        