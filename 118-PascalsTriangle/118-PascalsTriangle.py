# Last updated: 22/10/2026, 6:39:52 pm
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        a=numRows
        if a==1:
            return [[1]]
        if a==2:
            return [[1],[1,1]]
        b=[[1],[1,1]]
        
        for i in range(2,a):
            c=b[i-1]
            d=[1]
            for j in range(len(c) - 1):
                d.append(c[j] + c[j+1])
            d.append(1) 
            b.append(d)
        return b