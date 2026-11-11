# Last updated: 11/11/2026, 4:43:07 pm
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        nr = len(matrix)
        nc = len(matrix[0])
        a = []
        def r(i, j, cr, cc):
            if i == 0 or j == 0:
                return
            for _ in range(j):
                a.append(matrix[cr][cc])
                cc += 1
            cc -= 1  
            cr += 1  
            d(i - 1, j, cr, cc) 
            
        def d(i, j, cr, cc):
            if i == 0 or j == 0:
                return
            for _ in range(i):
                a.append(matrix[cr][cc])
                cr += 1
            cr -= 1  
            cc -= 1  
            l(i, j - 1, cr, cc) 
            
        def l(i, j, cr, cc):
            if i == 0 or j == 0:
                return
            for _ in range(j):
                a.append(matrix[cr][cc])
                cc -= 1
            cc += 1  
            cr -= 1  
            u(i - 1, j, cr, cc)
            
        def u(i, j, cr, cc):
            if i == 0 or j == 0:
                return
            for _ in range(i):
                a.append(matrix[cr][cc])
                cr -= 1
            cr += 1  
            cc += 1  
            r(i, j - 1, cr, cc) 
        r(nr, nc, 0, 0)
        
        return a