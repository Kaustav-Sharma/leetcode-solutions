# Last updated: 8/11/2026, 5:59:31 pm
class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows==1:
            return s

        a = [[] for i in range(numRows)]
        b = 0
        c = ''
        
        for i in s:
            if b == 0:
                c = 'plus'  
            a[b].append(i)

            if b == numRows - 1:
                c = 'minus'    
            if c == 'plus':
                b += 1
            if c == 'minus':
                b -= 1
                
        return "".join("".join(row) for row in a)