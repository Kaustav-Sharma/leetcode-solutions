# Last updated: 22/10/2026, 4:43:51 pm
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=''
        c=[]
        for i in digits:
            a+=str(i)
        a=str(int(a)+1)
        for i in a:
            c.append(int(i))    
        return c