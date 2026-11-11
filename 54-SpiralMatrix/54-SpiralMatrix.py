# Last updated: 11/11/2026, 4:40:24 pm
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        nr = len(matrix)
        nc = len(matrix[0])
        a = []
        cr = 0
        cc = 0
        
        def r(i, j):
            nonlocal cr, cc
            if i == 0 or j == 0:
                return
            for _ in range(j):
                a.append(matrix[cr][cc])
                cc += 1
            cc -= 1  
            cr += 1  
            d(i - 1, j) 
            
        def d(i, j):
            nonlocal cr, cc
            if i == 0 or j == 0:
                return
            for _ in range(i):
                a.append(matrix[cr][cc])
                cr += 1
            cr -= 1  
            cc -= 1  
            l(i, j - 1) 
            
        def l(i, j):
            nonlocal cr, cc
            if i == 0 or j == 0:
                return
            for _ in range(j):
                a.append(matrix[cr][cc])
                cc -= 1
            cc += 1  
            cr -= 1  
            u(i - 1, j)
            
        def u(i, j):
            nonlocal cr, cc
            if i == 0 or j == 0:
                return
            for _ in range(i):
                a.append(matrix[cr][cc])
                cr -= 1
            cr += 1  
            cc += 1  
            r(i, j - 1)
        r(nr, nc)
        
        return a