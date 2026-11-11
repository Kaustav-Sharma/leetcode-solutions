# Last updated: 11/11/2026, 8:39:38 pm
class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        l,h=1,x//2
        while l<=h:
            m=(l+h)//2
            if m*m==x:
                return m
            elif m*m>x:
                h=m-1
            else:
                l=m+1
        return h
            