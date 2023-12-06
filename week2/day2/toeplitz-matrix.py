class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        t=matrix[0][0]
        if len(matrix)==1:return True
        check=[len(m) for m in matrix ]
        print(check)
        print(set(check)=={1})
        if set(check)=={1}:
            return True
        else:
            for i in range(len(matrix)-1):
                for j in range(len(matrix[i])-1):
                    if matrix[i][j] != matrix[i+1][j+1]:
                        return False
            return True
                
            
            
            
        