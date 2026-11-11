# Last updated: 11/11/2026, 4:04:25 pm
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        nc=len(matrix[0])
        nr=len(matrix)
        c=[0]*nc
        r=[0]*nr
        for i in range(nr):
            for j in range(nc):
                if matrix[i][j]==0:
                    r[i],c[j]=-1,-1
        for i in range(nr):
            for j in range(nc):
                if r[i]==-1 or c[j]==-1:
                    matrix[i][j]=0