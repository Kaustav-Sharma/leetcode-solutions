# Last updated: 22/10/2026, 4:43:41 pm
class Solution:
    def hammingWeight(self, n: int) -> int:
        a=0
        while n > 0:            
            if n%2 ==1:
                a+=1
            n //= 2
        return a