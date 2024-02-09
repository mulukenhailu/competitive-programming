class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat=matrix
        self.r=len(self.mat)
        self.c=len(self.mat[0])
        self.rowsum=[]
        self.colsum=[]


        #2d presum
        #row wise
        for i in range(self.r):
            coll=self.mat[i]
            self.rowsum=[coll[0]]
            for j in range(1,self.c):
                self.rowsum.append(self.rowsum[-1]+coll[j])
            self.mat[i]=self.rowsum
            self.rowsum=[]

        #col wise
        for i in range(self.c):
            for j in range(1,self.r):
                self.mat[j][i]=self.mat[j][i]+self.mat[j-1][i]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        side_sum, offset, upper_sum, total_sum = 0, 0, 0, 0

        if col1 > 0:
            side_sum = self.mat[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            offset = self.mat[row1 - 1][col1 - 1]
        if row1 > 0:
            upper_sum = self.mat[row1 - 1][col2]

        total_sum = self.mat[row2][col2]

        return total_sum - side_sum - upper_sum + offset

        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
