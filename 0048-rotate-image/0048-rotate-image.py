class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        seen=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i, j) not in seen and (j, i) not in seen:
                    matrix[i][j], matrix[j][i]=matrix[j][i], matrix[i][j]
                    seen.add((i, j))
                    seen.add((j, i))
        for i in range(len(matrix)):
            matrix[i]=matrix[i][::-1]